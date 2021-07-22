#Boundary of objects
#contours !=edges"
import cv2 as cv 
import numpy as np

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


canny = cv.Canny(img,125,125) #this will decrease the edge number
cv.imshow('Canny Edge',canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)   #RETR_EXTERNAL resturns only external contours
#RETR_TREE returns all contours with hierarchical systems
#RETR_EXTERNAL returns all contours
#CHAIN_APPROX_NONE returns all the points on the contour
#CHAIN_APPROX_SIMPLE returns all the points on the contour in simple ones to make more sense

#ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
#cv.imshow('Thresh',thresh)

print(f'{len(contours)} contours found!')

cv.waitKey(0)

#bluring the image will reduce the number of contour points