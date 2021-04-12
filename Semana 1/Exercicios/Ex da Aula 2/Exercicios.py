# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 09:32:42 2021

@author: Miguel Correia

7,8 e 10
"""

#Exponenciais exercicios
import numpy as np
import matplotlib.pyplot as plt
"""
1.
(3**2)/3=(3*3)/3=3
"""
x=3
plt.hlines(3,-5,5,label="y=3")
plt.legend()
plt.show()

"""
2.
(3n(m**2))/(3n)=m**2
"""
m=np.linspace(-5,5,100)
y=m**2
plt.plot(m,y,label="y=m^2")
plt.legend()
plt.show()

"""
3.
(4(x**3)(y**4))/(3x(y**3))=(4/3)*(((x**3)(y**4))/(x(y**3)))=(4/3)*(x**2)y
=(4(x**2)y)/3

y=1, logo (4(x**2)/3)
x=1, logo (4y/3)
"""

x=np.linspace(-5,5,100)
y=((4*(x**2))/3)
plt.plot(x,y,label="y=4x^2/3")
y=np.linspace(-5,5,100)
x=4*y/3
plt.plot(y,x,"-r",label="x=4y/3")
plt.legend()
plt.show()

"""
4.
(((x**3)(y**4))*(2(x**2)(y**3)))**2=(2(x**(3+2))(y**(4+3)))**2=(2(x**5)(y**7))**2
=(2**2)((x**5)**2)((y**7)**2)=4(x**10)(y**14)

resposta = 4(x**10)(y**14)

5.
2x(((x**4)(y**4))**4)=2x((x**(4*4))(y**(4*4)))=2x((x**16)(y**16))
=2((x**17)(x*(y**16)))

resposta = 2((x**17)((y**16)))

6.
(3**4)/3=3**3=27
"""
plt.hlines(27,-5,5,label="y=27")
plt.legend()
plt.show()

"""
7.
((x**2)(y**4))/(4*x*y)=(x(y**3))/4
x=1, logo (y**3)/4
y=1, logo x/4
"""
y=np.linspace(-5,5,100)
x=(y**3)/4
plt.plot(y,x,label="x=y^3/4")
x=np.linspace(-5,5,100)
y=x/4
plt.plot(x,y,"-r",label="y=x/4")
plt.legend()
plt.show()

"""
8.
(x(y**3))/(4xy)=(y**2)/4
"""
y=np.linspace(-5,5,100)
x=(y**2)/4
plt.plot(y,x,label="x=y^2/4")
plt.legend()
plt.show()

"""
9.
(((u**2)(v**2))*(2(u**4)))**3=(2(u**6)(v**2))**3=(2**3)(u**(6*3))(v**(2*3))
=8(u**18)(v**6)

resposta = 8(u**18)(v**6)

10.

((3v(u**5))*(2(v**3)))/((u(v**2))*(2(u**3)v))=(6(v**4)(u**5))/(2(u**4)(v**3))
=3vu

v=1, logo, 3u == u=1, 3v
"""
u=np.linspace(-5,5,100)
y=3*u
plt.plot(u,y,label="y=3u or y=3v")
plt.legend()
plt.show()

#Exercicios Logaritmos

import numpy as np
#1
print((0.6**(np.sqrt(3)))) #0.4128066587835584

#2
print(((np.e)**3.2)) #24.53253019710935

#3
print(((1.0005)**400)) #1.2213417098970276

#4
#log4(64) = log4((4**3)) = 3, answer = 3

#5
#ln 1 = 0 
print((np.log(1)))

#6
print((np.log((np.sqrt(7))))) #0.9729550745276567

"""
7.
log5(25) = log5(5**2) = 2

8.
log3((1/81)) = log3(1) - log3(81) = 0 - log3(3**4) = -4

9.
ln((e**-2)) = -2

10.
log7(3) = log10(3)/log10(7)
"""
print((np.log10(3)/np.log10(7))) #0.5645

"""
11.
log2(1/2) = log(2**-1) = -1

