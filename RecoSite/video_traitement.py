import tensorflow as tf
import cv2

import cvlib as cv
import os
import math

def countPeople(filename, percentage = 400):
    capture = cv2.VideoCapture(filename)
    frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    #print("framecount = " + str(frame_count))
    framerate = frame_count / percentage
    s_par_image=framerate
    nbPersonnes = []
    if capture:
        oldbox = []
        while framerate < frame_count:
            ret, frame = capture.read()
            if ret:
                box, label, count = cv.detect_common_objects(frame)
                totalNewPersonOnFrame = 0
                for i in range (len(box)):
                    """ Vérifie que les nouvelles personnes comptées n'ont pas déjà été comptées en vérifiant
                    la distance avec leur ancienne position """
                    if i >= len(oldbox) or (math.sqrt((oldbox[i][0] - box[i][0])**2)) > 350:
                        if label[i] == "person" :
                            totalNewPersonOnFrame += round(count[i], 3)
                
                nbPersonnes.append(totalNewPersonOnFrame)
                cv2.imshow("Track", frame)
                framerate += 30
                capture.set(cv2.CAP_PROP_POS_FRAMES, framerate)
                
                oldbox = box
            key = cv2.waitKey(100)
    return nbPersonnes, frame_count, percentage,s_par_image

#print(countPeople())
