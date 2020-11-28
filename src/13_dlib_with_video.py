from imutils import face_utils
import dlib
import cv2
import numpy as np

capture = cv2.VideoCapture(1)

p = 'data/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)
width, height = capture.get(3), capture.get(4)

while(True):
    ret, frame = capture.read()
    rects = detector(frame, 0)

    for (i, rect) in enumerate(rects):
        shape = predictor(frame, rect)
        shape = face_utils.shape_to_np(shape)

        for (i, (x, y)) in enumerate(shape):
            # cv2.putText(frame, str(i), (x, y),  cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 2)

            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