12.
log15(42) = log10(42)/log10(15)
"""
print((np.log10(42)/np.log10(15))) #1.380

#13.
#log10(10x) = log10(10) + log10(x) = 1 + log10(x)
import matplotlib.pyplot as plt
x=np.linspace(1,100,1000)
y=1+np.log10(x)
plt.plot(x,y)
plt.grid()
plt.show()

"""
14.
ln(((x*y)/z)) = ln(x*y) - ln(z) = ln(x) + ln(y) + ln(z)

15.
log4(4(x**2)) = log4(4) + log4(x**2) = 1 + 2log4(x)
para fazer no spyder...
1 + 2*(log10(x)/log10(4))
"""
x=np.linspace(1,100,1000)
y=1+2*((np.log10(x))/(np.log10(4)))
plt.plot(x,y)
plt.grid()
plt.show()

#16.
#log3(sqrt(x-2))=log3((x-2)**(1/2))=(1/2)*log3(x-2) para fazer no spyder...
#(1/2)*((log2(x-2))/log2(3))
x=np.linspace(3,100,1000)
y=(1/2)*((np.log2(x-2))/np.log2(3))
plt.plot(x,y)
plt.grid()
plt.show()

#17.
#ln((sqrt(3x))/7)=ln((3x)**(1/2))-ln(7)=(1/2)(ln(3x))-ln(7)
x=np.linspace(1,100,1000)
y=(1/2)*(np.log(3*x))-np.log(7)
plt.plot(x,y)
plt.grid()
plt.show()


#Exercicios radicais
"""
1.
3sqrt(12)=3sqrt(2*2*3)=3*2sqrt(3)=6sqrt(3)

2.
6sqrt(128)=6sqrt(2*64)=6*2sqrt(32)=12sqrt(2*16)=12*2sqrt(8)=24sqrt(2*4)
=24*2sqrt(2)

3.
7sqrt(128)=7*2*2*2sqrt(2)=56sqrt(2)

4.
-8sqrt(392)=-8sqrt(2*196)=-8*2sqrt(98)=-16sqrt(98)=-16sqrt(2*49)
=-16sqrt(2*7*7)=-16*7sqrt(2)=-112sqrt(2)

5.
-7sqrt(63)=-7sqrt(7*9)=-7sqrt(7*3*3)=-7*3sqrt(7)=-21sqrt(7)

6.
sqrt(192n)=sqrt(2*96n)=2sqrt(48n)=2sqrt(2*24n)=4sqrt(12n)=8sqrt(3n)
"""
import matplotlib.pyplot as plt
import numpy as np

n=np.linspace(1,10,100)
y=8*np.sqrt(3*n)
plt.plot(n,y,label='y=8sqrt(3n)')
plt.legend()
plt.grid()
plt.show()

"""
7.
sqrt(343b)=sqrt(7*49b)=7sqrt(7b)
"""

import matplotlib.pyplot as plt
import numpy as np

b=np.linspace(1,10,100)
y=7*np.sqrt(7*b)
plt.plot(b,y,label='y=7sqrt(7b)')
plt.legend()
plt.grid()
plt.show()

"""
8.
sqrt(192(n**2))=n*sqrt(2*96)=2n*sqrt(48)=2n*sqrt(2*24)=4n*sqrt(12)
=8nsqrt(3)
"""

import matplotlib.pyplot as plt
import numpy as np

n=np.linspace(1,10,100)
y=4*n*np.sqrt(3)
plt.plot(n,y,label='y=8n*sqrt(3)')
plt.legend()
plt.grid()
plt.show()

"""
9.
sqrt(100(n**3))=sqrt(10**2(n**2)n)=10nsqrt(n)
"""

import matplotlib.pyplot as plt
import numpy as np 
n=np.linspace(1,10,100)
y=10*n*np.sqrt(n)
plt.plot(n,y,label='y=10n*sqrt(n)')
plt.legend()
plt.grid()
plt.show()

"""
10.
sqrt(200(a**3))=sqrt(2*100*(a**2)*a)=10a*sqrt(2a)
"""

import matplotlib.pyplot as plt
import numpy as np
a=np.linspace(1,10,100)
y=10*a*np.sqrt((2*a))
plt.plot(a,y,label='y=10a*sqrt(2a)')
plt.legend()
plt.grid()
plt.show()


















