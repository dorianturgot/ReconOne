import tensorflow as tf
import cv2

import cvlib as cv
import os

def countPeople():
    capture = cv2.VideoCapture("video1.mp4")
    frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    framerate = frame_count / 100
    nbPersonnes = []
    if capture:
        while True:
            ret, frame = capture.read()
            if ret:
                box, label, count = cv.detect_common_objects(frame)
                # print le nb de personnes
                #print(len(label))
                nbPersonnes.append(len(label))        
                cv2.imshow("Track", frame)
                framerate += 30
                capture.set(cv2.CAP_PROP_POS_FRAMES, framerate)
            key = cv2.waitKey(100)
            if key == ord('q'):
                    break
    return nbPersonnes

print(countPeople())
