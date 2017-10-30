# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:29:45 2017

@author: shinigami
"""
import time

def rek(n):
    if(n==0):
        return 0;
    if(n==1):
        return 1;
    
    return rek(n-2)+rek(n-1)
    
def itera(n):
    if(n==0):
        return 0;
    if(n==1):
        return 1;
    
    a=0
    b=1
    
    for j in range(1,n):
        c=b
        b=a+b
        a=c
    return b

n = (int)(input())
old = time.clock()
r = rek(n)
print("rekurenc n={} n!={} czas={}".format(n,r,(time.clock()-old)));
old = time.clock()
i = itera(n)
print("iteracyjn n={} n!={} czas={}".format(n,i,(time.clock()-old)));