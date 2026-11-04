"""Split a storybook sheet into panels: python3 crop_sheet.py SHEET FIRST_NUMBER [INSET]

Finds the light gutters automatically, writes pNN.png (native size) and gridNN.png
(2x, with native-pixel coordinate labels every 50px) for reading coordinates."""
import sys, cv2, numpy as np

sheet, first = sys.argv[1], int(sys.argv[2])
inset = int(sys.argv[3]) if len(sys.argv) > 3 else 4
im = cv2.imread(sheet)
g = im.astype(float).mean(2)

def gaps(v):
    thr = v.mean() + (v.max() - v.mean())*0.6
    idx = np.where(v > thr)[0]
    runs, s, p = [], idx[0], idx[0]
    for i in idx[1:]:
        if i != p + 1: runs.append((s, p)); s = i
        p = i
    runs.append((s, p))
    runs = [r for r in runs if r[1] - r[0] >= 3 or r[0] == 0 or r[1] == len(v) - 1]
    return [(runs[i][1] + 1, runs[i+1][0] - 1) for i in range(len(runs) - 1)]

cols, rows = gaps(g.mean(0)), gaps(g.mean(1))
k = first
for y0, y1 in rows:
    for x0, x1 in cols:
        if x1 - x0 < 50 or y1 - y0 < 50: continue
        p = im[y0+inset:y1-inset+1, x0+inset:x1-inset+1]
        cv2.imwrite(f'p{k:02d}.png', p)
        q = cv2.resize(p, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        for v in range(0, q.shape[1], 20):
            cv2.line(q, (v, 0), (v, q.shape[0]), (0, 0, 255) if v % 100 == 0 else (230, 180, 180), 1)
        for v in range(0, q.shape[0], 20):
            cv2.line(q, (0, v), (q.shape[1], v), (0, 0, 255) if v % 100 == 0 else (230, 180, 180), 1)
        for v in range(0, q.shape[1], 100): cv2.putText(q, str(v//2), (v+2, 14), 0, 0.45, (0, 0, 200), 1)
        for v in range(100, q.shape[0], 100): cv2.putText(q, str(v//2), (2, v-3), 0, 0.45, (0, 0, 200), 1)
        cv2.imwrite(f'grid{k:02d}.png', q)
        print(k, p.shape[1], 'x', p.shape[0])
        k += 1
