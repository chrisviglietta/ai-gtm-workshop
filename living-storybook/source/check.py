import cv2,numpy as np,sys,subprocess
name=sys.argv[1]
cap=cv2.VideoCapture(f'{sys.argv[2] if len(sys.argv)>2 else 'out2'}/{name}.mp4'); fr=[]
while True:
  ok,f=cap.read()
  if not ok: break
  fr.append(f)
fr=np.array(fr); print(name,len(fr))
idx=[0,28,56,84,112,140]
d=np.abs(fr.astype(int)-fr[0].astype(int)).max(0).max(-1).astype(np.uint8)
d=cv2.applyColorMap(np.clip(d*3,0,255).astype(np.uint8),cv2.COLORMAP_INFERNO)
row=[cv2.resize(fr[i],None,fx=.5,fy=.5) for i in idx]+[cv2.resize(d,None,fx=.5,fy=.5)]
cv2.imwrite(f'{sys.argv[2] if len(sys.argv)>2 else 'out2'}/{name}_sheet.jpg',np.hstack(row))
print('loop seam diff',np.abs(fr[-1].astype(int)-fr[0].astype(int)).mean(), 'step',np.abs(fr[1].astype(int)-fr[0].astype(int)).mean())
