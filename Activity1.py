# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:47:43 2018

@author: sanath
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dist(x,y):
    res=np.sqrt((x*x)+(y*y))
    return(res)
    
"""
def rad(lx,ly):
    res=np.sqrt((lx*lx)+(ly*ly))
    return(res)
"""
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





print("___Activity on Data Visualisation___")

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
print("\n")




print("Initial Plot of Customer Distribution")
plt.figure(1)
plt.scatter(x,y)
plt.show()
#since much of the data lies in the centre i.e 150/170 points lie at the centre therefore
#It would be better if we consider Median rather than mean ,since we have 20 outliers here
#Here in our case these outliers are far from the centre ,so we will consider Median
# Here if we consider even mean also it doesnot effect much ,since we have more points concentrated near centre
#Here iam considering median as the feature 
baseradius=dist(medianx,mediany)
print("Our New Base Location should be  X= ",medianx," Y=",mediany,",to gain max customers")   
print("\n")
custx=[]
custy=[]
clist=[]
temp=dist((medianx),(mediany))
print("Distance from initial location to New base location is",temp)
#myarr=[]
print("\n")
l=len(x)
ncust=np.arange(1,l+1)

for i in range(l):
    xa=x[i]
    ya=y[i]
    temp=dist((medianx-xa),(mediany-ya))
    if(temp<2):
        clist.append(i+1)
        custx.append(xa)
        custy.append(ya)

tcust=list(set(ncust)-set(clist))
tcust=sorted(tcust)
tcust=np.array(tcust)
tcustlen=len(tcust)


clist=np.array(clist)

custx=np.array(custx)
custy=np.array(custy)
#myarr=np.array(myarr)



df=pd.DataFrame(clist)
df.to_excel("Activity_1_Retain.xlsx", sheet_name='Retained Customers',index=False)

df=pd.DataFrame(tcust)
df.to_excel("Activity_1_Transfer.xlsx", sheet_name='Transferred Customers',index=False)


print("Retained Customers Graph")
plt.figure(2)
plt.scatter(custx,custy)
plt.show()

print("transferred Customers Plot")
tcustx=[]
tcusty=[]
for i in range(tcustlen):
    
    tcustx.append(x[tcust[i]-1])
    tcusty.append(y[tcust[i]-1])

plt.figure(3)
plt.scatter(tcustx,tcusty)
plt.show()



"""
                                    
#Manual removal of Outliers
ya=[]
yb=[]
#data Visualisation
#Here Iam removing the outliers Manually by visualisation from graph

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



plt.figure(3)
plt.scatter(ya,yb)
plt.show()
"""