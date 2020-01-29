#importing opencv
import cv2
#Reading the image from local disk
img = cv2.imread("src\\images\\chess.jpg", cv2.IMREAD_GRAYSCALE)
#displaying the original image
cv2.imshow("original image",img)

#Resizing image to small size
#img = cv2.resize(img,(420,300))

#applying algorithm to blur the image
img = cv2.blur(img, ksize = (10, 10))

#convert write image to file
cv2.imwrite('MyPic.jpg', img)
#displaying the blur image
cv2.imshow("blur image",img)

cv2.waitKey(0)