# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 09:04:46 2021

@author: Miguel Correia
"""

#Graficos lineares parte 1

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,0,5)
x1 = 0
x2 = np.linspace(0,4,5)
x3 = np.linspace(0,4,5)
y=-x-3
y1=1
y2=x+2
y3=2*x3
plt.plot(x,y,'-r',label = 'y=x+2')
plt.plot(x1,y1,'-g',label='y=1',marker=".")
plt.plot(x2,y2,'-m',label='y=x-3',marker='.')
plt.plot(x3,y3,'-b',label='y=2x',marker='.')
plt.title('Linear graphs')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()
plt.show()

#Graficos lineares parte 2

import matplotlib.pyplot as plt
import numpy as np

x=[-5,5]
m=[1,1,3,5]
b=[-2,3/4,2,1]
color=['g','r','k','m']
for i in range(len(m)):
    y=m[i]*np.array(x) + b[i]
    plt.plot(x,y,label='y=%sx+%s'%(m[i],b[i]),color=color[i])

plt.axis('auto')
plt.xlim(x)
plt.ylim(x)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.legend(prop={'size':15})
plt.title('Generic Plot')
plt.show()

#Funções Constantes

import matplotlib.pyplot as plt

plt.hlines(y=3,xmin=1,xmax=10,colors='r')
plt.vlines(x=6,ymin=1,ymax=10,colors='r')
plt.title('Constant graphs')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

#Funções Continuas Polinomiais

#Função quadrática
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,10)
y1=x**2
plt.plot(x,y1,'-r')
plt.show()

#Função cubica
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,10)
y1=-3*x**3+6*x
plt.plot(x,y1,'-b')
plt.show()

#Função quadratica
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,10)
y1=-3*x**4+6*x+2*x
plt.plot(x,y1,'-g')
plt.show()

#Funções discretas

import matplotlib.pyplot as plt
x=list(range(-3,4))
y=[8,4,2,0,2,4,8]
color=['g','r','k','m','k','r','g']
for i in range(0,len(x)):
    plt.plot(x[i],y[i],'o',color=color[i])
plt.title('Função discreta')
plt.grid()
plt.show()

#Regressão polinomial

import numpy as np 
import matplotlib.pyplot as plt
x=[1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y=[100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x,y,8))

print(np.polyfit(x,y,8))

myline= np.linspace(1,22,100)

plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.grid()
plt.show()


















