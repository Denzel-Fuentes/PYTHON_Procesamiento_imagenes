import cv2
import numpy as np

imagen = np.zeros((500, 500), np.uint8)
img1 = imagen.copy()
img2 = imagen.copy()
img3 = imagen.copy()
img4 = imagen.copy()
x, y, w, h = 10, 10, 400, 400
cv2.rectangle(imagen, (x, y), (x+w, y+h), 255, 10)
cv2.rectangle(imagen, (x+40, y+40), ((x+w)-100, (y+h)-100), 255, 2)
cv2.imshow('ImagenOriginal', imagen)

contours , hierarchy = cv2.findContours(imagen,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours2 , hierarchy2 = cv2.findContours(imagen,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours3 , hierarchy3 = cv2.findContours(imagen,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours4 , hierarchy4 = cv2.findContours(imagen,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img1,contours,-1,(255),4)
cv2.drawContours(img2,contours2,-1,(255),5)
cv2.drawContours(img3,contours3,-1,(255),6)
cv2.drawContours(img4,contours4,-1,(255),7)
cv2.imshow('Imagen1', imagen)
cv2.imshow('Imagen2', imagen)
cv2.imshow('Imagen3', imagen)
cv2.imshow('Imagen4', imagen)

""" cv2.imshow('simple',contours)
cv2.imshow('None',contours2)
 """
cv2.waitKey()
cv2.destroyAllWindows()


""" import cv2
import numpy as np

imagen = np.zeros((500, 500), np.uint8)
img1 = imagen.copy()
img2 = imagen.copy()
img3 = imagen.copy()
img4 = imagen.copy()
x, y, w, h = 10, 10, 400, 400
cv2.rectangle(imagen, (x, y), (x+w, y+h), 255, 10)
cv2.rectangle(imagen, (x+40, y+40), ((x+w)-100, (y+h)-100), 255, 2)
cv2.imshow('ImagenOriginal', imagen)

contours , hierarchy = cv2.findContours(imagen,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours2 , hierarchy2 = cv2.findContours(imagen,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
contours3 , hierarchy3 = cv2.findContours(imagen,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours4 , hierarchy4 = cv2.findContours(imagen,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img1,contours,-1,(255),4)
cv2.drawContours(img2,contours2,-1,(255),5)
cv2.drawContours(img3,contours3,-1,(255),6)
cv2.drawContours(img4,contours4,-1,(255),7)
cv2.imshow('Imagen1', imagen)
cv2.imshow('Imagen2', imagen)
cv2.imshow('Imagen3', imagen)
cv2.imshow('Imagen4', imagen)
 """
""" cv2.imshow('simple',contours)
cv2.imshow('None',contours2)
 """
""" cv2.waitKey()
cv2.destroyAllWindows()
 """