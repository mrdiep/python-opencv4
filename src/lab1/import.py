#importing opencv
import cv2
#Reading the image from local disk
img = cv2.imread("d:/out.png")
#Resizing image to small size
img = cv2.resize(img,(420,300))
#displaying the original image
cv2.imshow("original image",img)
#applying algorithm to blur the image
img = cv2.blur(img, ksize = (5, 5))
#displaying the blur image
cv2.imshow("blur image",img)
cv2.waitKey(0)