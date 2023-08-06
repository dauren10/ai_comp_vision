import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl
img  = cv2.imread('images/car1.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)


pl.imshow(cv2.cvtColor(edges,cv2.COLOR_BGR2RGB))
pl.show()