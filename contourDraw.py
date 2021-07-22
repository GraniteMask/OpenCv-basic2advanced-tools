#Boundary of objects
#contours !=edges"
import cv2 as cv 
import numpy as np

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)

blank=np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank',blank)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(blank, contours, -1, (0,0,255), 2)  #-1 for all the contours we want , then color, then thickness
cv.imshow('Contours Drawn',blank)

print(f'{len(contours)} contours found!')

cv.waitKey(0)

#bluring the image will reduce the number of contour points

#always try to do canny then contour counting rather than doing thresholding first