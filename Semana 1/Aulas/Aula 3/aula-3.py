# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 08:39:22 2021

@author: Miguel Correia
"""

#Trignometria

def ang_to_rad(ang):
    import numpy as np
    ang_to_r=ang*((np.pi)/180)
    return ang_to_r
#Exemplos
#1.

import numpy as np 
#x = BC/sen(24)
print((13/(np.sin((24*((np.pi)/180)))))) #x=31.96

#2.
#x=BC/cos(52.3)
print((5/(np.cos(ang_to_rad(52.3))))) #x=8.17

#3.
#x=tan(71)*BC
print((np.tan(ang_to_rad(71))*9)) #x=26.1

#4.
#x=BC/cos(63)
print((7.6/(np.cos(np.radians(63))))) #x=16.7


#Most angles used in math located in the first quadrant (for right angle)
import numpy as np
np.set_printoptions(precision=2)
np.set_printoptions(formatter={"float":'{:0.2f}'.format})
a = np.array([0,30,45,60,90])
print('Sine of different angles:')
# Convert to radians by multiplying to pi/180
print(np.sin(a*np.pi/180), "\n")
print("Cosine values for angles in array:")
print(np.cos(a*np.pi/180), "\n")
print('Tangent values for given angles:')
print(np.tan(a*np.pi/180))

#Graphs for the sine and cosine (for a full trig circle)

#Sine

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,360,360)
y=np.sin(np.radians(x))
plt.plot(x,y,"-r",label='y=sin(x)')


#Cosine

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,360,360)
y=np.cos(np.radians(x))
plt.plot(x,y,label='y=cos(x)')
plt.grid()
plt.legend()
plt.show()

#Graphs for various changes to sine (can be applied to cosine too) funcs

import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
y1=2*np.sin(x)
y2=np.sin(x+1)
y3=np.sin(x)+1
y4=-np.sin(x)
functions={'y=sin(x)':y,'y=2sin(x)':y1,'y=sin(x+1)':y2,'y=sin(x)+1':y3
           ,'y=-sin(x)':y4}
for f in functions.items():
    plt.plot(x,f[1],label=f[0])
plt.grid()
plt.legend()
plt.show()

#What is not a function?

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
X, Y = np.meshgrid(x,y)
f = X**2+Y**2 -16
fig, ax = plt.subplots()
ax.contour(X,Y,f,[0])
plt.title('circle graph ')
plt.xlabel('x', color='#1C2836')
plt.ylabel('y', color='#1C2833')
plt.grid()
plt.show()





















