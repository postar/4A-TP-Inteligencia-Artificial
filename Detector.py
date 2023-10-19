import cv2
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
EyesCascade= cv2.CascadeClassifier('haarcascade_eye.xml')
PerfilFace= cv2.CascadeClassifier('haarcascade_profileface.xml')
while True:
    a =1
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    Cara = faceCascade.detectMultiScale(gray, 1.1, 4)
    Ojos = EyesCascade.detectMultiScale(gray, 1.1, 4)
    Caraa = PerfilFace.detectMultiScale(gray, 1.1, 4)
    for (x,y,w,h) in Cara:
        a = 0
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,'Cara',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    if(a==1):
        for (x,y,w,h) in Caraa:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,'Cara',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    for (x,y,w,h) in Ojos:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,'Ojos',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()