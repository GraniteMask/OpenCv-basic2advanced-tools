import cv2 as cv

# img = cv.imread('../photos/big-bang.jpg')
# cv.imshow('Bang', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture(0) #here 0 refers to webcam and number can be increased if more number of webscams is attached to system and you want to choose specific cam
capture = cv.VideoCapture('../videos/sample.mp4')

while True:
    isTrue, frame = capture.read() #reading video frame by frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video',frame) 
    cv.imshow('Video resized',frame_resized) 

    if cv.waitKey(20) & 0xFF==ord('d'):   #if letter d is press then break out of while loop
        break

capture.release()
cv.destroyWindow()