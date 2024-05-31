import cv2
import numpy as np
import matplotlib.pyplot as plt
img  = cv2.imread("fuego.png")
madera_img = cv2.imread("madera.jpg")
fuego_img = cv2.imread("fuego1.jpg")
pa1isaje_img = cv2.imread("paisaje.jpg")

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
cv2.drawContours(img2,contours,-1,(0,0,255),2)
i = 1
for contour in contours:
    x,y,w,h = cv2.boundingRect(contour)
    if cv2.contourArea(contour)>15000:
        objeto = cv2.resize(fuego_img, (w, h))
        if cv2.contourArea(contour) > 42000:
            objeto = cv2.resize(madera_img, (w, h))
        if cv2.contourArea(contour) < 40000:
            objeto = cv2.resize(madera_img, (w, h))

        matriZeros = np.zeros((fil,col),dtype=np.uint8) 
        cv2.drawContours(matriZeros, [contour], -1, (255, 255, 255), -1) 
        for i in range(y, y + h):
            for j in range(x, x + w):
                if matriZeros[i, j] == 255:  
                    img[i, j] = objeto[i - y, j - x] 

objeto = cv2.resize(pa1isaje_img, (col,fil))
for i in range(fil):
    for j in range(col):
        if (img[i,j,1] == 0).all(): 
            img[i,j] = objeto[i,j] 
        
  
cv2.imshow('thres',img2)
cv2.imshow('ImagenOriginal', img)
cv2.waitKey()
cv2.destroyAllWindows()