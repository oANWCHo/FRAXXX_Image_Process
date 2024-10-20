import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1) # position , radius , BGR 

img = np.zeros((512,512,3), np.uint8) # create a black image, a window and bind function to window
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle) # call function

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()