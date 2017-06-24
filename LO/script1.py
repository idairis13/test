import cv2

img = cv2.imread("LO/galaxy.jpg",0) #adding LO/ changed the type from NONE to numpy.ndarray (don't know why)

print(type(img))
print(img)
#print(img.shape)
#print(img.ndim)

#resized_image = cv2.resize(img,(1000,500))
#cv2.imshow("Galaxy",img)
#cv2.waitKey()
#cv2.destroyAllWindows()
#print (cv2.__version__)



#THIS IS ON THE BRANCH 'Mybranch'
