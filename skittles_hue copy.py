import cv2
import numpy as np
import matplotlib.pyplot as plt

graph = cv2.imread('C:/Users/suji/Desktop/HOME/blue.jpg')
# print(skittles.shape)
cv2.imshow('bgr_image', graph)

h,s,v=cv2.split(cv2.cvtColor(graph, cv2.COLOR_BGR2HSV))
# cv2.imshow('h', h)

height, width = h.shape
output=np.zeros((height, width), np.uint8)
for i in range(0,height,1):
    for j in range(0,width,1):
        if h[i,j]>=110 and h[i,j]<=120:
            output[i,j]=255
        else:
            output[i,j]=0

cv2.imshow('getting_blue', output)

# h_=(h>45 and h<75)*255
# h_green=cv2.convertScaleAbs(h_) #int32->uint8
# cv2.imshow('h_green', h_green)
# hist=cv2.calcHist([h], [0],None,[256],[0,256])
    
# plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()