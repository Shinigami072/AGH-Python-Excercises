#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:49:26 2017

@author: shinigami
"""

import time
import math

def pierwsze(n):
   
    pierwsze = list(range(2,n+1));
    
    for p in range(2,(int)(math.ceil(math.sqrt(n)))):
        if(pierwsze[p-2] != 0):
            for j in range(p*p,n,p):
                pierwsze[j-2]=0
    for p in  range(len(pierwsze),0):
        if(pierwsze[p]!=0 or pierwsze[p]!=0):
            pierwsze.pop(p)
        
    return pierwsze
    
    #zwracamy wszyskie liczby pierwsze


n = (int)(input())

#pobieramy czas praed wykonaniem funkcji
times = []
for i in range(2):
    start_time = time.time()
    pierwsze(n)
    times.append((time.time() - start_time))
    print(i)
    
print("--- {} sseconds ---".format(sum(times)/len(times)))
#wyświetlamy różnicę czasu