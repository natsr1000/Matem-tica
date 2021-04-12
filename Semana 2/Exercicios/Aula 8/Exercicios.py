# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:18:58 2021

@author: Miguel Correia
"""

"""
1.
a)
S={Heads,Tails}

b)
S= {1,2,3,4,5,6}

c)
S={(Heads,1),(Heads,2),(Heads,3),(Heads,4),(Heads,5),(Heads,6),(Tails,1),
   (Tails,2),(Tails,3),(Tails,4),(Tails,5),(Tails,6)}

2.
"""

import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=10000
happened=0
for i in range(sim_num):
    die=random.randint(1,6)
    if die==4:
        happened+=1
probability=np.round(((happened/sim_num)*100))
plt.bar(["4"],[probability])
plt.show()
print(probability,"%")

#4.
import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=10000
happened=0
event_types=[]
for i in range(sim_num):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    events=str(die1)+"+"+str(die2)
    events_reversed=str(die2)+"+"+str(die1)
    som=die1+die2
    if som>7 or som%2!=0:
        happened+=1
        if events not in event_types and events_reversed not in event_types:
            event_types.append(events)
        else:
            pass
probability=np.round(((happened/sim_num)*100))
plt.bar(["Sum of 2 dices being bigger than 7 or an odd number"],[probability])
plt.show()
event_types.sort()
print(event_types)
print(probability,"%")

#5 ? the even one of the one above.
import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=10000
happened=0
event_types=[]
for i in range(sim_num):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    events=str(die1)+"+"+str(die2)
    events_reversed=str(die2)+"+"+str(die1)
    som=die1+die2
    if som>7 or som%2==0:
        happened+=1
        if events not in event_types and events_reversed not in event_types:
            event_types.append(events)
        else:
            pass
probability=np.round(((happened/sim_num)*100))
plt.bar(["Sum of 2 dices being bigger than 7 or an even number"],[probability])
plt.show()
event_types.sort()
print(event_types)
print(probability,"%")

"""
s={(1+1,1+3,1+5),(2+2,2+4,2+6),(3+1,3+3,3+5,3+6),(4+2,4+4,4+5,4+6),
   (5+1,5+3,5+4,5+5,5+6),(6+2,6+3,6+4,6+5,6+6)}
This value is different because the possibilies of the sum of the two
dies being bigger than 7 or even is down by two, that is because it has
to be 7, an uneven number, and not bigger or equal than 7, the uneven sum
catching the times that it is 7 but not the even numbers

3.
"""

import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=10000
happened=0
for i in range(sim_num):
    coin1=random.randint(1,2)
    coin2=random.randint(1,2)
    #1 = heads, 2 = tails
    if coin1==1 and coin2==1:
        happened+=1
probability=np.round(((happened/sim_num)*100))
plt.bar(["Chance of two coins coming out as heads"],[probability])
print(probability,"%")


#Exercicio de pratica
#Uneven
import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=10000
happened=0
event_types=[]
for i in range(sim_num):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    events=str(die1)+"+"+str(die2)
    events_reversed=str(die2)+"+"+str(die1)
    som=die1+die2
    if som>6 or som%2!=0:
        happened+=1
        if events not in event_types and events_reversed not in event_types:
            event_types.append(events)
        else:
            pass
probability=np.round(((happened/sim_num)*100))
event_types.sort()
print(event_types)
print(probability,"%")


#even
import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=10000
happened=0
event_types=[]
for i in range(sim_num):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    events=str(die1)+"+"+str(die2)
    events_reversed=str(die2)+"+"+str(die1)
    som=die1+die2
    if som>6 or som%2==0:
        happened+=1
        if events not in event_types and events_reversed not in event_types:
            event_types.append(events)
        else:
            pass
probability=np.round(((happened/sim_num)*100))
event_types.sort()
print(event_types)
print(probability,"%")

#The even one has 1+6 and 5+1 which the uneven doesn't

#Probability of whichever number showing
import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=100000
happened={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
for i in range(sim_num):
    die=random.randint(1,6)
    happened[str(die)]+=1
probabilities={"1":0,"2":0,"3":0,"4":0,"5":0,"6":0}
for n in range(1,7):
    probabilities[str(n)]=np.round(((happened[str(n)]/sim_num)*100))
keys=probabilities.keys()
values=probabilities.values()
plt.bar(keys,values)
plt.show()


#soms

import numpy as np
import random
import matplotlib.pyplot as plt
sim_num=100000
soms={"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}
for i in range(sim_num):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    die_som=die1+die2
    soms[str(die_som)]+=1
probabilities={"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"10":0,"11":0,"12":0}
for n in range(2,13):
    probabilities[str(n)]=np.round(((soms[str(n)]/sim_num)*100))
keys=probabilities.keys()
values=probabilities.values()
plt.bar(keys,values)
plt.show()





















