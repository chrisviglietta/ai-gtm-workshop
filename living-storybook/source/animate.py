"""Procedural 'living watercolor' animation of the 10 storybook panels.
All motion is a smooth warp of the original pixels (no repainting), periodic in T so clips loop."""
import cv2, numpy as np, subprocess, sys, os

S = 3                 # upscale factor (296x500 -> 888x1500)
FPS, T = 24, 7.0      # 7 s loops
N = int(FPS * T)
TAU = 2 * np.pi
OUT = sys.argv[1] if len(sys.argv) > 1 else 'out'
os.makedirs(OUT, exist_ok=True)

def load(k):
    p = cv2.imread(f'p{k:02d}.png'); p = p[:, :p.shape[1]//2*2]
    return cv2.resize(p, None, fx=S, fy=S, interpolation=cv2.INTER_LANCZOS4)

class Scene:
    def __init__(self, k):
        self.k = k
        self.img = load(k)
        self.H, self.W = self.img.shape[:2]
        self.Y, self.X = np.mgrid[0:self.H, 0:self.W].astype(np.float32)
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)
        self.warps, self.overlays = [], []

    # ---------- masks (native coords in, scaled out) ----------
    def box(self, x0, y0, x1, y1):
        m = np.zeros((self.H, self.W), np.float32)
        m[int(y0*S):int(y1*S), int(x0*S):int(x1*S)] = 1
        return m

    def soft(self, m, sigma):
        s = sigma * S
        m = cv2.GaussianBlur(m.astype(np.float32), (0, 0), s)
        return m / max(m.max(), 1e-6)

    def ellipse(self, cx, cy, rx, ry, p=2):
        d = ((self.X - cx*S) / (rx*S))**2 + ((self.Y - cy*S) / (ry*S))**2
        return np.exp(-d**p).astype(np.float32)

    def color_mask(self, bbox, hlo, hhi, smin, vmin=0, vmax=255):
        h, s, v = cv2.split(self.hsv)
        m = ((h >= hlo) & (h <= hhi) & (s >= smin) & (v >= vmin) & (v <= vmax)).astype(np.float32)
        return m * self.box(*bbox)

    def dark_mask(self, bbox, vmax=120):
        v = self.hsv[..., 2]
        return (v <= vmax).astype(np.float32) * self.box(*bbox)

    # ---------- warp effects: each fn(t)-> (dx,dy) backward displacement ----------
    def scarf(self, bbox, anchor, amp=2.2, wl=60, k=1, dilate=5, sigma=4, flutter=0.5):
        m = self.color_mask(bbox, 3, 18, 90)
        m = cv2.dilate(m, np.ones((dilate*S, dilate*S), np.uint8))
        m = self.soft(m, sigma)
        ax, ay = anchor[0]*S, anchor[1]*S
        ys, xs = np.nonzero(self.color_mask(bbox, 3, 18, 90))
        d2 = (xs-ax)**2 + (ys-ay)**2
        i = d2.argmax(); tip = np.array([xs[i]-ax, ys[i]-ay], np.float32)
        L = np.linalg.norm(tip); u = tip / L; pv = np.array([-u[1], u[0]])
        dist = np.sqrt((self.X-ax)**2 + (self.Y-ay)**2)
        w = (np.clip(dist / L, 0, 1.15) ** 1.3) * m
        ph0 = TAU * dist / (wl*S)
        A = amp * S
        def f(t):
            ph = TAU * k * t / T - ph0
            a = A*np.sin(ph) + A*0.25*flutter*np.sin(3*ph + 1.3)
            b = A*0.3*np.sin(2*ph + 0.7)
            return w*(a*pv[0] + b*u[0]), w*(a*pv[1] + b*u[1])
        self.warps.append(f)

    def hair(self, bbox, crown, amp=0.8, sigma=1.5, k=1, phase=0.6, exclude=None):
        m = self.soft(cv2.dilate(self.dark_mask(bbox), np.ones((2*S, 2*S), np.uint8)), sigma)
        cx, cy = crown[0]*S, crown[1]*S
        dist = np.sqrt((self.X-cx)**2 + (self.Y-cy)**2)
        w = m * np.clip(dist / (25*S), 0, 1)
        if exclude is not None:
            w = w * (1 - self.ellipse(*exclude, p=2))
        A = amp*S
        def f(t):
            ph = TAU*k*t/T - phase - self.Y/(18*S)
            return w*A*np.sin(ph), w*A*0.35*np.sin(ph*1 + 1.1)
        self.warps.append(f)

    def breathe(self, bbox, foot_y, top_y, amp=0.6, k=2, sigma=6, phase=0.0):
        m = self.soft(self.box(*bbox), sigma)
        w = m * np.clip((foot_y*S - self.Y) / ((foot_y-top_y)*S), 0, 1)
        A = amp*S
        def f(t):
            return 0*w, w*A*(0.5 - 0.5*np.cos(TAU*k*t/T + phase))
        self.warps.append(f)

    def rotate(self, center, mask, angle_fn):
        cx, cy = center[0]*S, center[1]*S
        px, py = self.X-cx, self.Y-cy
        def f(t):
            th = np.deg2rad(angle_fn(t))
            c, s = np.cos(th), np.sin(th)
            # backward map: sample src at R(-th)(p-c)+c
            sx = c*px + s*py; sy = -s*px + c*py
            return mask*(sx-px), mask*(sy-py)
        self.warps.append(f)

    def shift(self, mask, fn):
        def f(t):
            dx, dy = fn(t)
            return -mask*dx*S, -mask*dy*S
        self.warps.append(f)

    # ---------- overlays applied after warp ----------
    def stars(self, bbox, amp=0.7, smin=120, glow=3.5, seed=1, pulse=0.18, sway=3.0, exclude=()):
        h, s, v = cv2.split(self.hsv)
        m = ((h >= 12) & (h <= 32) & (s >= smin) & (v >= 170)).astype(np.uint8) * self.box(*bbox).astype(np.uint8)
        n, lab, st, _ = cv2.connectedComponentsWithStats(m)
        rng = np.random.default_rng(seed)
        layers = []
        for i in range(1, n):
            if st[i, 4] < 4*S*S: continue
            ccx, ccy = (st[i, 0] + st[i, 2]/2)/S, (st[i, 1] + st[i, 3]/2)/S
            if any(x0 <= ccx <= x1 and y0 <= ccy <= y1 for x0, y0, x1, y1 in exclude): continue
            one = (lab == i).astype(np.float32)
            core = self.soft(cv2.dilate(one, np.ones((S, S), np.uint8)), 0.7)
            halo = self.soft(one, glow)
            ph, kk = rng.uniform(0, TAU), int(rng.choice([2, 3, 4]))
            ph2 = rng.uniform(0, TAU)
            sx = (lambda ph2: lambda t: sway*S*np.sin(TAU*t/T + ph2))(ph2)
            layers.append((core, halo, ph, kk, sx))
            cx, cy = st[i, 0] + st[i, 2]/2, st[i, 1] + st[i, 3]/2
            rr = max(st[i, 2], st[i, 3])
            zm = np.exp(-(((self.X-cx)**2 + (self.Y-cy)**2) / (rr*0.9)**2)**2).astype(np.float32)
            R = rr*0.9 + 1.6*sway*S
            zt = np.exp(-(((self.X-cx)**2 + (self.Y-cy)**2) / R**2)**3).astype(np.float32)
            def zw(t, cx=cx, cy=cy, zm=zm, zt=zt, ph=ph, kk=kk, sx=sx):
                a = (0.5 + 0.5*np.sin(TAU*kk*t/T + ph))**1.6
                s = pulse*(a - 0.3)
                f = 1/(1+s) - 1
                o = sx(t)
                return zm*(self.X-cx-o)*f - zt*o, zm*(self.Y-cy)*f
            self.warps.append(zw)
        warm = np.array([150, 225, 255], np.float32)  # BGR soft gold
        def f(img, t):
            img = img.astype(np.float32)
            for core, halo, ph, kk, sx in layers:
                o = int(round(sx(t)))
                core, halo = np.roll(core, o, axis=1), np.roll(halo, o, axis=1)
                a = 0.5 + 0.5*np.sin(TAU*kk*t/T + ph)
                a = a**1.6
                g = (core*0.35 + halo*0.55) * amp * a
                img = img + (warm - img*0.6) * g[..., None] * 0.6
                img = img * (1 + core[..., None]*0.08*a)
            return img
        self.overlays.append(f)
        return len(layers)

    def sprites(self, kind, paths, size=(5, 3)):
        """Petals/leaves drifting along paths; alpha is 0 at the loop seam."""
        sw, sh = size[0]*S, size[1]*S
        pad = 4*S; bs = 2*pad + 2*max(sw, sh)
        spr = np.zeros((bs, bs, 4), np.float32)
        c = bs//2
        cv2.ellipse(spr, (c, c), (sw, sh), 0, 0, 360, (1, 1, 1, 1), -1, cv2.LINE_AA)
        alpha = cv2.GaussianBlur(spr[..., 3], (0, 0), 0.6*S)
        edge = alpha - cv2.erode(alpha, np.ones((S+1, S+1), np.uint8))
        rng = np.random.default_rng(7)
        grain = cv2.GaussianBlur(rng.normal(0, 1, (bs, bs)).astype(np.float32), (0, 0), S)
        if kind == 'petal':
            base, ink = np.array([110, 125, 210], np.float32), np.array([70, 80, 160], np.float32)
        else:
            base, ink = np.array([80, 165, 200], np.float32), np.array([50, 90, 120], np.float32)
        col = base[None, None]*(1 + 0.08*grain[..., None])
        col = col*(1-np.clip(edge, 0, 1)[..., None]*0.6) + ink*np.clip(edge, 0, 1)[..., None]*0.6
        def f(img, t):
            for (x0, y0, x1, y1, off, sway, spin, a_max) in paths:
                u = (t/T + off) % 1.0
                fade = np.clip(min(u, 1-u)/0.18, 0, 1); fade = fade*fade*(3-2*fade)
                if fade <= 0: continue
                x = (x0 + (x1-x0)*u + sway*np.sin(TAU*2*u))*S
                y = (y0 + (y1-y0)*u)*S
                ang = spin*np.sin(TAU*2*u + 0.5) + 25
                sq = 0.6 + 0.4*abs(np.cos(TAU*2*u))  # tumbling
                M = cv2.getRotationMatrix2D((c, c), ang, 1.0)
                M[:, :2] = M[:, :2] @ np.diag([1, sq])
                M[:, 2] += [x - c, y - c]
                A = cv2.warpAffine(alpha, M, (self.W, self.H))[..., None]*a_max*fade
                C = cv2.warpAffine(col, M, (self.W, self.H))
                img = img*(1-A) + C*A
            return img
        self.overlays.append(f)

    def field(self, t):
        dx = np.zeros_like(self.X); dy = np.zeros_like(self.Y)
        for w in self.warps:
            a, b = w(t); dx += a; dy += b
        return dx, dy

    def frame(self, t):
        dx, dy = self.field(t)
        fr = cv2.remap(self.img, self.X+dx, self.Y+dy, cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT).astype(np.float32)
        for o in self.overlays:
            fr = o(fr, t)
        return fr

    def planet(self, cx, cy, r, band, amp=2.5, k=1, phase=0.0):
        """Planet rocks on its axis; objects standing on its top (band px) stay put."""
        disc = ((self.X - cx*S)**2 + (self.Y - cy*S)**2 < ((r+2)*S)**2).astype(np.float32)
        disc = cv2.GaussianBlur(disc, (0, 0), 1.0*S)
        top = (cy - r + band)*S
        m = disc * np.clip((self.Y - top) / (14*S), 0, 1)
        self.rotate((cx, cy), m, lambda t: amp*np.sin(TAU*k*t/T + phase))

    def shooting_star(self, p0, p1, t0, dur=1.1, tail=0.35, width=1.4):
        warm = np.array([175, 235, 255], np.float32)
        p0, p1 = np.array(p0, np.float32)*S, np.array(p1, np.float32)*S
        def f(img, t):
            u = (t - t0) / dur
            if u <= 0 or u >= 1 + tail: return img
            lay = np.zeros(img.shape[:2], np.float32)
            n = 14
            for j in range(n):
                a0 = u - tail*j/n; a1 = u - tail*(j+1)/n
                if a0 < 0: break
                q0 = p0 + (p1-p0)*min(a0, 1); q1 = p0 + (p1-p0)*max(min(a1, 1), 0)
                cv2.line(lay, tuple(int(v) for v in q0), tuple(int(v) for v in q1), float((1-j/n)**1.5),
                         max(1, int(width*S*(1-j/n*0.6))), cv2.LINE_AA)
            if u < 1:
                h = p0 + (p1-p0)*u
                cv2.circle(lay, (int(h[0]), int(h[1])), int(1.6*S), 1.0, -1, cv2.LINE_AA)
            lay = cv2.GaussianBlur(lay, (0, 0), 0.8*S) + cv2.GaussianBlur(lay, (0, 0), 3*S)*0.6
            fade = min(1.0, u/0.15, (1+tail-u)/0.3)
            a = np.clip(lay*0.85*fade, 0, 1)[..., None]
            return img*(1-a) + warm*a
        self.overlays.append(f)

    def render(self, name):
        path = f'{OUT}/{name}.mp4'
        cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'bgr24',
               '-s', f'{self.W}x{self.H}', '-r', str(FPS), '-i', '-', '-an',
               '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p',
               '-movflags', '+faststart', path]
        pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for i in range(N):
            t = i / FPS
            fr = np.clip(self.frame(t), 0, 255).astype(np.uint8)
            if i in (0, N//4, N//2): cv2.imwrite(f'{OUT}/{name}_f{i:03d}.jpg', fr)
            pr.stdin.write(fr.tobytes())
        pr.stdin.close(); pr.wait()
        print('wrote', path)

def bump(t, t0, t1):
    """raised-cosine bump between t0..t1 seconds (0 elsewhere): one-off gesture that returns."""
    if t < t0 or t > t1: return 0.0
    return 0.5 - 0.5*np.cos(TAU*(t-t0)/(t1-t0))

def ease_hold(t, t0, t1, t2, t3):
    """0 -> 1 (t0..t1), hold, 1 -> 0 (t2..t3)."""
    sm = lambda x: x*x*(3-2*x)
    if t < t0 or t > t3: return 0.0
    if t < t1: return sm((t-t0)/(t1-t0))
    if t < t2: return 1.0
    return sm(1-(t-t2)/(t3-t2))

sin = lambda k, ph=0: (lambda t: np.sin(TAU*k*t/T + ph))
