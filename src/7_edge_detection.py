import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg', 0)

# add canny filter
edges = cv2.Canny(img, 30, 70)

# add threshold binary & otsu
_, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# display image
cv2.imshow('Edge Detection', np.hstack((img, thresh, edges)))
cv2.waitKey(0)