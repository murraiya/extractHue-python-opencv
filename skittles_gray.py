import cv2
import numpy as np

skittles = cv2.imread('C:/Users/suji/Desktop/HOME/imageSignalProcessing/images/skittles.jpg')
print(skittles.shape)

gray=cv2.cvtColor(skittles, cv2.COLOR_BGR2GRAY)
# cv2.imshow('skittles color', skittles)
# cv2.imshow('skittles gray', gray)

height, width = gray.shape
output=np.zeros((height, width), np.uint8)
for i in range(0,height,1):
    for j in range(0,width,1):
        if gray[i,j]>=128:
            output[i,j]=255
        else:
            output[i,j]=0

# cv2.imshow('Binarize1', output)


thres_level =128

B=(gray>thres_level)*255
Bimg=cv2.convertScaleAbs(B) #int32->uint8
# cv2.imshow('Binarize2', Bimg)



cv2.waitKey(0)
cv2.destroyAllWindows()