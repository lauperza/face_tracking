import cv2
from cvzone.FaceDetectionModule import FaceDetector
import pyfirmata
import numpy as np
import time
from sys import exit
# Configuración de perifericos de OpenCV
clasificador_caras  = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # Asignación de objeto a detectar.
cap = cv2.VideoCapture(0) # Tu cam(0 or 1) o el directorio del video, por ejemplo: /home/USER/Downloads/test.mp4
ws, hs = 1280, 720                                    
cap.set(3, ws)
cap.set(4, hs)
detector = FaceDetector()

# Conexión con Arduino
port = "/dev/ttyACM0" # El directorio del puerto(linux), en caso de que su S.O. sea Windows, sera suficiente con poner tty0, o su puerto correspondiente.
board = pyfirmata.Arduino(port)
time.sleep(3)
servo_axisX = board.get_pin('d:9:s') # Pin 9 Arduino
servo_axisY = board.get_pin('d:10:s') # Pin 10 Arduino
servo_pos = [90, 90] # Posicion inicial de los servos
# En caso de no encontrar la cámara, no se ingresara al ciclo while y se terminara el programa.
if not cap.isOpened():
    print("La cámara no está disponible, tal vez deberías verificar que hayas instalado todos los módulos y controladores de cámara correspondientes.")
    exit()
else:    
    while True:    # Ciclo infinito en el que se analiza cada imagen por separado.
        success, img = cap.read()
        img, bboxs = detector.findFaces(img, draw=False)
        # En caso de encontrar un rostro en la pantalla, se cumplira la condición.
        if bboxs:
            fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
            pos = [fx, fy]
            # Calculo de coordenadas del rostro.
            servoX = np.interp(fx, [0, ws], [0, 180])
            servoY = np.interp(fy, [0, hs], [0, 180])
            # Limitación de movimiento a 180°
            if servoX < 0:
                servoX = 0
            elif servoX > 180:
                servoX = 180
            if servoY < 0:
                servoY = 0
            elif servoY > 180:
                servoY = 180
            # Asignación de valores a los servomotores.
            servo_pos[0] = servoX
            servo_pos[1] = servoY
    
            # Impresion de información en la pantalla.
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
        # En caso de querer verificar los valores de movimiento.
        #servo_axisX.write(servo_pos[0])
        #servo_axisY.write(servo_pos[1])
    
        cv2.imshow("Face Tracking", img)
        if cv2.waitKey(1) == ord('q'):    # condicion que se cumplira cuando el usuario presione "q", y se finalizara el programa.
            cv2.destroyAllWindows()
            break
