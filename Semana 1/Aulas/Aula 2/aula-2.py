# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 08:41:28 2021

@author: Miguel Correia
"""

#Funções quadráticas

import numpy as np 
import matplotlib.pyplot as plt


x=np.linspace(-2,2,100)
y=x**2
plt.plot(x,y)

y=x**2+2
plt.plot(x,y,"-r")

y=2*x**2
plt.plot(x,y,"-g")
plt.grid()

y=-x**2
plt.plot(x,y,"-m")

y=x**2- 4
plt.plot(x,y,"-k")

plt.show()

def quadraticform(a,b,c):
    import numpy as np
    bef_sqrt=(b**2-4*a*c)
    if bef_sqrt>0:
        sqrt_val=np.sqrt(bef_sqrt)
    else:
        sqrt_val=False
    try:
        pos_quad=(-b+sqrt_val)/2
        neg_quad=(-b+sqrt_val)/2
    except:
        pass
    if sqrt_val==False:
        return "There is no place where they intersect with the x-axis"
    else:
        if pos_quad != neg_quad:
            statement="The function intersects x in",pos_quad,"and",neg_quad
            return statement
        else:
            statement="The function intersects x in only one value which is",pos_quad
            return statement
        

print(quadraticform(1,0,-4))

#Exponenciais, logaritmos e radicais


"""
Write each equation in it's exponential form:
    1.
    2=log7(x) == 7**2=(log7(x))**7 == 7**2=x
    
    2.
    3=log10(x+8) == 10**3=(log10(x+8)**10) == 10**3=x+8 == x=(10**3)-8
    
    3.
    log5(125)=x == (log5(125)**5)=5**x == 125=5**x
    
Rewrite into logarithms:
    1.
    2**4=16 == log2(16)=4
    
    2.
    sqrt(64)=8 == log64(8)=(1/2)  (sqrt(64)=64**(1/2))
    
    3.
    e**4=54.6 == 4=ln(54.6)
"""

#Funções exponenciais

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,3,20)
y1=2**x
y2=3**x
y3=(2**x)+4
y4=(2**(x+1))

plt.plot(x,y1,'m',label="2**x")
plt.plot(x,y2,'-b',label='3**x')
plt.plot(x,y3,'-r',label='(2**x)+4')
plt.plot(x,y4,label='(2**(x+1))')
plt.title('Exponential function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.grid()
plt.show()

#Funções logaritmas
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(1,100,200)
y1=np.sqrt(x)
plt.plot(x,y1,'-m',label='y=sqrt(x)')
plt.legend()
plt.grid()
plt.show()

x=np.linspace(1,100,200)
y1=np.log(x)
plt.plot(x,y1,'-m',label='y=log(x)')
plt.legend()
plt.grid()
plt.show()





























