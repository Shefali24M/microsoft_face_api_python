import cv2
import numpy as np
import requests
import urllib
import json
import time



cam=cv2.VideoCapture(0);
#for i in range(10):
for i in range(5):
    ret,img=cam.read()
    
    cv2.imwrite('mcs_dataset/image.jpg', img)
    cv2.imshow("Face",img)
    print(i)
    time.sleep(2)
 

#subscription_key = 'xxxxxxxxxxxxxxxxxx'
#image_path = "mcs_dataset/image.jpg"
#image_data = open(image_path, "rb").read()
#headers  = {'Ocp-Apim-Subscription-Key':subscription_key, "Content-Type": "application/octet-stream" }
#params = urllib.parse.urlencode({
#        'returnFaceId': 'true',
#        'returnFaceLandmarks': 'false',
#        'returnFaceAttributes': 'Age,emotion' })
#face_url = "https://faceshef.cognitiveservices.azure.com/face/v1.0/detect?%s" % params
#response = requests.post(face_url, headers=headers, data=image_data, params=params)
#print (response.json())
del(cam) 
  
      


