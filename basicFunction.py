import cv2 as cv 

img = cv.imread('../photos/big-bang.jpg')
cv.imshow('Bang',img)

# 1) Converting a image to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# 2) Blur an image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)     #(3,3) is color size and must be an odd number
cv.imshow('Blur',blur)

# 3) Edge Cascade
# canny = cv.Canny(img,125,175)
canny = cv.Canny(blur,125,175) #this will decrease the edge number
cv.imshow('Edge',canny)

# 4) Dilating the image
dilated = cv.dilate(canny,(3,3), iterations=1)  #(3,3) is kernel size
cv.imshow('Dilated',dilated)

# 5) Eroding an Image
eroded = cv.erode(dilated, (3,3), iterations=1)   #dilate will increase the thickness and size of edges and erode will decrease the thickness
cv.imshow('Eroded',eroded)

# 6) Resize an Image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)  #INTER_AREA--useful if you are shrinking the image to smaller size that of the original image. INTER_LINEAR and INTER_CUBIC is used when image is scaled to bigger size. INTER_CUBIC is smallest among all but gives higher quality image
cv.imshow('Resize',resized)

# 7) Cropping an image
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)