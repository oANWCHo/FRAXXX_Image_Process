import numpy as np
import cv2
from matplotlib import pyplot as plt

# img = cv2.imread('fibo building.jpg',1)
img = plt.imread('fibo building.jpg',1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([]) #hide number scale
plt.show()
cv2.imwrite('fibo building from matplot.png')