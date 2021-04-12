# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 08:40:28 2021

@author: Miguel Correia
"""

"""
Which graphs show relations that are functions:
    1. Function
    2. Not a Function
    3. Function (1/x)
    4. Function
    5. Not a Function

    
Given the following graph, Evaluate f(-1), Solve for f(x)=3.
f(-1)=1
f(x)=3 == x=2

Given the following graph, Evaluate f(0), Solve for f(x)=-3.
f(0) = 0
f(x) = -3 == x=-2 ^ x=2

Evaluate the expressions, given functions f,g and h,
f(x)=3x-2
g(x)=5-x^2
h(x)=-2x^2+3x-1

1. 3f(1)-4g(-2)
    3*(3*1-2)-4*(5-(-2)**2) =...
"""
print(3*(3*1-2)-4*(5-(-2)**2))
"""
    3f(1)-4g(-2)=-1

2.  f((7/3))-h(-2)
    (3*(7/3)-2)-(-2**(-2)+3*-2-1) =...
"""
print((3*(7/3)-2)-((-2)*(-2)**2+3*-2-1))
"""
    f((7/3))-h(-2)=20
    
Plot the folowing functions in python:
    (All functions in functions dictionary)
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10,10,200)
x_for_trig=np.linspace((-2*np.pi),(2*np.pi),200)
x_for_tan=np.linspace(((-np.pi)/2),((np.pi)/2),200)
functions={'y=x^4+3':x**4+3,'y=x^5+4x':x**5+4*x,'y=sqrt(x)+6':(np.sqrt(x)+6),
           'y=sqrt3(x)':x**(1/3),'y=tan(x)':np.tan(x_for_tan),'y=-x+2':-x+2,
           'y=-3x+2':-3*x+2,'y=-2x^2+1':2*(x**2)+1,'y=sin(2x)+4':(np.sin((2*x_for_trig))+4)}
for function in functions.items():
    if "sin" in function[0]:
        plt.plot(x_for_trig,function[1],label=function[0])
        plt.xticks([(-2*np.pi),0,(2*np.pi)],["-2pi","0","2pi"])
    elif "tan" in function[0]:
        plt.plot(x_for_tan,function[1],label=function[0])
        plt.ylim(-15,15)
        plt.xticks([((-np.pi)/2),0,((np.pi)/2)],["-pi/2","0","pi/2"])
    elif "cos" in function[0]:
        plt.plot(x_for_trig,function[1],label=function[0])
        plt.xticks([(-2*np.pi),0,(2*np.pi)],["-2pi","0","2pi"])
    else:
        plt.plot(x,function[1],label=function[0])
    plt.legend()
    plt.grid()
    plt.show()

"""
Determine the nth term of the sequence
a.
seq=(2,4,6,8,10,...) arrythmetic seq d=2
an=a1+(n-1)d = 2+(n-1)*2=2+2n-2= 2n

an=2n
"""
import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,20,20)
an=2*n
plt.scatter(n,an)

"""
b.
seq=(1,3,5,7,9,...) arrythmetic seq d=2
an=a1+(n-1)d = 1+(n-1)*2 = 1+2n-2= 2n-1

an=2n-1
"""
n=np.linspace(1,20,20)
an=2*n-1
plt.scatter(n,an)

"""
c.
seq=(99,199,299,399,499,...) arrythmetic seq d=100
an=a1+(n-1)d = 99+(n-1)*100 = 99+100n-100 = 100n-1

an=100n-1
"""
n=np.linspace(1,20,20)
an=100*n-1
plt.scatter(n,an)

"""
d.
seq=(3,-5,7,-9,11,...) 
an=(2n+1)*(-(-1)**n)

"""
import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(1,20,20)
an=(2*n+1)*(-(-1)**n)
plt.scatter(n,an)

"""
e.
seq=(2,(3/2),(4/3),(5/4),(6/5),...) two arrythmetic seq dividing
d=1
an=ax/ay
ax=2+(n-1)*1 = 1+n
ay=1+(n-1)*1 = n

an=(1+n)/n
"""
n=np.linspace(1,20,20)
an=(1+n)/n
plt.scatter(n,an)

