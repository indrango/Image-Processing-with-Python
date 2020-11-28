import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg')
print(img.shape)

# resize image 1
resize_img1 = cv2.resize(img, (int(img.shape[0]/3), int(img.shape[1]/2)))
print(resize_img1.shape)

# resize image 2
x1 = 50
y1 = 100
resize_img2 = cv2.resize(img, (x1, y1))
print(resize_img2.shape)

# display image
cv2.imshow('Image', img)
cv2.imshow('Resize Image 1', resize_img1)
cv2.imshow('Resize Image 2', resize_img2)
cv2.waitKey(0)


