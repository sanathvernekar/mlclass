# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 18:45:01 2018

@author: sanath
"""

import math

def mean(arr,n):
    
    result=sum(arr)/n
    return result
def standard_deviation(arr,n):
    u=mean(arr,n)
    temp=0
    for i in range(n):
        temp=temp+((arr[i]-u)**2)
    temp=temp/n
    result=math.sqrt(temp)
        
    return result
n=int(input())
arr=[int(x) for x in input().split()]
print("{0:.1f}".format(standard_deviation(arr,n)))
