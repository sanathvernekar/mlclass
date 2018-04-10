#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 14:33:05 2018

@author: sanath
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:54:34 2018

@author: sanath
"""

#using the formula method
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#fit 1st order curve for x and y

#fit 1 st order straight line
#based on formula method 

def a1(x,y):
    x=np.array(x)
    y=np.array(y)
    val=((len(x)*sum(x*y))-(sum(x)*sum(y)))/((len(x)*sum(x*x))-(sum(x)*sum(x)))
    return(val)
def a0(x,y,res_a1):
    x=np.array(x)
    y=np.array(y)
    val=(sum(y)/len(y))-((res_a1*sum(x))/len(x))
    return(val)
    
   
#n=int(input("Enter number of variables in X "))
#x = [float(x) for x in input().split()]
#y = [float(x) for x in input().split()]



dfs=pd.read_excel("Activity_2_Data.xlsx",sheetname="Sheet1")
x=np.array(dfs.iloc[0:,0])
#print(x)


#print(len(x))
y=np.array(dfs.iloc[0:,4])
#print(y)
#print(len(y))


plt.plot(x,y)
plt.show()

xlen=len(x)
ylen=len(y)
plt.figure(1)
plt.plot(x,y)
plt.show()
if xlen!=ylen:
    print("Enter equal number of samples for both x and y")
    quit()
res_a1=a1(y,x)
res_a0=a0(x,y,res_a1)
print("y =",res_a0,'+',res_a1,'x')


x_new=np.arange(1,101)
#print(x_new)
y_new=[]

for ele in x_new:
    #print(ele)
    #print(res_a0+(res_a1*ele))
    y_new.append(res_a0+(res_a1*ele))
#print(y_new)
plt.figure(2)
plt.plot(x,y)
plt.plot(x_new,y_new)
plt.show()

pred_x=float(input("Enter the value to be predicted:- "))
pred_y=(res_a0+(res_a1*pred_x))
print("Predicted value for ",pred_x," is ", pred_y)

"""
x=np.array(x)
y=np.array(y)
x_first=[]
for i in range(xlen):
    x_first.append(res_a0+(res_a1*x[i]))
x_first=np.array(x_first)
    
plt.figure(2)
plt.plot(y,x_first)
plt.show()

"""  
