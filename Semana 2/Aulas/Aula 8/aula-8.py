# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 08:46:17 2021

@author: Miguel Correia
"""

import numpy as np
import random
import matplotlib.pyplot as plt
simulation_number = 100000
club =0;spade=0;diamond=0;heart=0;percentages =[]
for i in range(0, simulation_number):
    card_points =[1,13,12,11,10,2,3,4,5,6,7,8,9]
    card_signs =['Heart','CLUB','DIAMOND','SPADE']
    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card = random_point,random_sign
    # print (random_card)
    ##Condition
    if ((random_card[1] == 'Heart') or (random_card[1] == 'DIAMOND') or
        (random_card[0] == 1) and (random_card[1] == 'SPADE') or
        (random_card[0] == 1) and (random_card[1] == 'CLUB')):
        club+=1
  
X=[]
if club > 0:
    percentages.append(np.round(club/simulation_number*100,2))
    X.append('CLUBS')
if spade > 0:
    percentages.append(np.round(spade/simulation_number*100,2))
    X.append('SPADE')
if diamond > 0:
    percentages.append(np.round(diamond/simulation_number*100,2))
    X.append('DIAMOND')
if heart > 0:
    percentages.append(np.round(heart/simulation_number*100,2))
    X.append('Heart')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X,percentages)
print(sum(percentages), '%')


"""
Example
A bag contains 15 balls...

Sample space = 2 blue balls, 1 blue and 1 red, 1 red and 1 blue, and 
2 red balls
"""

#P(AnB)

import numpy as np
import random
import matplotlib.pyplot as plt
simulation_number = 100000
club =0;spade=0;diamond=0;heart=0;percentages =[]
for i in range(0, simulation_number):
    card_points =[1,13,12,11,10,2,3,4,5,6,7,8,9]
    card_signs =['Heart','CLUB','DIAMOND','SPADE']
    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card = random_point,random_sign
    # print (random_card)
    ##Condition
    if (random_card[0] == 7) and (random_card[1] == 'SPADE'):
        club+=1
    if (random_card[0] == 7) and (random_card[1] == 'SPADE'):
        spade+=1
        
  
X=[]
if club > 0:
    percentages.append(np.round(club/simulation_number*100,2))
    X.append('CLUBS')
if spade > 0:
    percentages.append(np.round(spade/simulation_number*100,2))
    X.append('SPADE')
if diamond > 0:
    percentages.append(np.round(diamond/simulation_number*100,2))
    X.append('DIAMOND')
if heart > 0:
    percentages.append(np.round(heart/simulation_number*100,2))
    X.append('Heart')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X,percentages)
print(sum(percentages), '%')


#P(A|B)

import numpy as np
import random
import matplotlib.pyplot as plt
simulation_number = 100000
club =0;spade=0;diamond=0;heart=0;percentages =[]
for i in range(0, simulation_number):
    card_points =[1,13,12,11,10,2,3,4,5,6,7,8,9]
    card_signs =['Heart','CLUB','DIAMOND','SPADE']
    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card = random_point,random_sign
    # print (random_card)
    ##Condition
    if (random_card[0] == 1) and random_card[0] == 'DIAMOND' or random_card[1] == 'Heart':
        club+=1
  
X=[]
if club > 0:
    percentages.append(np.round(club/simulation_number*100,2))
    X.append('CLUBS')
if spade > 0:
    percentages.append(np.round(spade/simulation_number*100,2))
    X.append('SPADE')
if diamond > 0:
    percentages.append(np.round(diamond/simulation_number*100,2))
    X.append('DIAMOND')
if heart > 0:
    percentages.append(np.round(heart/simulation_number*100,2))
    X.append('Heart')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X,percentages)
print(sum(percentages), '%')


#Probabilidade de, saber que a carta é de paus, sair um rei 
import numpy as np
import random
import matplotlib.pyplot as plt
simulation_number = 100000
club =0;spade=0;diamond=0;heart=0;percentages =[]
for i in range(0, simulation_number):
    card_points =[1,13,12,11,10,2,3,4,5,6,7,8,9]
    card_signs =['CLUBS']
    random_point = random.choice(card_points)
    random_sign = random.choice(card_signs)
    random_card = random_point,random_sign
    # print (random_card)
    ##Condition
    if (random_card[1] == 'CLUBS') and random_card[0] == 13:
        club+=1
  
X=[]
if club > 0:
    percentages.append(np.round(club/simulation_number*100,2))
    X.append('CLUBS')
if spade > 0:
    percentages.append(np.round(spade/simulation_number*100,2))
    X.append('SPADE')
if diamond > 0:
    percentages.append(np.round(diamond/simulation_number*100,2))
    X.append('DIAMOND')
if heart > 0:
    percentages.append(np.round(heart/simulation_number*100,2))
    X.append('Heart')
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(X,percentages)
print(sum(percentages), '%')





















