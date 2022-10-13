import cv2

image= 'images/image2.jpg'
img= cv2.imread(image)
print(img.shape)

width, height= 1000, 1000
Resize= cv2.resize(img,(width, height))
print(Resize.shape)

Cropped= img[300:540,430:480]
Cropped_Resize= cv2.resize(Cropped,(img.shape[1],img.shape[0]))

cv2.imshow('Output', img)

cv2.imshow('Cropped Image: ',Cropped)

cv2.imshow('Resized Image: ',Resize)

cv2.imshow('Resized with cropped: ', Cropped_Resize)

cv2.waitKey(0)
