import cv2  #import library

#set height and width
h= 640
w= 480

cap= cv2.VideoCapture('sample video.mp4')  #load the video

while True:
     success, image= cap.read()
     image = cv2.resize(image, (h, w))  #resize with height and width

     cv2.imshow('Video', image)  #show the video
     
     if cv2.waitKey(1)&0xFF== ord('q'):  #escape!

         break
