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
#plt.show()

#Masking
img_1 = cv2.imread('Course\Image Processing\Images\\1.jpg')
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
img_3 = cv2.imread('Course\Image Processing\Images\\3.jpg')
img_3 = cv2.cvtColor(img_3, cv2.COLOR_BGR2RGB)
img_3 = cv2.resize(img_3, (174, 290))
print(img_3.shape)
x_offset =  img_1.shape[1] - img_3.shape[1]
y_offset =  img_1.shape[0] - img_3.shape[0]
rows, columns, channels = img_3.shape
roi = img_1[y_offset:img_1.shape[0], x_offset:img_1.shape[1]]
print(roi.shape)
img_3Gray = cv2.cvtColor(img_3, cv2.COLOR_RGB2GRAY)
mask_inv = cv2.bitwise_not(img_3Gray)
white_background = numpy.full(img_3.shape, 255, dtype=numpy.uint8)
bk = cv2.bitwise_or(white_background, white_background, mask=mask_inv)
fg = cv2.bitwise_or(img_3, img_3, mask=mask_inv)
final_roi = cv2.bitwise_or(roi, fg)
large_img = img_1
small_img = final_roi
large_img[y_offset:y_offset+small_img.shape[0], x_offset+small_img.shape[1]] = small_img
plt.imshow(large_img)
plt.show()

#Showing Images
plt.imshow(img_1)
#plt.show()
plt.imshow(img_2)
#plt.show()