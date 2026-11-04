"""Overlay where warps (red) and glows (blue) act, to catch misplaced regions before rendering."""
import sys, cv2, numpy as np, importlib
from animate import T, S
sys.argv = ['x', 'out3'] + sys.argv[1:]
mod = importlib.import_module(sys.argv[2]); ks = [int(a) for a in sys.argv[3:]]
import os; os.makedirs('out3', exist_ok=True)
rows = []
for k in ks:
    sc = mod.SCENES[k]()
    mag = np.zeros(sc.X.shape, np.float32)
    for t in np.linspace(0, T, 9)[:-1]:
        dx, dy = sc.field(t); mag = np.maximum(mag, np.hypot(dx, dy))
    ov = np.zeros_like(mag)
    for t in np.linspace(0, T, 9)[:-1]:
        f = sc.img.astype(np.float32)
        for o in sc.overlays: f = o(f, t)
        ov = np.maximum(ov, np.abs(f - sc.img).max(-1))
    v = sc.img.astype(np.float32)*0.55
    v[..., 2] += np.clip(mag/(2*S), 0, 1)*140
    v[..., 0] += np.clip(ov/40, 0, 1)*140
    v = cv2.resize(np.clip(v, 0, 255).astype(np.uint8), (288, 485))
    for g in range(0, 485, 50): cv2.line(v, (0, g), (6, g), (0, 0, 0), 1)
    rows.append(v)
cv2.imwrite(f'out3/mm_{ks[0]}.jpg', np.hstack(rows))
