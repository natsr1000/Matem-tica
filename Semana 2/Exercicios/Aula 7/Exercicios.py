# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:53:47 2021

@author: Miguel Correia
"""

#Statistics
#1.
import numpy as np
data=[4,7,2,9,12,2,20,10,5,9]
data.sort()
if len(data)%2!=0:
    median=data[(int(len(data)/2))]
else:
    median=(((data[int(np.round(len(data)/2))]+data[(int(np.round(len(data)/2))-1)]))/2)
print("The median is {}".format(median))


#ou entao pada calcular a mediana...
median = np.median(data)
print("The median is {}".format(median))


quartile_div=len(data)/3
if (np.round(quartile_div)*3)!=len(data):
    q1=data[:int(np.round(quartile_div))]
    q2=data[int(np.round(quartile_div)):int((np.round(quartile_div)*2)+1)]
    q3=data[int((np.round(quartile_div)*2)+1):]
else:
    q1=data[:int(np.round(quartile_div))]
    q2=data[int(np.round(quartile_div)):int((np.round(quartile_div)*2))]
    q3=data[int((np.round(quartile_div)*2)):]
x025=(q1[0]+q1[2])/2
x075=(q3[0]+q3[1])/2
x05=x075-x025
print("The quartiles are",q1,q2,q3,"with a lower range of",x025,"an upper range of",x075,"and an inner-quartile range of",x05)

#2.
import numpy as np
xi=[2,5,10,11]
s=0
for n in xi:
    s+=n
mean=s/len(xi)
#or...
mean=np.mean(xi)
print("The mean is",mean)
var_up_sum=0
for n in xi:
    var_up_sum+=((n-mean)**2)
variance=var_up_sum/(len(xi)-1)
print("With a variance of",variance)
std=np.sqrt(variance)
print("And a standard deviation of",std)

#3.
data=[4,1,2,1,3,2,1,1]
data.sort()
try:
    median=data[(int(len(data)/2))]
except:
    median=(data[int(np.round(len(data)/2))]+data[(int(np.round(len(data)/2))+1)])/2
print("The median is {}".format(median))

#4.
import numpy as np
mean=np.mean(data)
var_up_sum=0
for n in data:
    var_up_sum+=((n-mean)**2)
variance=var_up_sum/(len(data)-1)
std=np.sqrt(variance)
print("The standard deviation is",std)

#Calculate Portugal's mode, median, variance and standard deviation for
#boys and girls over the years for 4 countries

B_AUS=[527.0,527.0,519.0,510.1,497.0,494.0]
G_AUS=[522.0,513.0,509.0,497.82,491.0,488.0]
B_CAN=[541.0,534.0,533.0,523.2,520.0,514.0]
G_CAN=[530.0,520.0,521.0,513.02,511.0,510.0]
B_CZK=[524.0,514.0,495.0,504.7,496.0,501.0]
G_CZK=[509.0,504.0,490.0,492.9,489.0,498.0]
B_POR=[472.0,474.0,493.0,492.7,497.0,497.0]
G_POR=[460.0,459.0,481.0,481.3,487.0,488.0]

def meadian(data):
    try:
        median=data[(int(len(data)/2))]
    except:
        median=(data[int(np.round(len(data)/2))]+data[(int(np.round(len(data)/2))+1)])/2
    return median

def mode(data):
    all_mode=dict()
    for i in data:
        if str(i) not in all_mode.keys():
            all_mode[str(i)]=1
        else:
            all_mode[str(i)]+=1
    M_times=1
    mode=[]
    for i in all_mode.items():
        if i[1]>=M_times:
            if M_times==i[1]:
                mode.append(float(i[0]))
            else:
                M_times=i[1]
                mode=[float(i[0])]
        else:
            pass
    if M_times==1:
        mode="no mode"
    else:
        pass
    return mode

def variance(data):
    mean=np.mean(data)
    var_up_sum=0
    for i in data:
        var_up_sum+=((i-mean)**2)
    variance=var_up_sum/(len(data)-1)
    return variance

import numpy as np
B_AUS_data={'gender':'boys','country':'Australia','mode':mode(B_AUS),'median':meadian(B_AUS),'variance':variance(B_AUS),'standard deviation':np.sqrt(variance(B_AUS))}
G_AUS_data={'gender':'girls','country':'Australia','mode':mode(G_AUS),'median':meadian(G_AUS),'variance':variance(G_AUS),'standard deviation':np.sqrt(variance(G_AUS))}
B_CAN_data={'gender':'boys','country':'Canada','mode':mode(B_CAN),'median':meadian(B_CAN),'variance':variance(B_CAN),'standard deviation':np.sqrt(variance(B_CAN))}
G_CAN_data={'gender':'girls','country':'Canada','mode':mode(G_CAN),'median':meadian(G_CAN),'variance':variance(G_CAN),'standard deviation':np.sqrt(variance(G_CAN))}
B_CZK_data={'gender':'boys','country':'Czech Republic','mode':mode(B_CZK),'median':meadian(B_CZK),'variance':variance(B_CZK),'standard deviation':np.sqrt(variance(B_CZK))}
G_CZK_data={'gender':'girls','country':'Czech Republic','mode':mode(G_CZK),'median':meadian(G_CZK),'variance':variance(G_CZK),'standard deviation':np.sqrt(variance(G_CZK))}
B_POR_data={'gender':'boys','country':'Portugal','mode':mode(B_POR),'median':meadian(B_POR),'variance':variance(B_POR),'standard deviation':np.sqrt(variance(B_POR))}
G_POR_data={'gender':'girls','country':'Portugal','mode':mode(G_POR),'median':meadian(G_POR),'variance':variance(G_POR),'standard deviation':np.sqrt(variance(G_POR))}
all_data=[B_AUS_data,G_AUS_data,B_CAN_data,G_CAN_data,B_CZK_data,G_CZK_data,B_POR_data,G_POR_data]

for data in all_data:
    if type(data['mode'])=='string':
        print("In",data['country'],"the",data['gender'],"math scores have",data['mode'],',',data['median'],'of median, {variance:.2f} of variance, and {std:.2f} of standard deviation\n'.format(variance=data['variance'],std=data['standard deviation']))
    elif len(data['mode'])==1:
        print("In",data['country'],"the",data['gender'],"math scores have",data['mode'][0],'of mode,',data['median'],'of median, {variance:.2f} of variance, and {std:.2f} of standard deviation\n'.format(variance=data['variance'],std=data['standard deviation']))
    else:
        print("In",data['country'],"the",data['gender'],"math scores have",data['mode'],',',data['median'],'of median, {variance:.2f} of variance, and {std:.2f} of standard deviation\n'.format(variance=data['variance'],std=data['standard deviation']))

























