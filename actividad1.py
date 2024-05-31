import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img  = cv.imread("actividad1.png")
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_, thresholded = cv.threshold(img, 200, 255, cv.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
dilatado = cv.dilate(thresholded, kernel, iterations=2)
erocionado = cv.erode(dilatado, kernel, iterations=2)
contours, _ = cv.findContours(erocionado, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

output = img.copy()
cv.drawContours(output, contours, -1, (255, 0, 0), 2)

plt.figure(figsize=(12, 12))
plt.imshow(img, cmap='gray')
plt.show()
plt.figure(figsize=(12, 12))
plt.imshow(erocionado, cmap='gray')
plt.show()
plt.figure(figsize=(12, 12))
plt.imshow(output, cmap='gray')
plt.show()
