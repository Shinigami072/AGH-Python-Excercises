#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:49:26 2017

@author: shinigami
"""

import time
import math

def pierwsze(n):
   
    #jeżeli n<2 brak liczb pierwszych
    if(n<2)
        return [];
    
    pierwsze = [2]
    
    #sprawdzamy czy liczby od 2 - n są liczbami pierwszymi
    for possiblePrime in range(max(pierwsze),n+1):
        
        #sprawdzamy czy możliwa liczba pierwsza jest podzielna przez którąkolwiek z 
        #juz wyznaczonych liczb pierwszych
        isPrime = True
        for d in pierwsze:
            if(possiblePrime%d == 0):
               isPrime=False;
               #wprzypadku gdy jest podzielna przerywamy wykonywanie pętli
               break
           
        if(isPrime):#Jeżeli jest pierwsza dodajemy ją do wyznaczonych liczb pierwszych
            pierwsze.append(possiblePrime)
            
    #zwracamy wszyskie liczby pierwsze
    return pierwsze


n = (int)(input())

#pobieramy czas praed wykonaniem funkcji
start_time = time.time()
pierwsze(n)
print("--- {} sseconds ---".format((time.time() - start_time)))
#wyświetlamy różnicę czasu