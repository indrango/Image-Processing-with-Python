import cv2
import numpy as np

# read image
img = cv2.imread('images/lena.jpg')

# add rectangle / bounding box
x1 = 50
x2 = 200
y1 = 50
y2 = 200
cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

# add line
cv2.line(img, (0, 0), (40, 40), (255, 0, 0), 5)

# add circle
cv2.circle(img, (200, 220), 5, (0, 255, 255), -1)

# add eclipse
cv2.ellipse(img, (150, 150), (20, 20), 0, 0, 270, (255, 0, 0), -1)

# add text
cv2.putText(img, 'My Name is Lena', (50, 30),  cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

# add polylines
pts = np.array([[10, 5],  [50, 10], [70, 20], [20, 30]], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255), thickness=2)

# display image
cv2.imshow('Image', img)
cv2.waitKey(0)