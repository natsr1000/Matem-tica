# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 09:26:57 2021

@author: Miguel Correia
"""

import numpy as np

#Exercicios trignometria
#1.
#x=arccos((AB/AC))
rad=np.arccos((4/7))
print(np.degrees(rad)) #x=55.15

#2.
#x=arctan((BC/CA))
rad=np.arctan((12/13))
print(np.degrees(rad)) #42.7

#3.
#x=arctan((CB/CA))
rad=np.arctan((16/10))
print(np.degrees(rad)) #x=57.99

#4.
#x=arctan((BC/CA))
rad=np.arctan((5.6/15.3))
print(np.degrees(rad)) #20.1


#Exercicios de funções periódicas
"""
y=4+(1/2)sin(x)
Esta função tem uma amplitude de 1 e um periodo de 2pi

y=-4cos((3x-pi))
Esta funçao tem uma amplitude de 4 e um periodo de 2pi/3 =(arredondado) 120 graus
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,25)
x1=np.linspace(0,2*np.pi,4*25)
y=4+(1/2)*np.sin(x)
y1=-4*np.cos(((3*x1)-np.pi))
plt.plot(x,y,"-r",label="y=4+(1/2)sin(x)")
plt.plot(x1,y1,"-b",label="y=4cos((3x-pi))")
plt.grid()
plt.legend()
plt.show()

"""
O valor minimo para ver o grafico mais suave é 25 pontos para o primeiro
enquanto o outro é 4 vezes o numero de pontos, assim, chega-se a 
conclusao que o numero de pontos necessario é 25*amplitude para vermos
um grafico suave
"""





























