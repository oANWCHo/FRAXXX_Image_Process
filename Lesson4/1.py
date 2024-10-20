import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input-image-of-wood.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

blur = cv2.blur(img, (5,5))

gaussian = cv2.GaussianBlur(img, (5,5), 0)

median = cv2.medianBlur(img, 5)

bilateral = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(321),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(dst),plt.title('Averaging 5x5')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(blur),plt.title('Blur 5x5')

plt.xticks([]), plt.yticks([])

plt.subplot(324),plt.imshow(gaussian),plt.title('Gaussian Blur 5x5')

plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(median),plt.title('Median Blur')
plt.xticks([]), plt.yticks([])
plt.subplot(326),plt.imshow(bilateral),plt.title('Bilateral')
plt.xticks([]), plt.yticks([])
plt.show()