import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg')

# gray color
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# lab color
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# ycrcb color
ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

# hsv color
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# display image
cv2.imshow('Image', img)
cv2.imshow('Gray', gray_img)
cv2.imshow('Lab', lab_img)
cv2.imshow('Ycrcb', ycrcb_img)
cv2.imshow('HSV', hsv_img)
cv2.waitKey(0)

# https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/