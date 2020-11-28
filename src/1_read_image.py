import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg')

# display image
cv2.imshow('Image', img)
cv2.waitKey(0)
