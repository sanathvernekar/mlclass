# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 17:17:17 2018

@author: sanath
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfs=pd.read_excel("Activity_2_Data.xlsx",sheetname="Sheet1")
x=np.array(dfs.iloc[0:,0])
y=np.array(dfs.iloc[0:,4])
plt.figure(1)
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x,y)
plt.show()

m=len(x)

X=np.array(x)
Y=np.array(y)


theta0=100
init_theta0=theta0
theta1=25
init_theta1=theta1
m=len(X)
alpha=0.0001

print("Learning rate is ",alpha) 
print("Number of samples or data is",m)
count=0
while(True):
    cost_J0=0    
    cost_J1=0
    for i in range(m):
        h_x=theta0+theta1*X[i]
        cost_J0=cost_J0+(h_x-Y[i])
        cost_J1=cost_J1+((h_x-Y[i])*X[i])
        
    count+=1
    #uncomment to see variation of theta
    #print("iteration",count,"theta0",theta0,"theta1",theta1)
    
    
    
    temp0=theta0-((alpha*cost_J0)/m)
    temp1=theta1-((alpha/m)*cost_J1)
    
    if((np.abs(temp0-theta0)<0.00001)and(np.abs(temp1-theta1)<0.00001)):
      break
    theta0=temp0
    theta1=temp1

h=[]
for i in range(m):
    h.append(theta1*X[i]+theta0)
    
h=np.array(h)
plt.figure(2)
plt.xlabel("X")
plt.ylabel("Hypothesis")
plt.plot(X,Y)
plt.plot(X,h)   
plt.show()




print ("Assumed theta0 is ",init_theta0,"predicted theta0 is ",theta0)
print("Assumed theta1 is ",init_theta1,"predicted theta1 is ",theta1)
test_x=float(input("Enter a test sample:"))
predicted_y=(test_x*theta1)+theta0
#implementation of gradient descent for 1 st order curve(straight line)

print ("The value of predicted y is",predicted_y)

print("Importance feature scaling ,here you can see that the number of iteration it took to calculate the theta0 and theta1 are ",count," iterations ,so here if we scale down the x and y values to certain range i.e by normalisation,we can reduce the number of iterations it took to calculate the theta0 and theta1 ,or the other way is to judge the random theta0 and theta1 values by seeing the plot which are very close to each other ,so by this also we can reduce the number of iterations and computing time of the program")



















"""

#dummy code (test code)
theta0=4
theta1=3
m=len(X)
alpha=0.001

while(True):
    cost_J0=0    
    cost_J1=0
    for i in range(m):
        h_x=theta0+theta1*X[i]
        cost_J0=cost_J0+(h_x-Y[i])
        cost_J1=cost_J1+((h_x-Y[i])*X[i])
        
    temp0=theta0-((alpha*cost_J0)/m)
    temp1=theta1-((alpha/m)*cost_J1)
    
    if((np.abs(temp0-theta0)<0.01)and(np.abs(temp1-theta1)<0.01)):
      break
    theta0=temp0
    theta1=temp1

h=[]
for i in range(m):
    h.append(theta1*X[i]+theta0)
    
h=np.array(h)
plt.xlabel("X")
plt.ylabel("Hypothesis")
plt.plot(X,h)
    
print ("theta0={0}  theta1={1}").format(theta0,theta1)


test_x=input("Enter a test sample:" )
predicted_y=(test_x*theta1)+theta0

print ("The value of predicted y is"),predicted_y
"""


"""
#
for j in range(m):
    res=res+((theta0+theta1*x[j])-y[j])
new_theta0=theta0-((alpha/m)*(res))
print("Assumed Theta0 is ",theta0," New theta1 is",new_theta0 )

for j in range(m):
    res_theta1=res_theta1+((theta0+theta1*x[j])-y[j])*x[j]
new_theta1=theta1-((alpha/m)*res_theta1)

print("Assumed Theta1 is ",theta1,"new theta1 is",new_theta1)




hyp=[]
for ele in x:
    hyp.append((new_theta0+(new_theta1*ele)))
hyp=np.array(hyp)
plt.figure(2)
plt.plot(x,y)
plt.plot(x,hyp)
plt.show()
"""

