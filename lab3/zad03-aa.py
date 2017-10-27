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
random.seed()
refreshRate = 0.3
X = 17
Y = 7
tablica = [-1];


def display():
    for y in range(Y):
        for x in range(X):
            if(x in tablica and tablica.index(x) == y):
                print("o", end='')
            else:
                print(".", end='')
        print()
    
        

def randomDrop():
    d = tablica[0];
    while(d in tablica):
        d = random.randint(0,X-1) #znajdz mijsce nie zajęte przez kroplę
   
    tablica.insert(0,d)    
    if(len(tablica) > Y):
        tablica.pop() # usuń kroplę, poza widokiem
    
while( True ):
    randomDrop()
    display()
    time.sleep(refreshRate)
    os.system('clear');


