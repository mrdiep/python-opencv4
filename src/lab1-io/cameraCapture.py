import cv2

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')

# Check if the webcam is opened correctly
if not cameraCapture.isOpened():
    raise IOError("Cannot open webcam")

success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1:
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()
