import numpy as np
import cv2

img = cv2.imread('fibo building.jpg',1) #set to grayscale    
cv2.imshow('image',img) #show image
k = cv2.waitKey(0)
if k==27: #ESC
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('fibo building.png',img) #save
    cv2.destroyAllWindows()