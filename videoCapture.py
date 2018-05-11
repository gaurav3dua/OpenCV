import numpy as np
import cv2

cap = cv2.VideoCapture(0)
print(cap.get(3), cap.get(4)) #width x height, default 640x480
#cap.set(3, 1280) #probably max value is 1280
#cap.set(4, 720) #probably max value is 720
#print(cap.get(3), cap.get(4))
cap.set(3, 1280)
cap.set(4, 720)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame', gray)
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'Intro to OpenCV- Video Input, Color And Video Analysis With Python',(100,130),font,1,(255,255,255),2)
    cv2.line(frame,(0,150),(1600,150),(185,128,41),10)
    cv2.rectangle(frame,(1100,450),(700,100),(0,255,0),6)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#print(gray)
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()