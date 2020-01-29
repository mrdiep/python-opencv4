import cv2

cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('MyWindow')
face_cascade = cv2.CascadeClassifier('src\\cascades\\haarcascade_frontalface_default.xml')

def getFace(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    return frame

# Check if the webcam is opened correctly
if not cameraCapture.isOpened():
    raise IOError("Cannot open webcam")

success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1:
    cv2.imshow('MyWindow', getFace(frame))
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()
