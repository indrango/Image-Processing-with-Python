from imutils import face_utils
from collections import OrderedDict
import dlib
import cv2

FACIAL_LANDMARKS_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 35)),
	("jaw", (0, 17))
])

p = 'data/shape_predictor_68_face_landmarks.dat'
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

image = cv2.imread('images/elon-musk.jpg')
image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))

rects = detector(image, 0)

for (i, rect) in enumerate(rects):
    shape = predictor(image, rect)
    shape = face_utils.shape_to_np(shape)

    for (name, (i, j)) in FACIAL_LANDMARKS_IDXS.items():
        clone = image.copy()
        cv2.putText(clone, name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)

        for (x, y) in shape[i:j]:
            cv2.circle(clone, (x, y), 2, (0, 0, 255), -1)

        cv2.imshow('Output', clone)
        cv2.waitKey(0)