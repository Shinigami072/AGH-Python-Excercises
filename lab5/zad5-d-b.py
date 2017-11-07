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
    d = max(pierwsze)
    for p in pierwsze:
        #wykreślamy wszystkie wielokrotności danej liczby
         while(p<d):
             p+=p
             if(p>d):
                 break
             if(not p in pierwsze):
                 continue
             pierwsze.remove(p)
       
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