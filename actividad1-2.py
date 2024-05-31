import numpy as np

x = np.array([1, 1, 1, 3, 3, 3, 0, 0, 0, 2, 2,2])
g = np.array([-1, 0, 1])
n = len(x)
m = len(g)
longitud = n - m + 1
y = np.zeros(longitud)

""" x[i:i+m] extrae una subsección del array x 
g[::-1] invierte el array"""
for i in range(longitud):
    y[i] = np.sum(x[i:i+m] * g[::-1])  
