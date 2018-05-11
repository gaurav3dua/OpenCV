#Uses python3

import numpy as np
import cv2

img = cv2.imread('lena.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()
elif k == ord('s'):
	cv2.imwrite('lenaGray.jpg', img)
	cv2.destroyAllWindows()