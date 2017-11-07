#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:49:26 2017

@author: shinigami
"""

import time
import math

def pierwsze(n):
   
    pierwsze = [False]*2 + [True]*(n-2)
    ppierwsze =[0]*n
    ppi=0;
    d=math.sqrt(n)

    for (i,p) in enumerate(pierwsze):
        if(i>d):
            break
        if(not p):
            continue
        ppierwsze[ppi]=i
        ppi+=1;
        for delete in range(i*i,n,i):
            pierwsze[delete]=False
    
    
    
    return ppierwsze[0:ppi]
    
    #zwracamy wszyskie liczby pierwsze


n = (int)(input())

#pobieramy czas praed wykonaniem funkcji
times = []
for i in range(2):
    start_time = time.time()
    p=pierwsze(n)
    times.append((time.time() - start_time))
    print(i)
    print(p)
print("--- {} sseconds ---".format(sum(times)/len(times)))
#wyświetlamy różnicę czasu