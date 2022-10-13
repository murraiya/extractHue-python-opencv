# -*- coding: utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('C:/Users/suji/Desktop/HOME/imageSignalProcessing/code_space/src/lena.png', cv2.IMREAD_GRAYSCALE)

_min, _max, a, b = cv2.minMaxLoc(img)   
print(_min)
print(_max)

# tmp_img=img.copy().astype(np.float64)
# stretched_img=(((tmp_img-_min)*255)/np.float64(_max-_min)).astype(np.uint8)
equalized_img=cv2.equalizeHist(img)


cv2.imwrite('C:/Users/suji/Desktop/HOME/imageSignalProcessing/equalized_img.png',equalized_img)
hist = cv2.calcHist([equalized_img],[0],None,[256],[0,256])
plt.hist(equalized_img.ravel(), 256, [0,256]); 
plt.show()
