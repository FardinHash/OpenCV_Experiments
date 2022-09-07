import cv2

h= 640
w= 480

cap= cv2.VideoCapture(0)
cap.set(3, h)
cap.set(4, w)
cap.set(10, 150)

while True:
     success, image= cap.read()
     image = cv2.resize(image, (h, w))

     cv2.imshow('Video', image)
     if cv2.waitKey(1)&0xFF== ord('q'):

         break
