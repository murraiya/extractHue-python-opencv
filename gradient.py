# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/suji/Desktop/HOME/imageSignalProcessing/code_space/src/chessboard_gray.jpg', cv2.IMREAD_GRAYSCALE)

tmp_img=img.copy().astype(np.float64) 

kernel1 = np.array([[-1, 0, 1],
                          [-2, 0, 2],
                          [-1, 0, 1]])
kernel2 = (1/25)*np.array([[2, 2, 2],
                           [2, 2, 2],
                           [2, 2, 2]])

sobelFiltered = cv2.filter2D(tmp_img, -1, kernel1) 
gradAfterBlur = cv2.filter2D(tmp_img, -1, kernel1*kernel2) 


_sobelFiltered=abs(sobelFiltered).astype(np.uint8)
_gradAfterBlur=abs(gradAfterBlur).astype(np.uint8)
_sobelFiltered=abs(sobelFiltered).astype(np.uint8)

avg=cv2.mean(_gradAfterBlur)
print(avg)

high_edges=cv2.subtract(_gradAfterBlur, avg).astype(np.uint8)
#gradient magnitude가 많이 큰 애들만 남는다.
#변화량이 큰 애들만 남는다.



cv2.imwrite('C:/Users/suji/Desktop/HOME/imageSignalProcessing/a.png',high_edges)

cv2.imwrite('C:/Users/suji/Desktop/HOME/imageSignalProcessing/b.png',_gradAfterBlur)

cv2.imwrite('C:/Users/suji/Desktop/HOME/imageSignalProcessing/c.png',_sobelFiltered)

cv2.imshow('subtract',high_edges)
cv2.imshow('sobelFiltered',_sobelFiltered)
cv2.imshow('gradAfterBlur',_gradAfterBlur)
cv2.waitKey(0)









# cv2.imshow('src', img.astype(np.uint8))
# cv2.imshow('enhanced', filtered.astype(np.uint8))


# cv2.waitKey(0) # wait key until key pressed
# cv2.destroyAllWindows()

