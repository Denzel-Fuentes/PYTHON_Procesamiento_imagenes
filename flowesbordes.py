import cv2
import numpy as np
import matplotlib.pyplot as plt
img  = cv2.imread("descarga3.jpg")
img2 = img.copy()
kernel = np.ones((5,5),np.uint8)
fil,col,_ = img.shape
imgGris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgGris = cv2.dilate(imgGris,kernel,iterations=10)
for i in range(fil):
    for j in range(col):
        if img[i,j,2] > 200 and  img[i,j,0] > 180 and img[i,j,1] > 180:
            img[i,j,:] = 0 
        else:
            img[i,j,:] = 255
contours , hierarchy = cv2.findContours(img[:,:,0],cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img2,contours,-1,(0,0,255),5)
i = 1
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    if cv2.contourArea(contour)>5000: 
        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,0),2)
        text = "objeto "+str(i) 
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.6
        font_color = (0,255,0)  
        thickness = 2
        line_type = cv2.LINE_AA
        cv2.putText(img2, text, (x,y), font, font_scale, font_color, thickness, line_type)
        i+=1

cv2.imshow('Imagen1', img2)
cv2.imshow('thres',img2)
cv2.imshow('ImagenOriginal', img)
cv2.waitKey()
cv2.destroyAllWindows()
 
""" fil,col,_ = img.shape
for i in range(fil):
    for j in range(col):
        if img[i,j,2] < 150 and  img[i,j,0] > 180 and img[i,j,1] > 80:
            img[i,j,:] = 0 
        else:
            img[i,j,:] = 255


img4 = img.copy() """
""" Erosion y Dilatacion """
""" 
dilatacion = cv2.dilate(img4,kernel,iterations=1)
plt.imshow(dilatacion)
plt.show()
erosion = cv2.erode(dilatacion,kernel,iterations=1)
plt.imshow(erosion)
plt.show() 
"""

""" cerrado = cv2.morphologyEx(img4,cv2.MORPH_CLOSE,kernel)
plt.imshow(cerrado)
plt.show()
abierto = cv2.morphologyEx(img4,cv2.MORPH_OPEN,kernel)
plt.imshow(abierto)
plt.show()
"""

""" contours , hierarchy = cv2.findContours(img[:,:,0],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2,contours,-1,(0,0,255),8)
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    if cv2.contourArea(contour)> 1000: 
        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow('Imagen1', img2)
cv2.imshow('ImagenOriginal', img)
cv2.waitKey()
cv2.destroyAllWindows()

"""

""" contours , hierarchy = cv2.findContours(img[:,:,0],cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img2,contours,-1,(0,0,255),8)

for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    if area > len(contour): 
        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,0),2)

cv2.imshow('Imagen1', img2)
cv2.imshow('ImagenOriginal', img)
cv2.waitKey()
cv2.destroyAllWindows()
"""