from imutils import face_utils
from collections import OrderedDict
import dlib
import cv2

def shape_to_numpy_array(shape, dtype="int"):
    coordinates = np.zeros((68, 2), dtype=dtype)

    for i in range(0, 68):
        coordinates[i] = (shape.part(i).x, shape.part(i).y)

    return coordinates

def visualize_facial_landmarks(image, shape, colors=None, alpha=0.75):
    overlay = image.copy()
    output = image.copy()

    if colors is None:
        colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
                  (168, 100, 168), (158, 163, 32),
                  (163, 38, 32), (180, 42, 220)]

    for (i, name) in enumerate(FACIAL_LANDMARKS_IDXS.keys()):
        (j, k) = FACIAL_LANDMARKS_IDXS[name]
        pts = shape[j:k]
        facial_features_cordinates[name] = pts

        if name == "jaw":
            for l in range(1, len(pts)):
                ptA = tuple(pts[l - 1])
                ptB = tuple(pts[l])
                cv2.line(overlay, ptA, ptB, colors[i], 2)

        else:
            hull = cv2.convexHull(pts)
            cv2.drawContours(overlay, [hull], -1, colors[i], -1)

    cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)

    return output


def main():
    global facial_features_cordinates
    global FACIAL_LANDMARKS_IDXS
    
    facial_features_cordinates = {}

    FACIAL_LANDMARKS_IDXS = OrderedDict([
        ("mouth", (48, 68)),
        ("right_eyebrow", (17, 22)),
        ("left_eyebrow", (22, 27)),
        ("right_eye", (36, 42)),
        ("left_eye", (42, 48)),
        ("nose", (27, 35)),
        ("jaw", (0, 17))
    ])

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

            output = visualize_facial_landmarks(frame, shape)

            cv2.imshow('frame', output)

        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == "__main__":
    main()