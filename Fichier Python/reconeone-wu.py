from matplotlib.patches import draw_bbox
import numpy as np
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bboxpip
from numpy.lib.polynomial import poly

img = cv.imread('imagegroupe.jpg')
img1 = cv.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(img1)
plt.show()

box, label, count = cv.detect_common_objects(img)
output = draw_bbox(img, box, label, count)
output = cv.cvtColor(output,cv.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(output)
plt.show()

print(f"Number of objects in this image are {len(label)}")