# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:38:37 2021

@author: Miguel Correia
"""

#a)
import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(1,10,10)
n=100*(np.e**(2*t))
plt.plot(t,n)
plt.hlines(1000000,0,10)
plt.yscale('log')
#n=100*e**2t == n/100=e**2t == ln(n/100)=2t == ln(n/100)/2=t
val=np.log((1000000/100))/2
print("It takes",val,"months for the population to reach one million")
#or...
t_list=list(np.linspace(4,5,1000))
for t in t_list:
    n=100*(np.e**(2*t))
    if n>=1000000:
        break
    else:
        pass
print("It takes",t,"months for the population to reach one million")

#b)
#i.
M=np.linspace(0,10,11)
E=1.74*(10**19)*(10**(1.44*M))
plt.plot(M,E)
plt.yscale('log')
plt.xticks(list(range(0,11)),list(range(0,11)))
plt.grid()
plt.show()

e=1.74*(10**19)*(10**(1.44*5))
print('The Earthquake of that magnitude released',e,'Joules')

#ii.
double_e=e*2
m_list=list(np.linspace(4,6,10000))
for M in m_list:
    E=1.74*(10**19)*(10**(1.44*M))
    if E>=double_e:
        break
    else:
        pass
print('The magnitude of the Earthquake was of {M:.2f} on the Richter scale'.format(M=M))


#The data below obeys a power law y=A*(x**n). Obtain the equation and
#select the correct statement

x=[5,15,30,50,95]
y=[10,90,360,1000,3610]
import numpy as np
import matplotlib.pyplot as plt
plt.plot(x,y,"o")
plt.show()
#n=(log(y2) - log(y1))/(log(x2) - log(x1))

y1=np.log10(y[1])
y0=np.log10(y[0])
n_y=y1-y0
x1=np.log10(x[1])
x0=np.log10(x[0])
n_x=x1-x0
n=n_y/n_x
print(n)

logx=np.log10(x)
logy=np.log10(y)
plt.plot(logx,logy,"o")
plt.show()
print(np.poly1d(np.polyfit(logx,logy,1))) #2x-0.3979
A=10**(-0.3979)
print(A) #2/5

#n=2 e A=2/5




























    