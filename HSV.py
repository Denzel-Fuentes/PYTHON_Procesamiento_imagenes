import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
 
img = cv.imread("imagen10.jpg")
img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
img3 = cv.cvtColor(img,cv.COLOR_BGR2HSV)
 
plt.imshow(img)
plt.show()
plt.imshow(img2)
plt.show()
plt.imshow(img3)
plt.show()
#mascaras con colores basicos
#HSV
# (color , saturacion (blanco) , valor (negro) )
#azul 
lower = np.array([76, 58, 228])
upper = np.array([100, 255, 0])
mask_blue = cv.inRange(img3,lower,upper)
#rojo 
lower1 = np.array([0,50,50])
upper1 = np.array([15,255,255])
mask_red = cv.inRange(img3,lower1,upper1)
#amarillo 
lower2 = np.array([20,50,50])
upper2 = np.array([35,255,255])
mask_yellow = cv.inRange(img3,lower2,upper2)

#Aplicamos las mascaras por ende desapareceran las figuras geometricas 
res_red = cv.bitwise_and(img2, img2,mask=mask_red)
res_blue = cv.bitwise_and(img2, img2 ,mask=mask_blue)
res_yellow = cv.bitwise_and(img2, img2,mask=mask_yellow)

plt.imshow(res_red)
plt.show()

plt.imshow(res_yellow)
plt.show()

plt.imshow(res_blue)
plt.show()