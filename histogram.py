import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)  

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

circle = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)


mask = cv.bitwise_and(gray,gray,mask=circle)
cv.imshow('Mask',mask)

# 1) Grayscale Histogram

# gray_hist = cv.calcHist([gray],[0],None,[256],[0,256]) #(image,channels,mask,histsize,range)
gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256]) #(image,channels,mask,histsize,range)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('no. of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# 2) Color Histogram

mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow('Mask',mask)

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('no. of pixels')

colors = ('b','g','r')

for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)