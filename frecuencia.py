import numpy as np
import cv2
import matplotlib.pyplot as plt

img  = cv2.imread("estacion.png",cv2.IMREAD_GRAYSCALE)

gaus = cv2.GaussianBlur(img,(19,19),0)

Z = np.concatenate((img,gaus),axis=1)

plt.imshow(Z,cmap="gray")
plt.show()


Id  =  img.astype(float)
Lf = gaus.astype(float)
Hd = Id - Lf
plt.imshow(Hd,cmap="gray")
plt.show()

""" convertir a valor absoluto """

H = np.abs(Hd)
H = H-np.min(H)
H = H/np.max(H)*255
Z = np.concatenate((img,H),axis=1)

plt.imshow(Z,cmap="gray")
plt.show()

E = (H>50)*255
plt.imshow(E,cmap="gray")
plt.show()



