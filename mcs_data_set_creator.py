# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 22:43:13 2019

@author: SHEFALI MANGAL
"""

import cv2
import numpy as np
import requests
import urllib
import json

subscription_key = 'xxxxxxxxxxxxxxxxxxxxx'


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
id= input('enter user id: ')
sampleNum=0;
#while(True):
ret,img=cam.read();
    #gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=faceDetect.detectMultiScale(img);
for(x,y,w,h) in faces:
    sampleNum=sampleNum+1;
    cv2.imwrite("mcs_dataset/user."+str(id)+"."+str(sampleNum)+".jpg",img)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,60),3)
    cv2.waitKey(100);
    cv2.imshow("Face",img);
    image_path = "mcs_dataset/user."+str(id)+"."+str(sampleNum)+".jpg"
    image_data = open(image_path, "rb").read()
    headers  = {'Ocp-Apim-Subscription-Key':subscription_key, "Content-Type": "application/octet-stream" }
    params = urllib.parse.urlencode({
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'Age,emotion' })
    face_recognition_url = "https://faceshef.cognitiveservices.azure.com/face/v1.0/detect?%s" % params
    response = requests.post(face_recognition_url, headers=headers, data=image_data, params=params)
    print (response.json())
    cv2.waitKey(1000);
    if(sampleNum>10):
        break
cam.release()
cv2.destroyAllWindows()
                           
