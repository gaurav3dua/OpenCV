import cv2
import numpy as np

img = cv2.imread('lena.jpg')

px = img[200, 100]
print(px)
print(img.item(200,100,2)) #Red = 2 (BGR)

cv2.imshow('image', img)
px = img[200, 100]
print(px)
cv2.waitKey(0)
cv2.destroyAllWindows()