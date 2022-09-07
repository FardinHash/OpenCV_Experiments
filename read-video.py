import cv2

h= 640
w= 480

cap= cv2.VideoCapture('sample video.mp4')

while True:
     success, image= cap.read()
     image = cv2.resize(image, (h, w))

     cv2.imshow('Video', image)
     if cv2.waitKey(1)&0xFF== ord('q'):

         break
