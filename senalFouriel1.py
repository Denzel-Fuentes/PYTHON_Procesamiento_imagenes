import matplotlib.pyplot as plt
import numpy as np

x  = np.linspace(0,2*np.pi,300)
plt.plot(x,np.sin(x))
plt.plot(x,np.sin(2*x))
plt.plot(x,np.sin(x)+np.sin(2*x))

plt.xlabel("angulo")
plt.ylabel("seno(x)")
plt.show()

tiempo = np.arange(0,10,0.01)
senal = (2*np.sin(2*np.pi*1*tiempo)+ 
        2*np.sin(2*np.pi*2*tiempo)+
        3*np.sin(2*np.pi*4*tiempo)+
        1*np.sin(1*np.pi*1*tiempo))


plt.plot(tiempo,senal)
plt.title("original")
plt.xlabel("tiempo")
plt.ylabel("amplitud")
plt.show()

""" sacamos la transformada de fourier """
fourier = np.fft.fft(senal)
""" sacamos las frecuencaias de esa transformada """
frecuencia = np.fft.fftfreq(len(senal),0.01)
plt.figure(figsize=(10,4))
plt.subplot(2,1,2)
plt.plot(frecuencia,np.abs(fourier))
plt.title("Fourier")
plt.xlabel("Frecuencia")
plt.ylabel("Magnitud")
plt.xlim(0,5)
plt.tight_layout()
plt.show()

tiempo = np.arange(0,10,0.01)
#sin(x) + sin(3*x)/3 + sin(5*x)/5 + sin(7*x)/7
def senalTest(n,tiempo):
    total = 0
    x =  np.pi*tiempo
    for i in range(1,n,2):
        total+=np.sin(x*i)*i
    return total 

def graficoFourier(n,tiempo):
    total = 0
    x = 2 * np.pi*tiempo
    for i in range(1,n,2):
        total+=2*np.sin(i*x)
    return total 

plt.plot(tiempo,graficoFourier(20,tiempo))
plt.title("Onda Original")
plt.xlabel("tiempo")
plt.ylabel("amplitud")
plt.show()