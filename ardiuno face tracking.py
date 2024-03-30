import numpy as np
import serial
import time
import cv2
 
arduino = serial.Serial('/dev/cu.usbmodem1411301', 9600) #連接序列埠
time.sleep(2)
print("Connection to arduino...")
 
 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') #導入臉部辨識訓練素材
 
cap = cv2.VideoCapture(0) #開起攝影機
 
while 1:
    ret, img = cap.read()
    if ret == True:
        cv2.namedWindow("img", cv2.WINDOW_NORMAL)
        cv2.resizeWindow('img', 500, 500) #設定視窗大小
        cv2.line(img, (600, 250), (0, 250), (0, 255, 0), 2) #設定基準線位置 顏色 粗度
        cv2.line(img, (300, 0), (300, 500), (0, 255, 0), 2)
        cv2.circle(img, (300, 250), 10, (255, 255, 255), -1) 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #灰階設定
        faces = face_cascade.detectMultiScale(gray, 1.9 )
  
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 4) #臉部方框設定
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
 
            arr = {y: y+h, x: x+w}
            print(arr)
 
            print('X :' + str(x))
            print('Y :'+str(y))
            print('x+w :' + str(x+w))
            print('y+h :' + str(y+h))
 
            xx = int(x+(x+h))/2 #極限值設定
            yy = int(y+(y+w))/2
 
            print(xx)
            print(yy)
 
            center = (xx, yy) 
 
            print("Center of Rectangle is :", center)
            data = "X{0:d}Y{1:d}Z".format( int(xx), int(yy))
            print(f'output = {data } ')
            arduino.write(data.encode('utf-8')) #將數值傳回ardiuno
 
        cv2.imshow('img', img) #開起視窗
 
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break