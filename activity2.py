# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:47:43 2018

@author: sanath
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def rad(lx,ly):
    res=np.sqrt((lx*lx)+(ly*ly))
    return(res)

def mode(arr) :
    try:
        res=max(arr, key = arr.count)
        return(res)
    except:
        return None
#reading data

dfs=pd.read_excel("Activity_1_Data.xlsx",sheetname="Sheet1")
x=np.array(dfs.iloc[0:,1])
#print(len(x))
y=np.array(dfs.iloc[0:,2])
#print(len(y))
print("Before removal of outliers")
print("_________#####_____________")


meanx=np.mean(x)
print("Mean of x data",meanx)
meany=np.mean(y)
print("Mean of Y data ",meany)
print("_________#####_____________")
medianx=np.median(x)
print("Median of X data",medianx)
mediany=np.median(y)
print("Median of Y data",mediany)
print("_________#####_____________")
mx=list(x)
modex=mode(mx)
print("Mode of X data",modex)
my=list(y)
modey=mode(my)
print("Mode of X data",modey)
print("_________#####_____________")
stdx=np.std(x)
print("Standard deviation of X is",stdx)
print("Variance of X is ",stdx*stdx)
stdy=np.std(y)
print("Standard deviation of Y is ",stdy)
print("Variance of Y is ",stdy*stdy)
print("_________#####_____________")
print("\n \n ")


plt.figure(1)
plt.scatter(x,y)
plt.show()

myarr=[]
l=len(x)
for i in range(l):
    lx=x[i]
    ly=y[i]
    g=rad(lx,ly)
    myarr.append(g)




basepoint=rad(medianx,mediany)
print("Our New Base Location is ",medianx,mediany)   
cust=[]


ya=[]
yb=[]
#data Visualisation
#Here Iam removing the outliers Manually by visualisation from graph
myarr=np.array(myarr)
for i in range(l):
    if(x[i]<4 and x[i] >0 and y[i] <4 and y[i]>0 ) :
        ya.append(x[i])
        yb.append(y[i])
# If needed
print("After removal of outliers")

meanx1=np.mean(ya)
print("Mean of X after removal of outliers",meanx)
meany1=np.mean(yb)
print("Mean of Y after removal of outliers",meany)
print("_________#####_____________")

medianx1=np.median(ya)
print("Median of X after removal of outliers",medianx)
mediany1=np.median(yb)
print("Median of Y after removal of outliers",mediany)



#since much of the data lies in the centre i.e 150/170 points lie at the centre therefore
#It would be better if we consider Median rather than mean ,since we have 20 outliers here
#Here in our case these outliers are far from the centre ,so we will consider Median






plt.figure(2)
plt.scatter(ya,yb)
plt.show()