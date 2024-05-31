""" import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("estrella.png")
img2  = cv2.imread("estrella.png",cv2.IMREAD_GRAYSCALE)

ret,thresh = cv2.threshold(img2,240,255,cv2.THRESH_BINARY_INV)
contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
perimeter = cv2.arcLength(cnt,True)
epsilon = 0.05 * perimeter
approx = cv2.approxPolyDP(cnt,epsilon,True)

cv2.drawContours(img,[approx],-1,255,3)
plt.imshow(img)
plt.show()
 """

""" CONVEXHULL """

""" import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("mano.png")
img2  = cv2.imread("mano.png",cv2.IMREAD_GRAYSCALE)

ret,thresh = cv2.threshold(img2,240,255,cv2.THRESH_BINARY_INV)
contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
perimeter = cv2.arcLength(cnt,True)
epsilon = 0.01 * perimeter
approx = cv2.approxPolyDP(cnt,epsilon,True)

hull = cv2.convexHull(approx,False)

cv2.drawContours(img,[hull],-1,255,3)
plt.imshow(img)
plt.show()
 """

""" EJEMPLO CON ENGRANAJE """
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np 
img  = cv2.imread("auto3.jpg")
img2  = cv2.imread("auto3.jpg",cv2.IMREAD_GRAYSCALE)



plt.imshow(img2)
plt.show()
img2 = cv2.erode(img2,(5,5),iterations=60)
img2 = cv2.dilate(img2,(5,5),iterations=50)
plt.imshow(img2)
plt.show()
ret,thresh = cv2.threshold(img2,120,255,cv2.THRESH_BINARY_INV)
#thresh =cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,5)
plt.imshow(thresh)
plt.show()
contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
#cnt = contours[4]q


for i, cnt in enumerate(contours):
    if i !=8:  
        perimeter = cv2.arcLength(cnt, True)
        epsilon = 0.001 * perimeter
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        hull = cv2.convexHull(approx, False)
        if cv2.contourArea(cnt)> 5000 : 
            color = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
            cv2.drawContours(img, [approx], -1,color , 55)
    

plt.imshow(img)
plt.show()
