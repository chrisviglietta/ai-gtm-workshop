import sys
from animate import *

def capsule(sc, a, b, r, sigma=2):
    ax, ay, bx, by = a[0]*S, a[1]*S, b[0]*S, b[1]*S
    vx, vy = bx-ax, by-ay; L2 = vx*vx + vy*vy
    u = np.clip(((sc.X-ax)*vx + (sc.Y-ay)*vy)/L2, 0, 1)
    d = np.hypot(sc.X-(ax+u*vx), sc.Y-(ay+u*vy))
    m = (d < r*S).astype(np.float32)
    return sc.soft(m, sigma), u

def s1():
    sc = Scene(1)
    sc.scarf((140, 130, 296, 185), (150, 150), amp=2.4, wl=70)
    sc.hair((95, 92, 168, 160), (130, 98), amp=0.9)
    sc.stars((0, 0, 296, 110))
    for i, (x, y) in enumerate([(86, 238), (227, 258), (262, 299), (174, 326), (106, 390), (20, 320)]):
        m = sc.ellipse(x, y, 9, 9)
        sc.rotate((x, y+13), m, (lambda ph: lambda t: 3.0*np.sin(TAU*t/T + ph))(i*1.1))
    torso = sc.ellipse(140, 180, 48, 52)
    sc.rotate((140, 228), torso, lambda t: -0.9*bump(t, 2.2, 5.0))
    sc.breathe((95, 95, 190, 225), 225, 110, amp=0.45, k=2)
    return sc

def s2():
    sc = Scene(2)
    sc.scarf((10, 140, 170, 245), (165, 160), amp=2.4, wl=65)
    sc.hair((125, 100, 190, 180), (158, 106), amp=0.8)
    sc.stars((0, 0, 296, 140), amp=0.45)
    head = sc.ellipse(155, 128, 24, 30)
    sc.rotate((162, 160), head, lambda t: -2.2*ease_hold(t, 0.8, 3.0, 4.6, 6.8))
    sc.breathe((105, 150, 215, 372), 372, 150, amp=0.5, k=2)
    return sc

def s3():
    sc = Scene(3)
    sc.scarf((0, 150, 162, 222), (152, 158), amp=2.2, wl=65)
    sc.hair((115, 92, 185, 165), (148, 96), amp=0.8)
    upper = sc.ellipse(148, 168, 42, 78)
    sc.rotate((146, 240), upper, lambda t: 1.6*ease_hold(t, 0.6, 2.8, 4.6, 6.8))
    for (x0, y0, x1, y1, bx, by) in [(0, 230, 80, 500, 40, 500), (165, 195, 296, 500, 230, 500)]:
        m = sc.soft(sc.box(x0, y0, x1, y1), 6)
        sc.rotate((bx, by), m, (lambda ph: lambda t: 0.35*np.sin(TAU*t/T + ph))(bx/40))
    sc.sprites('petal', [(222, 218, 178, 345, 0.00, 6, 60, 0.85),
                         (60, 250, 96, 380, 0.50, 5, 50, 0.8)], size=(3, 2))
    return sc

def s4():
    sc = Scene(4)
    sc.scarf((0, 165, 108, 235), (100, 183), amp=2.0, wl=55)
    sc.hair((115, 120, 190, 185), (152, 126), amp=0.8)
    sc.breathe((110, 140, 200, 250), 250, 140, amp=0.4, k=2)
    leg = sc.ellipse(192, 292, 18, 44)
    sc.rotate((178, 248), leg, lambda t: 3.2*np.sin(TAU*t/T))
    # sun: sinks a little behind the horizon (backward map, clipped at horizon line)
    om = sc.color_mask((200, 190, 265, 250), 5, 25, 110)
    ys, xs = np.nonzero(om); hy = ys.max() - 1*S
    sm = sc.box(200, 185, 265, 260); sm[hy:] = 0
    sm[:, :] *= cv2.GaussianBlur(sc.box(198, 0, 267, 500), (0, 0), 2*S)
    sc.shift(sm, lambda t: (0, 1.6*t/T))
    clouds = sc.soft(sc.box(185, 160, 296, 270), 5) * (1 - sc.ellipse(230, 225, 22, 22))
    sc.shift(clouds, lambda t: (1.2*np.sin(TAU*t/T), 0))
    return sc

