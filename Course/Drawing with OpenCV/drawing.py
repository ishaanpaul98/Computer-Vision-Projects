import cv2
import numpy as np

#True while mouse button down and false while mouse button up
drawing = False
ix = -1
iy = -1

def drawCircle(event, x, y, flags, param):
    #if event == cv2.EVENT_LBUTTONDOWN:
    #    cv2.circle(img, (x, y), radius=100, color=(0,0,255), thickness=-1)
    #elif event == cv2.EVENT_RBUTTONDOWN:
    #    cv2.circle(img, (x, y), radius=100, color=(0,255,0), thickness=-1)
    pass

def drawRectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img, (ix, iy), (x,y), (0,255,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x,y), (0,255,0), -1)

cv2.namedWindow(winname='drawing')
cv2.setMouseCallback('drawing', drawRectangle)

img = np.zeros((512,512,3), np.int8)

while True:
    cv2.imshow('drawing', img)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows() 