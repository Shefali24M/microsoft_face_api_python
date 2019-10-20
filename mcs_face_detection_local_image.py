# import required module
import requests
import urllib
import json

subscription_key = 'xxxxxxxxxxxxxxxxxxxxx'
# this is the url of server where we will do an api request


# path of your image replace this with location of photo you want to get emotions for
image_path = "C:/Users/SHEFALI MANGAL/Pictures/Camera Roll/five.jpg"


# reading image data from file to python object
image_data = open(image_path, "rb").read()

# header is required in an api request to provide all information about request
headers  = {'Ocp-Apim-Subscription-Key':subscription_key, "Content-Type": "application/octet-stream" }
params = urllib.parse.urlencode({
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'Age,emotion' })
face_recognition_url = "https://faceshef.cognitiveservices.azure.com/face/v1.0/detect?%s" % params
# performing actual api POST method request and waiting for reponse
response = requests.post(face_recognition_url, headers=headers, data=image_data, params=params)
#print (response.json())
p= response.json() 
print(p)
with open('response.txt', 'w') as outfile:
    json.dump(p, outfile)

#s=(p[0]['emotion'])
#print(s) 
#r=(p[1]['faceId'])
#print(r)

with open('response.txt') as json_file:
    m = json.load(json_file)
    for a in m:
        print('faceId: ' + a['faceId'])
        #print('Emotion: '+ a['faceAttributes']['emotion'])
        #print(a['faceAttributes']['emotion'])

#print (list(response))
# you can remove this line if you like but I would suggest you keep it and study about this function from google
#response.raise_for_status()


# this variable will contain all the information in the form of list of json object which can be converted to dict
analysis = response.json()




# other things

# This is not python, it is bash and run on linux terminal. It means make a folder named images
# mkdir -p images
# # similarly curl is bash command and with curl you can make HTTP requests, here we are downloading two pics and keeping them as images/emotion_1.jpg
# curl -Ls https://aka.ms/csnb-emotion-1 -o images/emotion_1.jpg
# curl -Ls https://aka.ms/csnb-emotion-2 -o images/emotion_2.jpg
