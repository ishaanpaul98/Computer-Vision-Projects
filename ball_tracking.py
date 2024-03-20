import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils

fgbg = cv2.createBackgroundSubtractorMOG2()
feature_params = dict(maxCorners=1,qualityLevel=.6,minDistance=25,blockSize=9)
# Initializing video from training set
video = cv2.VideoCapture('Dataset/Videos/train/game_1/game_1.mp4')

while True:
    # Grabbing a frame from the video
    ret, frame = video.read()

    #Starting a window thread
    cv2.startWindowThread()
    
    #Initializing a mask
    mask = fgbg.apply(frame)
    frame = cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
    ball = cv2.goodFeaturesToTrack(frame,**feature_params)

    if ball is not None:
        x,y = ball[0][0]
        cv2.circle(frame,(int(x),int(y)),8,(180,180,0),2)


    cv2.imshow('game', frame)

    # Waiting for escape key to break from video
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# Releasing video and destroying all windows
video.release()
cv2.destroyAllWindows()
cv2.waitKey(1)
