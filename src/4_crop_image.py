import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg')

# crop image [y:y+h, x:x+w]
crop_img = img[50:200, 50:200]

# display image
cv2.imshow('Image', img)
cv2.imshow('Crop Image', crop_img)
cv2.waitKey(0)


