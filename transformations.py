import cv2 as cv 
import numpy as np

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)

# 1) Translation

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -->Left translate
#  x -->Right translate
# -y -->Up translate
#  y -->Down translate

translated = translate(img, 100,100)
cv.imshow('Translated',translated)
cv.waitKey(0)