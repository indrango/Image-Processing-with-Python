from imutils import face_utils
import dlib
import cv2
import numpy as np

capture = cv2.VideoCapture(1)

p = 'data/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)
width, height = capture.get(3), capture.get(4)

face_rectangle = [17, 26, 8]

while(True):
    ret, frame = capture.read()
    rects = detector(frame, 0)

    for (i, rect) in enumerate(rects):
        shape = predictor(frame, rect)
        shape = face_utils.shape_to_np(shape)

        left_side, right_size, bottom_side = shape[face_rectangle]
        cv2.rectangle(frame, (left_side[0]-20, left_side[1]-20), (right_size[0]+20, bottom_side[1]), (255, 0, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
