import cv2
import numpy as np
import imutils
import os
import time

Datos = 'n'
if not os.path.exists(Datos):
    print('Carpeta creada: ',Datos)
    os.makedirs(Datos)
cam = cv2.VideoCapture(0)
x1, y1 = 190, 80
x2, y2 = 450, 398
time.sleep(1)


count = 0
while True:
    ret, frame = cam.read() 
    if ret == False: break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    
    
    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto,width=38)

    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
        print('Imagen guardada:'+'/objeto_{}.jpg'.format(count))
        count = count +1
    if k == 27:
        break


    cv2.imshow('webcam',frame)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
