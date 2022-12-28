import cv2
img=cv2.imread('solar-system.jpg') 
cv2.putText (img,'Sun',(110,110),cv2.FONT_HERSHEY_COMPLEX,0.9,(0,0,255))
cv2.putText (img,'Mercury',(110,240),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText (img,'Venus',(200,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText (img,'Earth',(290,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText (img,'Mars',(380,260),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText (img,'Jupiter',(500,380),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText (img,'Saturn',(790,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText (img,'Urains',(990,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText (img,'Neptune',(1100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imwrite('Solar_systemwithname.jpg',img)
cv2.imshow('output',img)
cv2.waitKey(0) 


