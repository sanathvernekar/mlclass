#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 14:52:23 2018

@author: sanath
"""



#ssd implementation for theta0=0 and alpha(learning rate=1)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfs=pd.read_excel("Activity_2_Data.xlsx",sheetname="Sheet1")
x=np.array(dfs.iloc[0:,0])
#x=[1,2,3,4,5]
y=np.array(dfs.iloc[0:,4])
#y=[1,2,3,4,5]
plt.figure(1)
plt.plot(x,y)
plt.show()

range_of_theta=[-10,10]
number_of_samples=50
theta=np.linspace(range_of_theta[0],range_of_theta[1],number_of_samples)
min_cost=999999
cost_array=[]
m=len(y)
for i in range(number_of_samples):
    cost_j=0
    
    for j in range(m):
        cost_j=cost_j+(theta[i]*x[j]-y[j])**2
    cost_j==1/(2.0*m)*cost_j
    cost_array.append(cost_j)
    
    
    if cost_j<min_cost:
        min_cost=cost_j
        theta_hyp = theta[i]
        index_min=i
h=[]
for i in range(m):
    h.append(theta_hyp*x[i])
    
plt.figure(1)
plt.plot(theta,cost_array)
plt.scatter(theta,cost_array)
plt.show()


plt.figure(2)
plt.plot(theta,cost_array,'g',theta_hyp,min_cost,'rd')
plt.show()

plt.figure(3)
print("Predicted curve vs actual curve")
plt.xlabel("X")
plt.ylabel("PREDECTED Y")
plt.plot(x,y)
#plt.scatter(x,y)
plt.plot(x,h)
plt.show()

test_x=float(input("Enter the test value for x :-"))
print("predicted  hyphothesis value is :-",test_x*theta_hyp)









    
        
        


