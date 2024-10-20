
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)

blur = cv2.blur(img, (5,5))