"""
f.
seq=(1,4,9,16,25,...) two arrythmetic seq mult
d=1
an=ax*ay
ax=n
ay=n
an=n*n
an=n**2
"""
n=np.linspace(1,20,20)
an=n**2
plt.scatter(n,an)


"""
g.
seq=(0,2,6,12,20,...) two arrythmetic seq mult
an=ax*ay
ax=(-1+n)
ay=n
an=(-1+n)*n
"""
n=np.linspace(1,20,20)
an=(-1+n)*n
plt.scatter(n,an)

"""
h.
seq=(1,(2/3),(4/9),(8/27),(16/81),...) two geometric seq diving
an=ax/ay
rax= 2/1 = 4/2 = 2
ray= 3/1 = 9/3 = 3
ax=1*2**(n-1) = 2**(n-1)
ay=1*3**(n-1) = 3**(n-1)
an=(2**(n-1))/(3**(n-1)) =(2/3) ** (n-1)
"""
n=np.linspace(1,20,20)
an=(2/3)**(n-1)
plt.scatter(n,an)

"""
i.
seq=(6,12,20,30,42,...)
an=????
"""
n=np.linspace(1,20,20)
an=((n+1)**2+(n+1))
plt.scatter(n,an)


"""
j.
seq= ((2/3),(3/(2*4)),(4/(3*5)),(5/(4*6)),(6/(5*7)))
an=ax/(ay*az)
ax=n+1
ay=n
az=n+3
an((n+1)/n*(n+2)) = ((n+1)/(n**2+2n))
"""
n=np.linspace(1,20,20)
an=((n+1)/(n*(n+2)))
plt.scatter(n,an)

"""
k.
seq = (0,(1/3),0,(1/3),0,...)
an=(-1/6)*sin((pi/2)+pi*n)+(1/6)
ou...
an=(-1/6)*cos(pi*n)+(1/6)
"""
import numpy as np
import matplotlib.pyplot as plt
n=np.linspace(-7,7,15)
an=(-1/6)*np.sin((np.pi/2)+np.pi*n)+(1/6)
plt.scatter(n,an)

"""
l.
seq = (-(1/2),(2/5),-(3/8),(4/11),-(5/14),...)
an=((-1)**n)*((n)/(2*n+(n-1)))
"""
n=np.linspace(1,20,20)
an=((-1)**n)*((n)/(2*n+(n-1)))
plt.scatter(n,an)



"""
Find the sum of the first five terms of the sequence:
    a)
    an+1=an-1.5
    a1=3.5
"""
seq=[3.5]
soma=seq[0]
for n in range(4):
    an1=seq[n]-1.5
    soma+=an1
    seq.append(an1)
print("The sum of the first five members are",soma) #2.5

"""
b)
    an+1=(1/an)-1
    a1=5
"""
seq=[5]
soma=seq[0]
for n in range(4):
    an1=(1/seq[n])-1
    soma+=an1
    seq.append(an1)
print("The sum of the first five members are",soma) #-1.18 = -(2777/2340)

"""
c)
    an+1=(an^2-n**2)/2
    a1=1
"""
seq=[1]
soma=seq[0]
for n in range(4):
    an1=((seq[n]**2)-((n+1)**2))/2
    soma+=an1
    seq.append(an1)
print("The sum of the first five members are",soma) #-8.375 = -(67/8)

"""
d)
    an+1=sqrt(an)
    a1=65.536
"""
import numpy as np
seq=[65536]
soma=seq[0]
for n in range(1,5):
    an1=np.sqrt(seq[(n-1)])
    soma+=an1
    seq.append(an1)
print("The sum of the first five members are",soma) #65814

"""
e)
    an+1=(2**(n+1))*(((n+1)**2)-(2*an))
    a1=1
"""
seq=[1]
soma=seq[0]
for n in range(1,5):
    an1=(2**n)*((n**2)-(2*seq[(n-1)]))
    soma+=an1
    seq.append(an1) 
print("The sum of the first five members are",soma)


















