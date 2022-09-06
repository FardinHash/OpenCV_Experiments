import cv2  #import library

image= cv2.imread('images/images1.jpg')  #load the image to read

cv2.imshow('Hello AI', image)  #show the image

cv2.waitKey(0)
