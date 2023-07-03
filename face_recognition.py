import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input("\n Enter face ID")

count =0

while(True):
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectnagle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        cv.imwrtite("C:\Users/bhopa/OneDrive/Documents/3rd Year/6th sem/UROP/Dataset"+str(face_id) + '.'+ str(count)+ ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image',img)

    k = cv2.waitkey(100) & 0xff

    if k ==27:
        break
    elif count>=30:
        break

print("\n Exiting Program")
cam.release()
cv2.destroyAllWindows()                    
