import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('windows.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(221),plt.imshow(img, cmap = 'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(laplacian, cmap = 'gray'),plt.title('Laplacian')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(sobelx, cmap = 'gray'),plt.title('Sobel X')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(sobely, cmap = 'gray'),plt.title('Sobel Y')
plt.xticks([]), plt.yticks([])
plt.show()