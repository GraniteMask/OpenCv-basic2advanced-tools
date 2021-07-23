import cv2 as cv 
import numpy as np

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)  

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 1) Laplacian

lap = cv.Laplacian(gray,cv.CV_64F) #(src, data depth)
lap = np.uint8(np.absolute(lap)) #absolute is used so that even if there is any negative value computed it will be converted into a +ve value
cv.imshow('Laplacian', lap)

# 2) Sobel

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0) #(src,data depth, x direction, y direction)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1) #(src,data depth, x direction, y direction)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

cv.waitKey(0)