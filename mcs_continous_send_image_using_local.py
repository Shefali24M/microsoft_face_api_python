# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:45:18 2019

@author: SHEFALI MANGAL
"""

import time

import cv2
import numpy as np
import requests
import urllib
import json

subscription_key = 'xxxxxxxxxxxxxxxxxxxxx'
headers  = {'Ocp-Apim-Subscription-Key':subscription_key, "Content-Type": "application/octet-stream" }
params = urllib.parse.urlencode({
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'Age,emotion' })
face_url = "https://faceshef.cognitiveservices.azure.com/face/v1.0/detect?%s" % params


for i in range(2):
    cam=cv2.VideoCapture(0)
    ret,img=cam.read()
    cv2.waitKey(100);
    cv2.imshow("Face",img)
    cv2.imwrite('mcs_dataset/image'+str(i)+'.jpg', img)
    image_path = 'mcs_dataset/image'+str(i)+'.jpg'
    image_data = open(image_path, "rb").read()
    response = requests.post(face_url, headers=headers, data=image_data, params=params)
    print (response.json())
    print("image"+str(i))
    time.sleep(3)

cam.release()
cv2.destroyAllWindows()
