import cv2 as cv 
import numpy as np

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)  

#Averaging
average= cv.blur(img,(3,3))
cv.imshow("Average Show", average)

#Gaussian Blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)  #more natural blur than averaging

#Median Blur
median cv.medianBlur(img,3)

#Bilateral Blue (most effective blur)
bilateral = cv.bilateralFilter(img, 5,15, 15)  #(img,diameter,sigmacolor,sigmaspace[determine the distance of pixel effecting the computation of a particular pixel])

cv.waitKey(0)