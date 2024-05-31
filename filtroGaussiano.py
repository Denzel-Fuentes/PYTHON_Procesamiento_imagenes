"""Created on Fri Apr 12 14:36:58 2024 @author: Lenovo"""

import numpy as np 
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("imagen.jpeg")

kernels = [(3,3),(9,9),(15,15)]


#for (KX,KY) in  kernels:
#    blurred = cv2.blur(img, (KX,KY))
#    cv2.imshow("Res ( {} , {} ) ".format(KX,KY),blurred)
#    cv2.waitKey()
#cv2.destroyAllWindows()

"""
for (kX, kY) in kernels:
    
    GaussianBlurred = cv2.GaussianBlur(img, (kX, kY), 0)
    cv2.imshow("Res ({}, {})".format(kX,kY),GaussianBlurred)
    cv2.waitKey()
cv2.destroyAllWindows()
"""

gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gris, (21,21), 0)
cv2.imshow("Blurred", blurred)
(T2,threshInv2) = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("iamgen binaria invertida",threshInv2)
img2 = img.copy()

blurred2 = cv2.GaussianBlur(img, (21,21), 0)
mascara = cv2.bitwise_and(img,img,mask=threshInv2)
fil,col,_ = img.shape
for i in range(fil):
    for j in range(col):
        if mascara[i,j].any():
            img[i,j] = blurred2[i,j]
    
cv2.imshow("imagen_original",img2)
cv2.imshow("mascara",img)


for(K) in (3,9,15):
    median = cv2.medianBlur(img,K)
    cv2.imshow("Median {}".format(K),median)
    cv2.waitKey()


gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(img, (15,15), 0)
cv2.imshow("Blurred", blurred)

(T,threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("iamgen binaria",threshInv)

(T2,threshInv2) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("iamgen binaria invertida",threshInv2)

mascara = cv2.bitwise_and(img,img,mask=threshInv2)
cv2.imshow("mascara",mascara)

cv2.waitKey()
cv2.destroyAllWindows()



