import cv2
import numpy as np

kernel= np.ones((5,5),np.uint8)
print(kernel)

image= 'images/image2.jpg'
img= cv2.imread(image)

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur= cv2.GaussianBlur(imgGray,(7,7),0)

imgCanny= cv2.Canny(imgBlur,100,200)

imgDilation= cv2.dilate(imgCanny, kernel , iterations= 10)

imgEroded= cv2.erode(imgDilation, kernel, iterations= 2)

cv2.imshow('Output',img)

cv2.imshow('GrayScale Image: ',imgGray)
cv2.imshow('Blur Image: ',imgBlur)
cv2.imshow('Edge image: ',imgCanny)
cv2.imshow('Dialation: ',imgDilation)
cv2.imshow('Eroded Image: ',imgEroded)

cv2.waitKey(0)
