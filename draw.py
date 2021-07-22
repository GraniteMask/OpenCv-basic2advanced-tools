import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #3 for number of color channels
cv.imshow('Blank',blank)

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Cat',img)


# 1) Paint the image of a certain colour

blank[:] = 0,255,0
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green',blank)

# 2) Drawing a rectangle

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=2)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) #to fill the rectangle area
cv.imshow('Rectangle',blank)

# 3) Draw a circle

cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (0,0,250), thickness=3)   #(file,ending point, radius,color,thickness) #if thickness=-1 then we can fill the color of circle

cv.imshow('Circle',blank)

# 4)Draw a line

cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('line',blank)

#5)write text on image

cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)  #(file,text,position,fontname,scale of text,colour,thickness)

cv.imshow('Text',blank)

cv.waitKey(0)