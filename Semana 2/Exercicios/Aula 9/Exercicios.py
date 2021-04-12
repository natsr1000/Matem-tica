# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:43:37 2021

@author: Miguel Correia
"""

#1. Solve
#Part 1
import numpy as np
M=np.array([[10,20],[20,50]])
b=np.array([[1],[0]])
x,y=np.linalg.solve(M,b)
print('x =',x[0])
print('y =',y[0])

#Part 2
import numpy as np
M=np.array([[10,20],[20,50]])
b=np.array([[0],[1]])
t,z=np.linalg.solve(M,b)
print('t =',t[0])
print('z =',z[0])

#2. Find the inverses
#Part 1
import numpy as np
A=np.array([[0,0,0,2],[0,0,0,3],[0,4,0,0],[5,0,0,0]])
try:
    inv_A=np.linalg.inv(A)
    print(inv_A)
except:
    print("This array doesn't have an inverse")

#Part 2
import numpy as np
B=np.array([[3,2,0,0],[4,3,0,0],[0,0,6,5],[0,0,7,6]])
try:
    inv_B=np.linalg.inv(B)
    print(inv_B)
except:
    print("This array doesn't have an inverse")
    

#3. Find the inverses

import numpy as np
A=np.array([[0,3],[4,0]])
B=np.array([[2,0],[4,2]])
C=np.array([[3,4],[5,7]])
inv_A=np.linalg.inv(A)
inv_B=np.linalg.inv(B)
inv_C=np.linalg.inv(C)
print("The inverse of matrix A is\n",A)
print("The inverse of matrix B is\n",B)
print("The inverse of matrix C is\n",C)

#4. Find the numbers a and b that give the inverse of 5*eye(4)-ones(4,4)
#Part 1
import numpy as np
A=5*np.eye(4)
B=np.ones((4,4))
M=A-B
a=M[1][1]
b=M[1][2]
print("a =",a)
print('b =',b)

#Part 2 What are a and b in the inverse of 6*eye(5)-ones(5,5)
import numpy as np
A=6*np.eye(5)
B=np.ones((5,5))
M=A-B
a=M[1][1]
b=M[1][2]
print("a =",a)
print('b =',b)

"""
5.
Use matplotlib.pyplot.plot to produce a plot of the function 
f(x)=(e^(-x/10))*sin(pi*x) and g(x)=xe**(-x/3) over the interval of [0,10]
Include labels for the x and y axis, and a legend explaining which line
is which plot. Save the plot as a .jpg('jpeg') file and send me a copy
with your work.
"""
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,10001)
f=((np.e)**(-x/10))*(np.sin((np.pi*x)))
g=x*(np.e**(-x/3))
plt.plot(x,f,label='f(x)=(e^(-x/10))*sin(pi*x)')
plt.plot(x,g,label='g(x)=xe**(-x/3)')
plt.legend()
plt.xlabel('x values')
plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
plt.ylabel('y values')
plt.grid()
plt.savefig('Gráfico.jpg',format='jpg')
plt.show()


"""
6.
The function np.random.rand can be used to construct and fill vectors
and matrices with random numbers. Use the help of facility in python to
learn how to construct a 10x10 matrix named M filled with random numbers
"""
import numpy as np
import matplotlib.pyplot as plt
M=np.random.rand(10,10)
fig,ax = plt.subplots(1,1)
ax.axis('off')
ax.imshow(M)
ax.set_title('10x10 Matrix')
plt.savefig('Matriz.jpg',format='jpg')
plt.show()

"""
7.
The shape of a limaçon can be defined parametrically as 
                    r=r0+cos(O)
                    x=rcos(O)
                    y=rsin(O)
when r0=1 this curve is called a cardoid. Use this definition to plot
the shape of a limaçon for r0=0.8, r0=1.0, r0=1.2. Be sure to use enough
points that so that the curve is closed and appears smooth (except for
the cusp in the cardoid). Use a legend to identify which curve is which
"""
import numpy as np
import matplotlib.pyplot as plt
r0=[0.8,1.0,1.2]
colors=['red','purple','blue']
O=np.linspace(0,(2*np.pi),10000)
for i in range(3):
    r=r0[i]+np.cos(O)
    x=r*np.cos(O)
    y=r*np.sin(O)
    label_str="r0="+str(r0[i])
    plt.plot(x,y,color=colors[i],label=label_str)
plt.legend()
plt.show()

"""
8.
Exercicio da Lista 4 do sudoku
"""

import numpy as np
import sys
sudoku=np.array([[0,2,0,5,0,1,0,9,0],
                 [8,0,0,2,0,3,0,0,6],
                 [0,3,0,0,6,0,0,7,0],
                 [0,0,1,0,0,0,6,0,0],
                 [5,4,0,0,0,0,0,1,9],
                 [0,0,2,0,0,0,7,0,0],
                 [0,9,0,0,3,0,0,8,0],
                 [2,0,0,8,0,4,0,0,7],
                 [0,1,0,9,0,7,0,6,0]])
def print_board(sudoku):
    """ Shows the sudoku board in the console """
    for i in range(len(sudoku)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(sudoku[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")
            if j==8:
                print(sudoku[i][j])
            else:
                print(str(sudoku[i][j]) + " ", end="")

def ValuesAdd(y,x,num):
    global sudoku
    box_x=(x//3)*3
    box_y=(y//3)*3
    totalbox=0
    totalrow=0
    totalcol=0
    #Counting the sum of the box numbers
    for i in range(box_y,box_y+3):
        for j in range(box_x,box_x+3):
            totalbox+=sudoku[i][j]
    #Counting the sum of the column's numbers
    for i in range(len(sudoku[0])):
        totalrow+=sudoku[y][i]
    #Counting the sum of the row's numbers
    for i in range(len(sudoku)):
        totalcol+=sudoku[i][x]
    #Checking if the numbers are higher than what they can be
    if totalbox>45 or totalrow>45 or totalcol>45:
        return False
    else:
        return True

def possible(y,x,num):
    """checks to see if it's possible to insert a certain number(num) in a certain space(x,y) """
    global sudoku
    for i in range(0,9): #goes through the grids index
        if sudoku[y][i]==num: #checks to see if any row num is equal to this one
            return False
        if sudoku[i][x]==num: #checks to see if any column num is equal to this one
            return False
    box_y=(y//3)*3 #value to go through the num's box
    box_x=(x//3)*3 #value to go through the num's box
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[box_y+i][box_x+i]==num: #checks to see if there isn't an equal num in the box
                return False #if there is, returns false
    if ValuesAdd(y,x,num)==False: #checks the sum of the nums in row, column
        return False #and box, if they're bigger than 45 return false
    return True
    
def isSolution(sudoku):
    for y in range(9): 
        for x in range(9):
            if sudoku[y][x]==0: #checks which spaces are empty
                for num in range(1,10): #tries giving numbers to sudoku
                    if possible(y,x,num)==True:
                        sudoku[y][x]=num #inserts the number
                        isSolution(sudoku) #goes back to the beginning, checking for more empty spaces
                        sudoku[y][x]=0 #if there is a wrong number in a place, goes back and retries
                return 
    print_board(sudoku)
    print("-------------------------")
    print("Sudoku is solved!")
    sys.exit("Sudoku is solved!")
isSolution(sudoku)























