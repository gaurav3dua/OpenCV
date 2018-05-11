import cv2
import numpy as np
img = cv2.imread('lena.jpg', cv2.IMREAD_GRAYSCALE)

thresh = 127
im_bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('image', im_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()