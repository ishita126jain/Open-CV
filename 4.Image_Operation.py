import cv2
import numpy as np

img = cv2.imread('photos/watch.jpg', cv2.IMREAD_COLOR)

px = img[55,55]
print(px) #Here we prints the color of specific pixel 

# We can even chnage the color of particular pixel
img[55,55] = [255,255,255]
px = img[55,55]
print(px)

#ROI Region of Image
roi = img[100:150, 100:150]
print(roi)

#Change color of some roi
img[100:150, 100:150] = [255,255,255]

#Copy and paste the roi
part = img[37:111, 107:194]  # 111-37 = 74 and 194-107 = 87
img[0:74, 0:87] =part

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()