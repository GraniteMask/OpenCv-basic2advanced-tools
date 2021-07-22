import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)  #it reads as BGR image

#plt.imshow(img)  #it reads as RGB image so you will see a inversion of colour
#plt.show()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 1) BGR to HSV (Hue Saturation Value)

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

# 2)BGR to L*a*b
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# 3) BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

cv.waitKey(0)

#always convert BGR to RGB before loading to matplotlib
#if we want to convert from HSV to LAB then we first have to convert it to BGR then that BGR to LAbs