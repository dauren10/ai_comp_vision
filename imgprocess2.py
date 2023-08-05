import cv2
import numpy as np

photo = np.zeros((500,500, 3), dtype='uint8')
#photo[10:150, 200:280] = 255, 0, 0

cv2.rectangle(photo, (220,220), (100,100),(0, 128, 0), thickness=cv2.FILLED)
cv2.line(photo, (0,photo.shape[0]//2), (photo.shape[1],photo.shape[0]//2), (0, 128, 0), thickness=2)

cv2.circle(photo, (photo.shape[1]//2,photo.shape[0]//2), 50, (0,128,0), thickness=cv2.FILLED )
cv2.putText(photo, 'Dauren', (100,150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,0,0),thickness=3) 
cv2.imshow('Photo',photo)
cv2.waitKey(0)
