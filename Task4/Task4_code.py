import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('im1.jpg')
img = cv2.imread('mega_space_molly.jpg')
# img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

k = 1

blur = cv2.GaussianBlur(img, (5,5), 0)
mask = cv2.subtract(img,blur)
unsharp_mask = cv2.add(img,k*mask)

cv2.namedWindow('Original')
cv2.imshow('Original',img)
cv2.namedWindow('blur')
cv2.imshow('blur',blur)
cv2.namedWindow('mask')
cv2.imshow('mask',mask)
cv2.namedWindow('unsharp mask')
cv2.imshow('unsharp mask',unsharp_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(321),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(322),plt.imshow(blur),plt.title('blur')
# plt.xticks([]), plt.yticks([])
# plt.subplot(323),plt.imshow(mask),plt.title('mask')
# plt.xticks([]), plt.yticks([])
# plt.subplot(324),plt.imshow(unsharp_mask),plt.title('unsharp_mask')
# plt.xticks([]), plt.yticks([])
# plt.show()