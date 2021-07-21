import cv2 as cv

#img = cv.imread('photos/big-bang.jpg') #for reading images

#cv.imshow('Bang', img)

#Reading Videos
#capture = cv.VideoCapture(0) #here 0 refers to webcam and number can be increased if more number of webscams is attached to system and you want to choose specific cam
capture = cv.VideoCapture('')

cv.waitKey(0)