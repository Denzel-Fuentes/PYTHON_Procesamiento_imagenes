import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("estrella2.jpg")
img2  = cv2.imread("estrella2.jpg",cv2.IMREAD_GRAYSCALE)

ret,thresh = cv2.threshold(img2,240,255,cv2.THRESH_BINARY_INV)
contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
perimeter = cv2.arcLength(cnt,True)
epsilon = 0.05 * perimeter
approx = cv2.approxPolyDP(cnt,epsilon,True)

cv2.drawContours(img,[approx],-1,255,3)
plt.imshow(img)
plt.show()
