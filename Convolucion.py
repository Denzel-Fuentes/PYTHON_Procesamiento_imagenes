import  numpy as np
import cv2 as cv

import matplotlib.pyplot as plt 

n = 1000
i = np.array(range(n))

# intervalo de tiempo
t = i*np.pi/n*8
x = np.sin(t)
y = np.sin(2*t)
x1 = x+y
r = np.random.random_sample(size = n)-0.5

#senales staticas
plt.plot(t,x)
plt.plot(t,y)
plt.plot(t,x1)
plt.legend(["x","y","x1"])
plt.show()
#esta es la senal estatica con ruido
xr = x1 + r
plt.figure(figsize=(20,9))
plt.plot(t,xr)
plt.legend(["x1"])
plt.show()

#nueva senal
m = 15
g = np.ones((m,))/m
y = np.convolve(xr,g,"same")
plt.figure(figsize = (20,9))
plt.plot(t,xr)
plt.plot(t,y)
plt.plot(t,x1)
plt.legend(["xr","y"])
plt.show()


