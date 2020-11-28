import cv2
import numpy as np

# add images
img1 = cv2.imread('images/lena_small.jpg')
img2 = cv2.imread('images/opencv-logo-white.png')
res = cv2.addWeighted(img1, .6, img2, .4, 0)

# show images
cv2.imshow('Image Blending', res)
cv2.waitKey(0)