def s5():
    sc = Scene(5)
    sc.scarf((0, 185, 120, 320), (165, 198), amp=1.8, wl=60)
    sc.hair((128, 135, 205, 210), (165, 142), amp=0.8)
    lean = sc.ellipse(140, 195, 48, 70)
    sc.rotate((115, 305), lean, lambda t: 1.1*ease_hold(t, 1.0, 3.2, 4.8, 6.9))
    tilt = lambda t: 6.0*ease_hold(t, 0.8, 2.4, 4.8, 6.4)
    head = sc.ellipse(198, 236, 21, 18)
    sc.rotate((206, 256), head, tilt)
    tail = sc.ellipse(266, 320, 34, 16)
    sc.rotate((236, 312), tail, lambda t: 4.0*np.sin(TAU*t/T + 0.8) + 1.5*np.sin(TAU*2*t/T))
    fur = sc.img[int(238*S):int(242*S), int(204*S):int(208*S)].reshape(-1, 3).mean(0)
    def blink(img, t):
        a = bump(t, 3.3, 3.62)
        if a <= 0: return img
        th = np.deg2rad(tilt(t)); c, s = np.cos(th), np.sin(th)
        qx, qy = 200-206, 232-256
        ex, ey = (206 + c*qx - s*qy)*S, (256 + s*qx + c*qy)*S
        m = np.zeros(img.shape[:2], np.float32)
        cv2.circle(m, (int(ex), int(ey)), int(1.9*S), 1, -1, cv2.LINE_AA)
        m = cv2.GaussianBlur(m, (0, 0), 0.6*S)[..., None]*a
        img = img*(1-m) + fur*m
        l = np.zeros(img.shape[:2], np.float32)
        cv2.ellipse(l, (int(ex), int(ey)), (int(1.8*S), int(0.6*S)), -20, 10, 170, 1, max(1, S//2), cv2.LINE_AA)
        l = l[..., None]*a*0.8
        return img*(1-l) + np.array([40, 50, 70], np.float32)*l
    sc.overlays.append(blink)
    return sc

def s6():
    sc = Scene(6)
    sc.scarf((60, 210, 172, 275), (170, 231), amp=2.2, wl=55, k=2)
    sc.hair((150, 192, 192, 242), (172, 197), amp=0.8, k=2)
    sc.breathe((110, 190, 205, 340), 337, 195, amp=0.7, k=2)
    for i, (cx, cy, px) in enumerate([(178, 310, 168), (146, 310, 160)]):
        m = sc.ellipse(cx, cy, 13, 26)
        sc.rotate((px, 282), m, (lambda sgn: lambda t: sgn*2.2*np.sin(TAU*2*t/T))(1 if i == 0 else -1))
    # drifting wisps of watercolor sand (tileable streak texture scrolled one tile per loop)
    rng = np.random.default_rng(3)
    P = 296*S//2
    tex = rng.random((sc.H, P)).astype(np.float32)
    tex = cv2.GaussianBlur(np.tile(tex, (1, 3)), (0, 0), sigmaX=26*S/3, sigmaY=1.2*S)[:, P:2*P]
    tex = (tex - tex.mean())/tex.std()
    a = np.clip((tex - 1.3)*0.6, 0, 1)
    rows = np.clip((sc.Y[:, :P] - 300*S)/(60*S), 0, 1) * np.clip((470*S - sc.Y[:, :P])/(60*S), 0, 1)
    a = a*rows*0.16
    sand = np.array([110, 165, 205], np.float32)
    def wisps(img, t):
        sh = int(round(P*t/T))
        A = np.tile(np.roll(a, sh, axis=1), (1, 3))[:, :sc.W][..., None]
        return img*(1-A) + sand*A
    sc.overlays.append(wisps)
    return sc

def s7():
    sc = Scene(7)
    sc.scarf((15, 140, 152, 240), (152, 140), amp=2.6, wl=65)
    sc.hair((105, 92, 165, 150), (140, 98), amp=0.8)
    sc.stars((185, 15, 245, 62), amp=0.55, glow=4.0)
    sc.breathe((85, 75, 205, 338), 338, 80, amp=0.6, k=1, phase=0)
    m, u = capsule(sc, (165, 120), (197, 66), 9)
    dvec = np.array([197-165, 66-120], np.float32); dvec /= np.linalg.norm(dvec)
    w = m*np.clip(u*1.1, 0, 1)
    sc.shift(w, lambda t: tuple(dvec*1.6*(0.5-0.5*np.cos(TAU*t/T))))
    return sc

def s8():
    sc = Scene(8)
    sc.scarf((0, 215, 108, 362), (122, 222), amp=1.5, wl=70)
    sc.hair((78, 160, 168, 240), (125, 168), amp=0.8, exclude=(132, 212, 12, 14))
    canopy = sc.ellipse(110, 95, 108, 62)
    sc.rotate((38, 330), canopy, lambda t: 0.35*np.sin(TAU*t/T))
    loose = sc.soft(sc.box(212, 80, 296, 295), 4)
    sc.shift(loose, lambda t: (0.9*np.sin(TAU*t/T + 0.4), 0.7*np.sin(TAU*2*t/T)))
    sc.breathe((70, 170, 185, 330), 330, 175, amp=0.4, k=2)
    # right page lifts and settles once (spine -> outer edge)
    page = sc.soft(sc.box(206, 244, 241, 300), 2) * np.clip((sc.X - 206*S)/(32*S), 0, 1)
    sc.shift(page, lambda t: (-2.2*bump(t, 2.4, 5.0), -1.2*bump(t, 2.4, 5.0)))
    sc.sprites('leaf', [(150, 125, 188, 335, 0.00, 7, 70, 0.85),
                        (205, 110, 250, 300, 0.33, 6, 60, 0.8),
                        (95, 140, 130, 300, 0.66, 5, 80, 0.75)], size=(3, 2))
    return sc

def s9():
    sc = Scene(9)
    sc.scarf((60, 150, 165, 205), (168, 168), amp=2.0, wl=50, k=2)
    sc.hair((143, 132, 188, 182), (165, 137), amp=0.7, k=2)
    sc.stars((0, 0, 296, 120))
    sc.breathe((110, 135, 215, 278), 276, 140, amp=0.5, k=2)
    for (piv, c, sg) in [((148, 184), (126, 194), 1), ((171, 183), (192, 192), -1)]:
        m = sc.ellipse(*c, 23, 9)
        sc.rotate(piv, m, (lambda sg: lambda t: sg*2.6*np.sin(TAU*t/T))(sg))
    for (cx, sg) in [(146, 1), (176, -1)]:
        m = sc.ellipse(cx, 248, 12, 26)
        sc.rotate((162, 218), m, (lambda sg: lambda t: sg*1.6*np.sin(TAU*2*t/T))(sg))
    return sc

def s10():
    sc = Scene(10)
    sc.scarf((0, 130, 140, 232), (128, 147), amp=2.4, wl=70)
    sc.hair((105, 88, 172, 160), (136, 93), amp=0.9)
    sc.breathe((95, 90, 180, 325), 322, 95, amp=0.5, k=2)
    clouds = sc.soft(sc.box(168, 150, 296, 265), 5)
    sc.shift(clouds, lambda t: (2.0*np.sin(TAU*t/T), 0))
    return sc

SCENES = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
NAMES = ['01-little-planet', '02-among-the-stars', '03-rose-garden', '04-sunset', '05-the-fox',
         '06-desert-walk', '07-reaching-for-a-star', '08-beneath-the-tree', '09-between-planets', '10-horizon']
if __name__ == '__main__':
    which = [int(a) for a in sys.argv[2:]] or range(1, 11)
    for i in which:
        SCENES[i-1]().render(NAMES[i-1])
