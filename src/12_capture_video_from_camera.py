import cv2

capture = cv2.VideoCapture(1)

width, height = capture.get(3), capture.get(4)

while(True):
    ret, frame = capture.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break