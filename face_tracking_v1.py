import cv2
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np
import time
from sys import exit

clasificador_caras  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture("/home/lau/Descargas/test.mp4") # your cam(0 or 1) or the directory of the video,
ws, hs = 1280, 720                                     # for example: /home/USER/Downloads/test.mp4
cap.set(3, ws)
cap.set(4, hs)
detector = FaceDetector()

# connection with arduino
port = "/dev/ttyACM0" # the directory of the port
board = pyfirmata.Arduino(port)
time.sleep(3)
servo_axisX = board.get_pin('d:9:s') #pin 9 Arduino
servo_axisY = board.get_pin('d:10:s') #pin 10 Arduino
servoPos = [90, 90] # initial servo position

if not cap.isOpened():
    print("camera not available, maybe you should check that you have installed all the corresponding camera modules and drivers")
    exit()
else:
    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img, draw=False)
    
        if bboxs:
            #get the coordinate
            fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
            pos = [fx, fy]
            #convert coordinat to servo degree
            servoX = np.interp(fx, [0, ws], [0, 180])
            servoY = np.interp(fy, [0, hs], [0, 180])
    
            if servoX < 0:
                servoX = 0
            elif servoX > 180:
                servoX = 180
            if servoY < 0:
                servoY = 0
            elif servoY > 180:
                servoY = 180
    
            servoPos[0] = servoX
            servoPos[1] = servoY
    
    
            cv2.circle(img, (fx, fy), 120, (0, 0, 255), 2)
            cv2.putText(img, "GENIO DETECTADO", (820, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0,191,255), 3)
                
        else:
            cv2.putText(img, "NO HAY UN GENIO", (820, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0,191,255), 3)
            cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)  # x line
            cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)  # y line
            cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
    
        cv2.putText(img, f'Servo X: {int(servoPos[0])} grados', (900, 630), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 191, 0), 2)
        cv2.putText(img, f'Servo Y: {int(servoPos[1])} grados', (900, 680), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 191, 0), 2)
        cv2.putText(img, 'si desea terminar el seguimiento,',  (50, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 191, 0), 2)
        cv2.putText(img, 'por favor, presione "Q"',  (50, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 191, 0), 2)        
        servo_axisX.write(servoPos[0])
        servo_axisY.write(servoPos[1])
    
        cv2.imshow("Face Tracking", img)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break