# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:23:33 2024

@author: Lenovo
"""
import  numpy as np
import cv2 as cv
import matplotlib.pyplot as plt 

n = 1000
i = np.array(range(n))

# intervalo de tiempo
t = i*np.pi/n*8
x = np.sin(t)
x1 = np.sin(t)
x2 = 0.3 * np.sin(20*t)
x = x1+x2
r = (np.random.random_sample(size = n)-0.5)*0.2


z = x+r
plt.figure(figsize=(20,9))
plt.plot(t,x1)
plt.plot(t,x2)
plt.plot(t,z)
plt.legend(["x1","x2","z"])
plt.show()

m = 25
h1 = cv.getGaussianKernel(m, 7)
h2 = cv.getGaussianKernel(m, 1)

plt.plot(h1)
plt.plot(h2)
plt.legend(["h1","h2"])
plt.show()


plt.figure(figsize=(20,9))
y1  = np.convolve(z , h1[:,0],"same")
y2 = np.convolve(z , h2[:,0],"same")
plt.plot(y1)
plt.plot(y2)
plt.legend(["y1","y2"])
plt.show()

#se reduce el ruido alto

plt.figure(figsize=(20,9))
plt.plot(x1)
plt.plot(y1)
plt.plot(x1-y1)
plt.legend(["x1","y1","error"])
plt.show()


plt.figure(figsize=(20,9))
plt.plot(x2)
plt.plot(y2-y1)
plt.plot(x2-(y2-y1))
plt.legend(['1','2','3'])
plt.show()
