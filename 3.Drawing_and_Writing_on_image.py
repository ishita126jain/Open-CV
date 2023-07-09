import numpy as np
import cv2

#Drawing Line
img = cv2.imread('photos/watch.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (150,150), (0,0,255), 15)
cv2.imshow('image1', img)

#Drawing Rectangle
img = cv2.imread('photos/watch.jpg', cv2.IMREAD_COLOR)
cv2.rectangle(img, (15,25), (200,150),(0,255,0), 5)
cv2.imshow('image2', img)

#Drawing Circle
img = cv2.imread('photos/watch.jpg', cv2.IMREAD_COLOR)
cv2.circle(img,(100,63), 55, (255,0,0), -1) # -1 represent the filling of circle
cv2.imshow('image3', img)

#Drawing Polygon
img = cv2.imread('photos/watch.jpg', cv2.IMREAD_COLOR)
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 3)
cv2.imshow('image4', img)

#Writing on Image
img = cv2.imread('photos/watch.jpg', cv2.IMREAD_COLOR)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV !',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)
cv2.imshow('image5', img)


cv2.waitKey(0)
cv2.destroyAllWindows()