import cv2
import matplotlib.pyplot as plt
import numpy

#Blending images
img_1 = cv2.imread('Course\Image Processing\Images\\1.jpg')
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
img_2 = cv2.imread('Course\Image Processing\Images\\2.jpg')
img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
large_img = img_1
small_img = img_2

#Resizing both images to be the same size
print(img_1.shape)
print(img_2.shape)

#img_1 = cv2.resize(img_1, (174, 290))
#img_2 = cv2.resize(img_2, (174, 290))

#blended = cv2.addWeighted(src1=img_1, alpha=0.8, src2=img_2, beta=0.2, gamma=10)
#plt.imshow(blended)
#plt.show()

#Overlay images of different sizes - NO BLENDING 
#Numpy reassignment
x_offset = 0
y_offset = 0
x_end = x_offset + small_img.shape[1]
y_end = y_offset + small_img.shape[0]
large_img[y_offset:y_end, x_offset:x_end] = small_img
plt.imshow(large_img)
plt.show()
#Blend together images of different sizes

#Showing Images
plt.imshow(img_1)
plt.show()
plt.imshow(img_2)
plt.show()