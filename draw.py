import cv2 as cv 
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8') #3 for number of color channels
cv.imshow('Blank',blank)

# img = cv.imread('../photos/big-bang.jpg')
# cv.imshow('Cat',img)


# 1) Paint the image of a certain colour

# blank[:] = 0,255,0
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green',blank)

# 2) Drawing a rectangle

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), thickness=2)
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED) #to fill the rectangle area
cv.imshow('Rectangle',blank)

# 3) Draw a circle

cv.waitKey(0)