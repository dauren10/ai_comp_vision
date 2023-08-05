import cv2
import numpy as np

img =  cv2.imread('images/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r, g, b = cv2.split(img)

img = cv2.merge([b,g,r])

cv2.imshow('Result', img)

cv2.waitKey(0)