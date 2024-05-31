import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img  = cv.imread("zebra1.jpg",0)
plt.figure(figsize=(20,9))
plt.imshow(img,cmap="gray")
plt.show()
m = 55
g = np.ones((m,))/m
N,M = img.shape
Y = np.zeros((N,M))
for i in range(N):
    Y[i,:] = np.convolve(img[i,:],g,"same")
plt.figure(figsize=(20,9))
plt.imshow(Y,cmap="gray")
plt.show()

""" CON FILTRO GAUSIANO """
Y2 = np.zeros((N,M))
h1 = cv.getGaussianKernel(m, 7)
for i in range(N):
    Y2[i,:] = np.convolve(img[i,:],h1[:,0],"same")
plt.figure(figsize=(20,9))
plt.imshow(Y2,cmap="gray")
plt.show()