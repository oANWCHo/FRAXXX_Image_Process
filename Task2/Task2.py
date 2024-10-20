import cv2

img = cv2.imread('what.jpg',0)


img2 = cv2.convertScaleAbs(img, alpha=-10, beta=10)  
# adjust contrast to 10 and brightness to 50

cv2.namedWindow('before')
cv2.imshow('before',img)
cv2.namedWindow('after')
cv2.imshow('after',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()