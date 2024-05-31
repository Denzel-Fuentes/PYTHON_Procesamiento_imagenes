import numpy as np
import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("ruido.jpg",cv2.IMREAD_GRAYSCALE)

img = cv2.medianBlur(img,5)

plt.imshow(img)
plt.show()

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(th1)
plt.show()

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,5)
plt.imshow(th2,cmap="gray") 
plt.show()

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)
plt.imshow(th3,cmap="gray") 
plt.show()

