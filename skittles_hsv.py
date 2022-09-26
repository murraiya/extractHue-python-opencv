import cv2
import numpy as np
import matplotlib.pyplot as plt

skittles = cv2.imread('C:/Users/suji/Desktop/HOME/imageSignalProcessing/images/skittles.jpg')

src = cv2.imread('./data/lena.jpg')
cv2.imshow('src', src)

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

v2 = cv2.equalizeHist(v)
hsv2 = cv2.merge([h, s, v2])
dst = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)
cv2.imshow('dst', dst)

cv2.waitKey(1)
cv2.destroyAllWindows()