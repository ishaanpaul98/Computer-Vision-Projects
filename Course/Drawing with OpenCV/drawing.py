import cv2
import numpy as np

def drawCircle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), radius=100, color=(0,0,255), thickness=-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), radius=100, color=(0,255,0), thickness=-1)
cv2.namedWindow(winname='drawing')
cv2.setMouseCallback('drawing', drawCircle)

img = np.zeros((512,512,3), np.int8)

while True:
    cv2.imshow('drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows() 