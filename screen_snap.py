import numpy as np
from PIL import ImageGrab
import cv2


def scrn_snap(bbox=(50, 50, 690, 530)):
    capture= np.array(ImageGrab.grab(bbox))
    capture = cv2.cvtColor(capture, cv2.COLOR_RGB2BGR)

    return capture


while True:
    timer= cv2.getTickCount()

    img= scrn_snap()

    fps= cv2.getTickFrequency()/(cv2.getTickCount()-timer)

    cv2.putText(img, 'FPS {}'.format(int(fps)), (75, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (20, 230, 20), 2)

    cv2.imshow('Captured Screen', img)

    cv2.waitKey(1)
