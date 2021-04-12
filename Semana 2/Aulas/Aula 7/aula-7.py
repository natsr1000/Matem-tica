# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 08:44:56 2021

@author: Miguel Correia
"""

#Geometric mean
import numpy as np
data=[7.0,8.0,8.5]
geo_mean=(7*8*8.5)**(1/(len(data)))
print(geo_mean)

#Variace
var2=(((7-7.83)**2)+((8-7.83)**2)+((8.5-7.83)**2))/(3-1)
var=np.sqrt(var2)
print(var)

#example 2
data=[10,30,50]
mean=((10+30+50)/3)
var2=(((data[0]-mean)**2)+((data[1]-mean)**2)+((data[2]-mean)**2))/(len(data)-1)
var=np.sqrt(var2)
print(var)

#Standart deviation

#sd=sqrt(variance)

var=20
sd=np.sqrt(20)
print(sd)

#Quartile
data=[3, 6, 7, 11, 13, 22, 30, 40, 44, 50, 52, 61, 68, 80, 94]
q1=11
q2=40
q3=61
q4=90
import pandas as pd
df=pd.DataFrame(data)
print(df.describe())
print(df.quantile(0.5)) #50% quartile
quartiles=pd.qcut(data,3)
print(quartiles)



#Sampling

#Random sample
import random
Sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("With list:", random.sample(Sample, 5)) 

#Systematic sample
import numpy as np
systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
step = 2
print(np.mean(sample))
size = int(len(sample)/step)
for i in range(0,size):
    systematic_sample.append(sample[i*step])
print(systematic_sample)
systematic_mean = np.mean(systematic_sample)
print(systematic_mean)

#Or
import numpy as np
systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
step = 2
for i in range(0,15,step):
    systematic_sample.append(sample[i])
print(systematic_sample)
systematic_mean=np.mean(systematic_sample)
print(systematic_mean)

#Cluster sample
systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
step = 3
print(np.mean(sample))
size = int(len(sample)/step)
for i in range(0,size):
    systematic_sample.append(sample[i*step])
    systematic_sample.append(sample[i*step]+1)
systematic_mean = np.mean(systematic_sample)
print(systematic_mean)

#Stratified sample
import random 
import numpy as np
def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] for i in range(wanted_parts) ]
systematic_sample = []
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14, 15]
A, B, C = split_list(sample, 3)
total= split_list(sample, 3)
stratified_list =[]
print('mean all values:', np.mean(sample) )
splited_list = [A, B, C]
for i in range(0,len(splited_list)):
    stratified_list.append(splited_list[i][random.randint(0,4)])
systematic_mean = np.mean(stratified_list)
print('stratified mean', systematic_mean)


#Scipy

import numpy as np
from scipy import stats
from scipy.stats import gmean
from scipy.stats import hmean
import random
numbers = [ 1, 1, 2, 2, 3, 3, 4, 1, 2 ]
print(numbers)
Mean = np.mean(numbers)
Median = np.median(numbers)
Mode = int(stats.mode(numbers)[0]) # index 1 gives frequency
print("Mean = ", Mean, "\nMedian = ", Median, "\nMode = ", Mode)
Geometric_Mean = gmean(numbers)
Harmonic_mean = hmean(numbers)
print("Geometric Mean = ", Geometric_Mean, "\nHarmonic Mean = ",
Harmonic_mean)
Variance = np.var(numbers)
Standard_Deviation = np.std(numbers)
print("Variance = ", Variance, "\nStandard deviation = ",
Standard_Deviation)
Q1 = np.percentile(numbers, 25)
Q2 = np.percentile(numbers, 50)
Q3 = np.percentile(numbers, 75)
print("Q1 = ", Q1, "\nQ2 = ", Q2, "\nQ3 = ", Q3) # 1 1 1 2 2 2 3 3 




























