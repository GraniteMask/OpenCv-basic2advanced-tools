import cv2 as cv 
import numpy as np

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)  

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 1) Simple Thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)   #(src,thresh,maxval,type)  if pixel>150--->set value as 255. if pixel<150-->set value as 0
cv.imshow('Simple Thresholding', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholding', thresh_inv)

# 2) Adaptive Thresholding (manually specify the threshold value-->in advance cases will not work)

adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3) #(src,maxValue,adaptiveMethod,thresholdType,blocksize,c)
cv.imshow('Adaptive Thresholding', adapt_thresh)

cv.waitKey(0)