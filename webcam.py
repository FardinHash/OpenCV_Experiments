import cv2  #import library 

#set height and width
h= 640
w= 480

cap= cv2.VideoCapture(0)  #access the webcam

cap.set(3, h)
cap.set(4, w)
cap.set(10, 150)

while True:
     success, image= cap.read()
     image = cv2.resize(image, (h, w))  #resize with height and width

     cv2.imshow('Video', image)  #show the output
     
     if cv2.waitKey(1)&0xFF== ord('q'):  #escape!

         break
