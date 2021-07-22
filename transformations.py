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


# 2) Rotation of image
def rotate(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)  #1.0 is scale 
    dimensions = (width,height) 
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,45)  #-ve angle for clockwise rotation
cv.imshow('Rotated',rotated)


cv.waitKey(0)