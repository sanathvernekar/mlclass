#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:08:05 2018

@author: sanath
"""
#fit second order curve
#based on matrix method

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfs=pd.read_excel("Activity_2_Data.xlsx",sheetname="Sheet1")
x=np.array(dfs.iloc[0:,0])
#print(x)


#print(len(x))
y=np.array(dfs.iloc[0:,4])
#print(y)
#print(len(y))
print("original plot")
plt.figure(1)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)
plt.show()
p=[[len(x),sum(x),sum(x*x)],[sum(x),sum(x*x),sum(x*x*x)],[sum(x*x),sum(x*x*x),sum(x*x*x*x)]]
r=[sum(y),sum(x*y),sum(x*x*y)]
q=np.linalg.solve(p,r)
c=q[0]
m=q[1]
g=q[2]


x_new=np.arange(1,101)
y_new=[]
for ele in x_new:
    y_new.append(c+(m*ele)+(g*ele*ele))
print("Second order curve for the given plot")
plt.figure(2)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)
plt.plot(x_new,y_new)
plt.show()

pred_x=float(input("Enter the value to be predicted:- "))
pred_y=(c+(m*pred_x)+(g*pred_x*pred_x))
print("Theta0",c,"theta1",m,"theta2",g)
print("Predicted value for ",pred_x," is ", pred_y)
#compared to 1st order fit the second order curve fits for this curve
