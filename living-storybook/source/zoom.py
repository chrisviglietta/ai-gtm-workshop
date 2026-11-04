import cv2,sys,numpy as np
k,x0,y0,x1,y1,s=map(int,sys.argv[1:7])
p=cv2.imread(f'p{k:02d}.png')[y0:y1,x0:x1]
q=cv2.resize(p,None,fx=s,fy=s,interpolation=cv2.INTER_CUBIC)
for v in range((x0//10+1)*10,x1,10):
  X=(v-x0)*s; cv2.line(q,(X,0),(X,q.shape[0]),(0,0,255) if v%50==0 else (200,150,150),1)
  if v%50==0: cv2.putText(q,str(v),(X+2,12),0,0.4,(0,0,255),1)
for v in range((y0//10+1)*10,y1,10):
  Y=(v-y0)*s; cv2.line(q,(0,Y),(q.shape[1],Y),(0,0,255) if v%50==0 else (200,150,150),1)
  if v%50==0: cv2.putText(q,str(v),(2,Y-2),0,0.4,(0,0,255),1)
cv2.imwrite(sys.argv[7],q)
