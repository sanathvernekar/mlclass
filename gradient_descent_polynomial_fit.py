# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 14:32:30 2018

@author: sanath
"""
#implementation of gradient descent to fit multi order curve
#To know the importance of fitting polynomial fit to the data

import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

#dfs=pd.read_excel("Activity_2_Data.xlsx",sheetname="Sheet1")
#x=np.array(dfs.iloc[0:,0])
x=[0,1,2,3,4,5,6,7,8]
#y=np.array(dfs.iloc[0:,4])
y=[0,1,4,9,16,25,36,49,64]
plt.figure(1)
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y)
plt.show()
X=np.array(x)
Y=np.array(y)
m=len(X)
alpha=0.000001

print("Learning rate is ",alpha) 
print("Number of samples or data is",m)
count=0
theta0=1
init_theta0=theta0
theta1=2
init_theta1=theta1
theta2=1
init_theta2=theta2
m=len(X)
theta0_prev=100
theta1_prev=100
theta2_prev=100
while(True):
    cost_J0=0    
    cost_J1=0
    cost_J2=0
    for i in range(m):
        h_x=theta0+theta1*X[i]+theta2*X[i]
        cost_J0=cost_J0+(h_x-Y[i])
        cost_J1=cost_J1+((h_x-Y[i])*X[i])
        cost_J2=cost_J2+((h_x-Y[i])*X[i]*X[i])
        
    count+=1
    #uncomment to see variation of theta
    print("iteration",count,"theta0",theta0,"theta1",theta1,"theta2",theta2)
    
    
    
    temp0=theta0-((alpha*cost_J0)/m)
    temp1=theta1-((alpha/m)*cost_J1)
    temp2=theta2-((alpha/m)*cost_J2)
    
    if((np.abs(temp0-theta0)<0.00001)and(np.abs(temp1-theta1)<0.00001) and (np.abs(temp2-theta2)<0.00001)):
      break
    theta0=temp0
    theta1=temp1
    theta2=temp2


h=[]
for i in range(m):
    h.append(theta1*X[i]+theta0+theta2*(X[i]**2))
    
    
h=np.array(h)
plt.figure(2)
plt.xlabel("X")
plt.ylabel("Hypothesis")
plt.plot(X,Y)
plt.plot(X,h)   
plt.show()

print ("Assumed theta0 is ",init_theta0,"predicted theta0 is ",theta0)
print("Assumed theta1 is ",init_theta1,"predicted theta1 is ",theta1)
print("Assumed theta2 is ",init_theta2,"predicted theta2 is ",theta2)
test_x=float(input("Enter a test sample:"))
predicted_y=(test_x*theta1)+theta0+(test_x*test_x*theta2)
#implementation of gradient descent for 1 st order curve(straight line)

print ("The value of predicted y is",predicted_y)

#print("Importance feature scaling ,here you can see that the number of iteration it took to calculate the theta0 and theta1 are ",count," iterations ,so here if we scale down the x and y values to certain range i.e by normalisation,we can reduce the number of iterations it took to calculate the theta0 and theta1 ,or the other way is to judge the random theta0 and theta1 values by seeing the plot which are very close to each other ,so by this also we can reduce the number of iterations and computing time of the program")













