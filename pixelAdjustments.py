import cv2
import numpy as np

img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

px = img[200, 100]
print(px)
for i in range(50, 150):
	for j in range(0, 512):
		img[j, i+60] = 255
cv2.imshow('image', img)
px = img[200, 100]
print(px)
cv2.waitKey(0)
cv2.destroyAllWindows()