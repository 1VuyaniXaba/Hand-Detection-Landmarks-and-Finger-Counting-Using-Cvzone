import cv2
from cvzone.HandTrackingModule import HandDetector
import time

#setting up PC camera (with and height)
print(f"Capturing CAM: {time.localtime()[0:5]}")  
#extracts the year,month,hour, minutes, seconds to keep track of when the 
#The program began 
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

#calling the hand detector 
detector = HandDetector(staticMode=False, maxHands=2, detectionCon=0.5)

while True:
    success, frame = camera.read()
    #check if the camera capture was succesful or not
    if not success:
        print("Camera capture FAILED")
    else:
        print("Camera Captured")
    #camera flip
    frame = cv2.flip(frame,1)
    #appliying the model on the stream frames
    hand, frame = detector.findHands(img=frame, draw=True)  #True Shows B-Box and joint points
    if hand:
        lmList = hand[0]["lmList"] #21 hand landmarks
        fingers_up = sum(detector.fingersUp(hand[0]))  #counts the sum of the fingers up
        cv2.putText(frame, f"Fingers Up: {fingers_up}",(20,20),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=1,
                    color=(255,0,0)) #cv2.putTesxt write a text on the frame
        print("hand recognised")
    cv2.imshow("Hand Detector", frame)  #cv2.imshow() show the stream on a new seperate window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   #checks the key every 1ms, if q is pressed the loop breaks
cv2.destroyAllWindows()
camera.release()
