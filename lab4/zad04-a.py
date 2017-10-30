#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:29:45 2017

@author: shinigami
"""
import time

def rek(n):
    if(n==0 or n==1):
        return 1;
    
    return n*rek(n-1)
    
def itera(n):
    i=1
    
    if(n>0):
        for j in range(1,n+1):
            i*=j
    return i

n = (int)(input())
old = time.clock()
r = rek(n)
print("rekurenc n={} n!={} czas={}".format(n,r,(time.clock()-old)));
old = time.clock()
i = itera(n)
print("iteracyjn n={} n!={} czas={}".format(n,i,(time.clock()-old)));