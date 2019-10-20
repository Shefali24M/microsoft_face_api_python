import requests
import json

subscription_key = 'xxxxxxxxxxxxxxxxxxxxx'
assert subscription_key



face_api_url = 'https://faceshef.cognitiveservices.azure.com/face/v1.0/detect'
image_url ='https://upload.wikimedia.org/wikipedia/commons/b/b6/Deepika_Padukone_Cannes_2018_%28cropped%29.jpg'
#image_url = "C:\Users\SHEFALI MANGAL\Desktop\IMG-20170901-WA0014"
#with open(image_url, 'rb') as f:
    #img_data = f.read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params, json={"url": image_url},
                         headers=headers)
print (response.json())
#print(json.dumps(response.json()))
#print(response)