import cv2
import numpy

photo = cv2.imread('images/1.jpg')
img = numpy.zeros(photo.shape[:2],dtype='uint8')

circle = cv2.circle(img.copy(), (200,300), 80, 255, -1)
square = cv2.rectangle(img.copy(), (25,25), (250,350), 255, -1)



img = cv2.bitwise_and(photo, photo, mask=square)
cv2.imshow("Result",img)
cv2.waitKey(0)

