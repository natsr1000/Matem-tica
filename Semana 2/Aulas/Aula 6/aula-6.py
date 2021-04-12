# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 08:56:54 2021

@author: Miguel Correia
"""

#semilog y
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,10)
y=x
plt.plot(x,y,"-r",label="y=x")
plt.grid()
plt.show()

plt.plot(x,y,label="y=x")
plt.semilogy()
plt.show()

#semilog x
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,10)
y=x
plt.plot(x,y,"-r",label="y=x")
plt.grid()
plt.show()

plt.plot(x,y,label="y=x")
plt.semilogx()
plt.show()

#both
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,10)
y=x
plt.plot(x,y,"-r",label="y=x")
plt.grid()
plt.show()

plt.plot(x,y,label="y=x")
plt.yscale('log')
plt.xscale('log')
plt.grid()
plt.show()

#Consider the data (slide 12)
import matplotlib.pyplot as plt
import numpy as np
x=[2,30,70,100,150]
y=[4.24,16.4,25.1,30.0,36.7]
plt.plot(x,y,"o")
plt.show()

logx=np.log10(x)
logy=np.log10(y)
print(np.poly1d(np.polyfit(logx,logy,1)))
plt.plot(logx,logy,'o')
plt.show()

#slide 11

"""
find the n and A

n=(log(y2) - log(y1))/(log(x2)-log(x1))

exemplo
log(A)=0.5 == A=10**0.5
"""




















