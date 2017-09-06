#https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html
import numpy as np
import matplotlib.pyplot as plt 
#declaramos una funcion que nos devuelva f(x)=exp(-x)*cos(2pi*x)
def f(t):
 return np.exp(-t) * np.cos(2*np.pi*t)

#definimos el rango de dos variables y el intervalo en el que cambian
t1=np.arange(0.0, 5.0, 0.1)
t2=np.arange(0.0, 5.0, 0.02)

#crea el grupo de graficas
plt.figure(1)
#crea el lienzo con dos renglones, una columna y entra a la primera seccion de esta division
plt.subplot(211)
#grafica la variable t1 contra la funcion f(t1) con circulos azules y grafica la variable t2 contra la funcion f(t2) con una linea negra
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

#entra a la segunda seccion del lienzo dividido
plt.subplot(212)
#grafica la variable t2 contra la funsion cos
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.savefig('Dosfunciones.png')
plt.show()
