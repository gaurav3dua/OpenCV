import cv2
import numpy as np
cap = cv2.VideoCapture(0)
print(cap.get(3), cap.get(4)) 
cap.set(3, 1280)
cap.set(4, 720)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = 140
    bw = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('frame', bw)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()