# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 08:37:38 2021

@author: Miguel Correia
"""

#Matrizes

#row matrix
import numpy as np
print(np.array([2,3]))
print(np.matrix('2 3'))

#Col matrix
print(np.matrix('2;3'))

#diagonal matrix
print(np.diag([5,-7,3]))

#Unit matrix
b=np.eye(3)
print(b)



#Addition
import numpy as np
m1=np.matrix('2 3 ; 1 5')
m2=np.matrix('4 1 ; 1 2')
print((m1+m2))


#Multiplication
import numpy as np
m1=np.matrix('2 3 ; 1 5')
m2=np.matrix('4 1 ; 1 2')
print((m1*m2))

A=np.matrix('-1 3 ; 4 2')
B=np.matrix('1 2 ; 3 4')
C=B*A
D=A*B
print(C)
print(D)

#Matriz transporta é trocar a linha pela coluna

#Mais multiplicaçao

import numpy as np
A=np.matrix('2 2 ; 1 1')
B=np.matrix('-1 -2 ; 1 2')
C=A*B
print(C)

#C=0 mas nem A nem B =0

import numpy as np
A=np.matrix('2 2 ; 1 1')
B=np.matrix('1 2 ; 1 2')
C=np.matrix('4 10 ; -2 -5')
AB=A*B
AC=A*C
print(AB)
print(AC)

A=np.array([[2,2],[1,1]])
B=np.array([[1,2],[1,2]])
C=np.array([[4,10],[-2,-5]])
AB=A*B
AC=A*C
print(AB)
print(AC)

#Matrizes determinantes
import numpy as np
a=np.matrix('0 3 ; 4 0') 
print(np.linalg.det(a)) #= 0*0-3*4

b=np.matrix('2 3 1 ; 4 5 -1 ; 2 1 0')
print(np.linalg.det(b))


#Matrizes inversas
X=np.matrix('1 2 ; 3 4')
print(np.linalg.inv(X))


#Calculo de matrizes com incognitas
#Modo dificil
import numpy as np
A=np.matrix('1 2;6 -3')
A1=np.matrix('3 2;8 -3')
A2=np.matrix('1 3;6 8')
det1=np.linalg.det(A)
det2=np.linalg.det(A1)
det3=np.linalg.det(A2)
print('x =', (det2/det1))
print('y =', (det3/det1))

#Modo inverso
import numpy as np
A=np.matrix('1 2;6 -3')
B=np.array([3,8])
X=np.linalg.inv(A).dot(B)
print('x,y =',X)

#Modo divertido :)
import scipy.linalg as sc
import numpy as np
M=np.matrix('1 2;6 -3')
b=np.array([3,8])
x=np.linalg.solve(M,b)
y= sc.solve(M,b)
print(x)
print(y)

#matplotlib nisto

import numpy as np
import matplotlib.pyplot as plt
l=[]
l1=[]
fig,ax = plt.subplots(3,1)
M=np.array([[1,3,-5,2],[0,4,-2,1],[2,-1,3,-1],[1,1,1,1]])
b=np.array([0,6,5,10])
l.append(b)
x=np.linalg.solve(M,b)
print(M)
print(b)
print(x)
l1.append(x)
ax[0].axis('off')
ax[0].imshow(M)
ax[1].axis('off')
ax[1].imshow(l)
ax[2].imshow(l1)
ax[2].axis('off')

























