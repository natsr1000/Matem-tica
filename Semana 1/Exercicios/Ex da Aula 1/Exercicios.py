# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 12:22:49 2021

@author: Miguel Correia
"""

#Exercicios funções
#1
import matplotlib.pyplot as plt
n=range(-10,-5)
h=[]
f_points=[]
g_points=[]
for i in range(len(n)):
    f=n[i]-5
    g=4*n[i]+2
    f_points.append(f)
    g_points.append(g)
    h.append((f+g))
plt.plot(n,f_points,"-b",marker=".",label="f(n)=n-5")
plt.plot(n,g_points,"-g",marker=".",label="g(n)=4n+2")
plt.plot(n,h,"-r",marker=".",label="f+g")
print("O valor de (g+f)(-8) é",h[2])
plt.legend()
plt.grid()
plt.show()

#2
import matplotlib.pyplot as plt
n=range(-12,-7)
f=[]
g_points=[]
h_points=[]
for i in range(len(n)):
    g=3*n[i]-2
    h=4*n[i]-2
    g_points.append(g)
    h_points.append(h)
    f.append((g+h))
plt.plot(n,g_points,"-b",marker=".",label="g(n)=3n-2")
plt.plot(n,h_points,"-g",marker=".",label="h(n)=4n-2")
plt.plot(n,f,"-r",marker=".",label="g+h")
print("O valor de (g+h)(-10) é",f[2])
plt.legend()
plt.grid()
plt.show()

#3
import matplotlib.pyplot as plt
n=range(-8,-3)
f=[]
g_points=[]
h_points=[]
for i in range(len(n)):
    g=n[i]**2-2
    h=2*n[i]+5
    g_points.append(g)
    h_points.append(h)
    f.append((g+h))
plt.plot(n,g_points,"-b",marker=".",label="g(n)=n^2-2")
plt.plot(n,h_points,"-g",marker=".",label="h(n)=2n+5")
plt.plot(n,f,"-r",marker=".",label="h+g")
print("O valor de (g+h)(-6) é",f[2])
plt.legend()
plt.grid()
plt.show()

#4

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,1000)
h=x+1
g=3*x-5
f=(3*(x**2))+(10*x)-25
plt.plot(x,h,"-b",label="h(n)=t+1")
plt.plot(x,g,"-g",label="g(n)=3t-5")
plt.plot(x,f,"-r",label="h/g")
val=(3*(5**2))+(10*5)-25
print("O valor de (h*g)(5) é",val)
plt.legend()
plt.grid()

#5
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,1000)
h=2*x-1
g=3*x-5
f=h/g
plt.plot(x,h,"-b",label="h(n)=2n-1")
plt.plot(x,g,"-g",label="g(n)=3n-5")
plt.plot(x,f,"-r",label="h/g")
plt.ylim(-10,10)
val=(2*0-1)/(3*0-5)
print("O valor de (h/g)(0) é",val)
plt.legend()
plt.grid()

#6
import matplotlib.pyplot as plt
import numpy as np

n=np.linspace(1,3,100)
g=n-3
h=-3*n**3+6*n
f=((-3)*(n**3))+7*n-3

plt.plot(n,g,"-b",label="g(n)=n-3")
plt.plot(n,h,"-g",label="h(n)=3n^3+6n")
plt.plot(n,f,"-r",label="g+h")
plt.legend()
plt.show()
val=f=((-3)*(1**3))+7*1-3
print("The value is",val)


#Exercicio Regressão linear

import numpy as np
import matplotlib.pyplot as plt
expenditure=[2400,2650,2350,4950,3100,2500,5106,3100,2900,1750]
income=[41200,50100,52000,66000,44500,37700,73500,37500,56700,35600]

mymodel=np.poly1d(np.polyfit(expenditure,income,1))

myline = np.linspace(1,7000,100000)

plt.scatter(expenditure,income)
plt.plot(myline,mymodel(myline))
plt.grid()
plt.show()
strfunc=str(mymodel)
print('The Slope of the function is {}'.format(strfunc.split('x')[0]))
print('The intersection of the function with y is'+format(strfunc.split('+')[1])+'+'+format(strfunc.split('+')[2]))