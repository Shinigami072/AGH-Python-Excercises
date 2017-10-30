#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:57:05 2017

@author: shinigami
"""
import math

def pascal(n):
    if(n==1):
        print("1")
        return [1]
    if(n ==2):
        pascal(n-1)
        print("1 1")
        return [1,1]
    
    b = pascal(n-1)
    c = [1,1]
    for i in range(1,len(b)):
        c.insert(1,b[i]+b[i-1])
    for i in c:
        print(i,end=" ")
    print()
    return c

    
i = (int)(input())
pascal(i)