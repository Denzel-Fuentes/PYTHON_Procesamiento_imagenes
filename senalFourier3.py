import random
import numpy as np
import cv2
import matplotlib.pyplot as plt
 
x = np.arange(-500, 501, 1)
longitudOnda  = 10
0
y = np.sin(2 * np.pi * x/longitudOnda)
 
plt.plot(x,y)
plt.show()
X, Y =np.meshgrid(x,x)
gradiente = np.sin(2 * np.pi * X/longitudOnda)
plt.set_cmap('gray')
""" plt.imshow(gradiente)
plt.show()
 
angulo = np.pi/ 4
gradiente2 =  np.sin(2 * np.pi * (X * np.cos(angulo)+ Y*np.sin(angulo))/longitudOnda)
plt.imshow(gradiente2)
plt.show()



plt.subplot(121)
plt.imshow(gradiente2)
fourier = np.fft.fft2(gradiente2)   
fourier = np.fft.fftshift(fourier)   
plt.subplot(122)
plt.imshow(abs(fourier))
plt.xlim([480,520])
plt.ylim([520,480])
plt.show()  """
 

""" TAREA DE SENAL GRADIENTS """
def gradients(n):
    gradiente = 0
    for i in range(1,n,1):
        angulo = np.pi/ random.randint(1, 4)
        gradiente+=np.sin(2 * np.pi * (X * np.cos(angulo)+ Y*np.sin(angulo))/random.randint(50, 200))
    return gradiente

gradienteF = gradients(5)
plt.subplot(121)
plt.imshow(gradienteF)
fourier = np.fft.fft2(gradienteF)   
fourier = np.fft.fftshift(fourier)   
plt.subplot(122)
plt.imshow(abs(fourier))
plt.xlim([480,520])
plt.ylim([520,480])
plt.show()