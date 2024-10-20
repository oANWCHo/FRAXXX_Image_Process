import cv2
import numpy as np
from matplotlib import pyplot as plt

def imreconstruct(img, marker):
    mask = img
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    recon1 = marker
    recon1_old = np.zeros(recon1.shape,np.int8)
    while np.sum(np.sum(recon1 - recon1_old)) != 0 :
        recon1_old = recon1
        recon1 = cv2.dilate(recon1, se)
        recon1 = recon1 & mask
    return recon1

def marking_O(img):
    imgc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(imgc.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    single_level_holes = np.zeros_like(imgc)
    multiple_level_holes = np.zeros_like(imgc)
    for idx in range(len(hierarchy[0])):
        if hierarchy[0][idx][3] != -1:
            cv2.drawContours(single_level_holes, contours, idx, (255, 255, 255), cv2.FILLED, 8, hierarchy)

    imgn = cv2.bitwise_not(imgc)
    img_o = cv2.bitwise_and(imgn, single_level_holes)
    return img_o

# read image
img1 = cv2.imread('text_frombook.png')

# Find a tall and delete it out
se = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 51))
img_er = cv2.erode(img1, se)
img_recon = imreconstruct(img1,img_er)
img_subst = cv2.subtract(img1,img_recon)

# Make letter connect
kernel = np.ones((3,3), np.uint8)
kernel2 = np.ones((2,2), np.uint8)
img_subst = cv2.dilate(img_subst, kernel2, iterations=6)  
img_subst = cv2.erode(img_subst,kernel2, iterations=1)

# Find "o" in image
img_markO = marking_O(img_subst)

# process and deconstruct
img_markO_er = cv2.erode(img_markO,kernel2, iterations=9)
img_markO_dil = cv2.dilate(img_markO_er, kernel, iterations=11)
img_markO_color = cv2.cvtColor(img_markO_dil, cv2.COLOR_GRAY2BGR)
img_O = imreconstruct(img1,img_markO_color)

# split image into two
img_O_top = img_O[0:0+640, 0:0+3000]
img_O_bot = img_O[640:640+1000 , 0:0+3000]

# Find "o" in image on top zone
img_markO_top = marking_O(img_O_top)
img_markO_top_er = cv2.erode(img_markO_top,kernel, iterations=8)
img_markO_top_dil = cv2.dilate(img_markO_top_er, kernel, iterations=8)
img_markO_top_color = cv2.cvtColor(img_markO_top_dil, cv2.COLOR_GRAY2BGR)
img_O_top_2 = imreconstruct(img_O_top,img_markO_top_color)

# Combine image
img_fin = cv2.vconcat([img_O_top_2, img_O_bot]) 

# Plotting result
plt.subplot(321),plt.imshow(img1),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(img_subst),plt.title('substract tall out')
plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(img_markO),plt.title('Finding O')
plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(img_O),plt.title('Get O but didnt want another')
plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(img_O_top_2),plt.title('split top and bottom and finding O')
plt.xticks([]), plt.yticks([])
plt.subplot(326),plt.imshow(img_fin),plt.title('combine top and bottom')
plt.xticks([]), plt.yticks([])
plt.show()

