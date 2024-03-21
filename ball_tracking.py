import cv2
import matplotlib.pyplot as plt
import numpy as np
import imutils

def technique1():
    fgbg = cv2.createBackgroundSubtractorMOG2()
    feature_params = dict(maxCorners=1,qualityLevel=.6,minDistance=25,blockSize=9)
    # Initializing video from training set
    video = cv2.VideoCapture('Dataset/Videos/train/game_1/game_1.mp4')

    while True:
        # Grabbing a frame from the video
        ret, frame = video.read()
        original_frame = frame.copy()

        #Starting a window thread
        cv2.startWindowThread()
    
        #Initializing a mask
        mask = fgbg.apply(frame)
        frame = cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))
        ball = cv2.goodFeaturesToTrack(frame,**feature_params)

        if ball is not None:
            x,y = ball[0][0]
            cv2.circle(original_frame,(int(x),int(y)),8,(0,0,255),3)


        cv2.imshow('Technique 1', original_frame)
        # Waiting for escape key to break from video
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    # Releasing video and destroying all windows
    video.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

def technique2():
    video = cv2.VideoCapture('Dataset/Videos/train/game_1/game_1.mp4')
    sensitivity = 50
    lower_white = np.array([0,0,0], dtype=np.uint8)
    upper_white = np.array([0,0,255], dtype=np.uint8)
    while True:
        # Grabbing a frame from the video
        ret, frame = video.read()

        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        width, height = frame.shape[:2]
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_white, upper_white)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        center = None

        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

            # To see the centroid clearly
            if radius > 2:
                print("RADIUS SEEN")
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 0, 255), 5)
                cv2.circle(frame, center, 5, (0,0,255), -1)

        cv2.imshow('Technique 2', frame)
        # Waiting for escape key to break from video
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    # Releasing video and destroying all windows
    video.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def main():
    technique = input("Which technique would you like to use: ")
    if technique == '1':
        technique1()
    elif technique == '2':
        technique2()

if __name__ == "__main__":
    main()
    