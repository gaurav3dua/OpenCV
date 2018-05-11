import urllib
import cv2
import numpy as np
import urllib.request, urllib.parse, urllib.error
import time

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://10.140.244.162:8080/shot.jpg'

while True:

    # Use urllib to get the image and convert into a cv2 usable format
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = 127
    img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

    # put the image on screen
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    #time.sleep(0.1) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break