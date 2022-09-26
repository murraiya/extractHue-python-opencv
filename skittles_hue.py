import cv2
import numpy as np
import matplotlib.pyplot as plt

skittles = cv2.imread('C:/Users/suji/Desktop/HOME/imageSignalProcessing/images/skittles.jpg')
print(skittles.shape)

# b,g,r=cv2.split(skittles)
# cv2.imshow('b', b)
# cv2.imshow('g', g)
# cv2.imshow('r', r)

h,s,v=cv2.split(cv2.cvtColor(skittles, cv2.COLOR_BGR2HSV))
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)

hist=cv2.calcHist([h], [0],None,[256],[0,256])
    
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()