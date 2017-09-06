import numpy as np
import pylab as pl 
#Vector (arreglo) con los valores del eje x
x=[6000,7000,8000,9000,10000]
#Vector (arreglo) con los valores del eje y
y=[73,80,85,87,89]
#Grafica el vector x contra el vector y
pl.plot(x,y)
x1=[7000,8000,9000,10000,11000]
y2=[80,83,85,86,88]
pl.plot(x1,y2)
pl.ylabel('Eficiencia [%]')
pl.xlabel('Voltaje [V]')
pl.title('Eficiencia contra Voltaje')

#Guarda la grafica
pl.savefig('temp1.png') 
