import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('sample.jpeg')
imgplot = plt.imshow(img)
plt.show()