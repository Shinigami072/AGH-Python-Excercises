# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:09:41 2017

@author: shinigami
padający śnieg
odświeźanie 0.3s
"""
import time
import os
import random
refreshRate = 0.3 #co ile odświeżamy
X = 80 #wymiar X
Y = 23 #wymiar Y
tablica = [-1]; #gdzie znajdująsię krople


def display():
    for y in range(Y): #przechodzimy przez kolejne rzędy
        for x in range(X): #i kolejne komórki w nich
            if(x in tablica and tablica.index(x) == y): #jeśli w naszej tablicu znajdziemy x i jego pozycja odpowiada y
                print("o", end='')
            else:
                print(".", end='')
        print()
    
        

def randomDrop():
    d = tablica[0];# pobieramy element z tablicy
    while(d in tablica):
        d = random.randint(0,X-1) #znajdz mijsce nie zajęte przez kroplę
   
    tablica.insert(0,d)    
    if(len(tablica) > Y):
        tablica.pop() # usuń kroplę, poza widokiem

random.seed()# ustawiamy generator liczb losowych
while( True ):
    randomDrop()#losjemy nową kroplę
    display()#wyświetl klatę deszczu
    time.sleep(refreshRate)#poczekaj
    os.system('clear');#wyczyść terminal


