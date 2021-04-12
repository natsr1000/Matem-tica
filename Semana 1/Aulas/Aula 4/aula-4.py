# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 08:43:51 2021

@author: Miguel Correia
"""

#Sequencias
import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,20,20)
an=2*n-1
print(an)
plt.scatter(n,an,label='an=2n-1')
plt.grid()
plt.legend()
plt.show()



#Exemplo de formula a partir de sequencia
import numpy as np
import matplotlib.pyplot as plt
seq=(0.25,0.5,0.75,1)
d=0.25
n=np.linspace(1,20,20)
an= 0.25+(n-1)*d
print(an)
plt.scatter(n,an,label='an=0.25n')
plt.xticks(n,list(range(20)))
plt.grid()
plt.legend()
plt.show()

n=np.linspace(1,20,20)
an=(-1)**n
print(an)

n=np.linspace(1,20,20)
an=n**2+1
print(an)

n=np.linspace(1,10,10)
an=3**n
print(an)


#Sum of some terms of a arrythmetic sequence
n=np.linspace(1,20,20)
an=0.25*n
sn=(4*(an[0]+an[3]))/2
print(sn)

#Geometric progression
#r=(a2/a1)=(a3/a2)=(a4/a3)=...
#an=a1*r**(n-1)
#sn=(a1*(1-r**n))/(1-r)

seq=(3,9,27,81)
if (9/3==27/9):
    r=9/3
else:
    r=None
n=np.linspace(1,20,20)
an=3*r**(n-1) #== (3*r**n)/r==3**n
print(an)
#Soma dos primeiros 5 elementos
sn=(an[0]*(1-3**n[4]))/(1-3)
print(sn)
#A soma disso é igual a...
sn=0
for n in range(1,6):
    sn+=3**n
print(sn)


#Outra soma

n=np.linspace(1,5,5)
an=2*n-1
sn=0
for n in range(0,5):
    sn+=2*n+1
print(sn)
#==
sn=(5*(an[0]+an[4]))/2
print(sn)
#==
print(np.sum(an))



#Find the sum of n=1 -> 12 4(0.3)**n
#r=a2/a1
r=(4*(0.3**2))/(4*(0.3**1))
def seq_sum_geo(a1,n,n_max,r):
    sn=(a1*(0.3**n))*(1-(r**n_max))/(1-r)
    return sn
a1=4
print(seq_sum_geo(a1,1,12,0.3)) #1.7142848032440001
print(seq_sum_geo(a1,0,12,0.3)) #5.714282677480001
def seq_sum_geo_wFor(n,n_max):
    soma=0
    for i in range(n,(n_max+1)):
        soma+=4*(0.3**i)
    return soma
print(seq_sum_geo_wFor(1,12)) #1.7142848032440001
print(seq_sum_geo_wFor(0,12)) #5.714282677480001



#Convergence

import matplotlib.pyplot as plt
import numpy as np
x = 1.0
n = 50
a=n/n+1
data = []
for i in range(n):
    x1 = i/(i + 1)
    if abs(x1 - x) < 1.e-3:
        print('a = {a}, n = {i}, result is {x}.'.format(a=a, i=i, x=x))
        last_index = i
        break
    else:
        pass
    x = x1
    data.append([i,x])
    last_index = n
plt.scatter(*zip(*data))
plt.hlines(y=1,xmin=0,xmax=last_index)
plt.xlim(0, last_index)

























