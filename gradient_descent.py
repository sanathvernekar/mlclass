# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 13:59:57 2018

@author: sanath
"""
#single dimension
#single straight line
import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

dfs=pd.read_excel("Activity_2_Data.xlsx",sheetname="Sheet1")
x=np.array(dfs.iloc[0:,0])
y=np.array(dfs.iloc[0:,1])
plt.figure(1)
plt.plot(x,y)
plt.show()

alpha=0.00001
theta0=1
new_theta0=1
theta1=10
new_theta1=10
m=len(x)
res=0
res_theta1=0
print("Learning rate is ",alpha) 
print("Number of samples or data is",m)
#
for j in range(m):
    res=res+((theta0+theta1*x[j])-y[j])
new_theta0=theta0-((alpha/m)*(res))
print("Assumed Theta0 is ",theta0," New theta1 is",new_theta0 )

for j in range(m):
    res_theta1=res_theta1+((theta0+theta1*x[j])-y[j])*x[j]
new_theta1=theta1-((alpha/m)*res_theta1)

print("Assumed Theta1 is ",theta1,"new theta1 is",new_theta1)




    
        
        


