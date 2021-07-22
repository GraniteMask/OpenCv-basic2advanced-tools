import cv2 as cv 

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)

# 1) Converting a image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2) Blur an image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)     #(3,3) is color size and must be an odd number
cv.imshow('Blur',blur)

cv.waitKey(0)