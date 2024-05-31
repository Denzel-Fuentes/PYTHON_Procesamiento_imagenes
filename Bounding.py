import cv2

img  = cv2.imread("geometricas.png")
img2 = img.copy()

fil,col,_ = img.shape
imgGris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(imgGris,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,5)
contours , hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img2,contours,-1,(0,0,255),8)
cv2.imshow('Imagen1', img2)
cv2.imshow('thres',thresh)
cv2.imshow('ImagenOriginal', img)
cv2.waitKey()
cv2.destroyAllWindows()