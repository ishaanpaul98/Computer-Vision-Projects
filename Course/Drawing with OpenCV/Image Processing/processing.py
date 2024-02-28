import cv2
import matplotlib.pyplot as plt

#Blending images
img_1 = cv2.imread('1.jpg')
print(type(img_1))
img_2 = cv2.imread('2.jpg')

plt.imshow(img_1)
plt.imshow(img_2)
