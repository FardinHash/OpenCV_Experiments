#import libraries
import cv2
import numpy as np

img= np.zeros((512, 512, 3), np.uint8)

print(img)  #fresh image

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 2)  #draw line

cv2.rectangle(img, (350, 100), (450, 200), (0, 0, 255), cv2.FILLED)  #rectangle

cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)  #circle

cv2.putText(img, 'Shapes', (75, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 1)  #text

cv2.imshow('Output', img)  #output

cv2.waitKey(0)
