# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 17:04:51 2018

@author: sanath
"""
#Gradient desccent without bias
#with theta0=0 and find out theta1
#2.3.1 exercise
#Basic Formula implementation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfs=pd.read_excel("Activity_2_Data.xlsx",sheetname="Sheet1")
x=np.array(dfs.iloc[0:,0])
y=np.array(dfs.iloc[0:,4])
print("original plot")
plt.figure(1)
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,y)
plt.show()

X=np.array(x)
Y=np.array(y)

count=0
theta0=0
theta1=150
init_theta1=theta1
m=len(X)
cost_J=0
alpha=0.0001
theta_prev=100


print("Learning rate is ",alpha) 
print("Number of data samples is",m)

count=0
while(np.abs(theta1-theta_prev)>0.001):
    cost_J=0
    for i in range(m):
        cost_J=cost_J+(((theta1*X[i])-Y[i])*X[i])
    count+=1
    temp=theta1-(alpha/m)*cost_J
    theta_prev=theta1
    theta1=temp
    

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


print("number of iterations took to converge is ",count)
test_x=float(input("Enter a test sample:"))
predicted_y=(test_x*theta1)+theta0
print ("theta0",theta0,"theta1",theta1)
print("Assumed theta1 ",init_theta1,"new theta1 is",theta1)

print ("The value of predicted y is",predicted_y)
print(" ")

print("Importance feature scaling ,here you can see that the number of iteration it took to calculate the theta0 and theta1 are ",count," iterations ,so here if we scale down the x and y values to certain range i.e by normalisation,we can reduce the number of iterations it took to calculate the theta0 and theta1 ,or the other way is to judge the random theta0 and theta1 values by seeing the plot which are very close to each other ,so by this also we can reduce the number of iterations and computing time of the program")






"""

for j in range(m):
    res_theta1=res_theta1+((theta0+theta1*x[j])-y[j])*x[j]
new_theta1=theta1-((alpha/m)*res_theta1)

print("Assumed Theta1 is ",theta1,"new Theta1 is",new_theta1)

hyp=[]
#hypothesis function
#predicting the values for different values of x
for ele in x:
    hyp.append(theta0+(new_theta1*ele))
hyp=np.array(hyp)
plt.figure(2)
plt.plot(x,y)
plt.plot(x,hyp)
plt.show()
    


"""


    
        
        


