# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 11:00:53 2021

@author: Miguel Correia
"""

#Check if the sequence converges using python:
import matplotlib.pyplot as plt
def n_seq(a,r,n):
    print(a)
    print(r)
    seq_val=[]
    for i in range(1,(n+1)):
        seq=a*(r**i)
        seq_val.append(seq)
    return seq_val
#if 0<r<1
n=20
seq=n_seq(1,0.5,n)
plt.scatter(list(range(1,(n+1))),seq,label='an=a*r^n, 0<r<1')
plt.hlines(0,0,20)
plt.legend()
plt.grid()
plt.show()

#if r>1
n=20
sq=n_seq(1,2,n)
plt.scatter(list(range(1,(n+1))),sq,label='an=a*r^n,r=>1')
plt.ylim(0,1000)
plt.legend()
plt.grid()
plt.show()

"""
enquanto quando o r é entre 0 e 1, existe uma convergência para 0, mas
quando o r é maior do que 1, não existe convergência, e age como se fosse
uma função exponencial
"""