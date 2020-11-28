import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg')

# write image
cv2.imwrite('images/gambar_baru_lena.png', img)

