import cv2
import numpy as np
import dlib

# left_eye
# right_eye
# nose
# lips
# left_eyebrow
# right_eyebrow
# face

detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


class extract:
    def __init__(self, path):
        self.path = path
        self.img_original = cv2.imread(self.path)
        # self.img_original = cv2.resize(self.img_original,(0,0), None, 0.3, 0.3)
        self.parts = {'face': [i for i in range(0,17)], 'left_eyebrow': [i for i in range(17,22)],
                      'right_eyebrow': [i for i in range(22,27)], 'nose': [i for i in range(27,36)],
                      'left_eye': [i for i in range(36,42)], 'right_eye': [i for i in range(42,48)],
                      'lips': [i for i in range(48,61)]}

    def extract_part(self, points, scale=1):
        part = np.zeros_like(self.img_original)
        part = cv2.fillPoly(part, [points], (255,255,255))
        img = cv2.bitwise_and(self.img_original,part)
        bounding_box = cv2.boundingRect(points)
        x, y, w, h = bounding_box
        img_crop = img[y:y+h, x:x+w]
        img_crop = cv2.resize(img_crop, (0,0), None, scale,scale)
        return img_crop

    def detect_face_part(self, face_part, show_detected_face=False, save_file=False):
        img = self.img_original.copy()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detect(img_gray)

        for face in faces:
            img = self.img_original.copy()
            dots = []
            left, top, right, bottom = face.left(), face.top(), face.right(), face.bottom()
            img = cv2.rectangle(img, (left,top), (right, bottom), (0,255,0), 2)
            pointers = predict(img, face)

            for dot in range(68):
                x = pointers.part(dot).x
                y = pointers.part(dot).y
                dots.append([x,y])

            dots = np.asarray(dots)
            show = self.extract_part(dots[self.parts[face_part][0]:self.parts[face_part][-1]+1], 1)
            if show_detected_face:
                cv2.imshow('face_detect', img)
            if save_file:
                cv2.imwrite(face_part + '.jpg', show)
            cv2.imshow(face_part, show)
            cv2.waitKey(0)


start = extract() # write path of the image file
start.dectect_face_part() # write one of the face part / True or False to show the detected face (default=False) / True or False to save file which is part of the face (defalut=False)
# start = extract('./images/image.jpg')
# start.detect_face_part('left_eye',True,True)
