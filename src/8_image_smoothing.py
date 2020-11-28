import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg')

# add basic blur
blur = cv2.blur(img, (3, 3))

# add gaussian blur
gau_blur = cv2.GaussianBlur(img, (3, 3), 0)

# display image
res = np.hstack((img, blur, gau_blur))
cv2.imshow('Image', res)
cv2.waitKey(0)