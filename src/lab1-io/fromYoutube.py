import pafy
import cv2

url = 'https://www.youtube.com/watch?v=cXCPS0o-nq4'
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="webm")

#start the video
cap = cv2.VideoCapture(play.url)
while (True):
    ret,frame = cap.read()
    """
    your code here
    """
    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break    

cap.release()
cv2.destroyAllWindows()