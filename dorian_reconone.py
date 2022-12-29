import os
import cv2
import tensorflow
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
from numpy.lib.polynomial import poly

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = os.path.join(folder,filename)
        if img is not None:
            images.append(img)
    return images

images = load_images_from_folder("images")

for imageFile in images :
    img = cv2.imread(imageFile)
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    box, label, count = cv.detect_common_objects(img)
    output = draw_bbox(img, box, label, count)

    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    plt.figure(figsize=(10,10))
    plt.axis('off')
    plt.imshow(output)
    plt.show()

    print("Nombre de personnes sur l'image : " + str(len(label)))