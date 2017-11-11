#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:49:26 2017

@author: Krzysztof Stasiowski
WEAIiIB - Informatyka
WDI
liczenie liczb pierwszych metodą sita Eratostenesa
"""

import time
import math
import sys

def pierwsze(n):
    #deklaracja tablicy, pokazującej czy dana liczba jest pierwsza
    pierwsze = [False]*2 + [True]*(n-2)
    #Deklaracja tablicy do przechowywania końcowych liczb pierwszych 
    ppierwsze =[0]*n
    ppi=0;# licznik liczb pierwszych
    d=math.sqrt(n) #obliczenie pierwiastka z n, musimy sprawdzić jedynie liczbymniejsze od tego pierwiastka

    for (i,p) in enumerate(pierwsze):#przechodzimy przez listę liczbpierwszych (i - sprawdzana liczba, p - czy jest pierwsza)
        if(i>d):
            break #zakończenie sprawdzania jeżeli i > pierwiastka z n
        if(not p):
            continue # pominięcie jeśeli i nie jest liczbą pierwszą
        ppierwsze[ppi]=i #dodanie liczby pierwszej do listy liczb pierwszych
        ppi+=1;#zwiększenie licznika liczb pierwszych
        for delete in range(i*i,n,i):
            pierwsze[delete]=False#usunięcie wszyskich wielokrotności liczby pierwszej
        
    return ppierwsze[0:ppi] #zwracamy wszyskie liczby pierwsze


n = (int)(sys.argv[1]) #pobranie liczby sprawdzanych liczb jako argument programu

#pobieramy czas przed wykonaniem funkcji
start_time = time.time()
p=pierwsze(n)
print("{}   {}".format(n,((time.time() - start_time))))
#wyświetlamy różnicę czasu
