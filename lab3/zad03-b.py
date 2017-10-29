#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:46:40 2017

@author: shinigami
"""

import time
import os
import random

refreshRate = 0.3 #Odświeżanie

X = 79 #wymiary terminala
Y = 21
cX = ((X-1)//2)# - środkowy x
cY = ((Y-1)//2)# - środkowy y

bok =1; #wielkość obecnego boku/2

maxBok =min((X-1)//2,(Y-1)//2); #maksymalna wielkość boku /2

kierunek =True # True - rośniemy, False - malejemy

random.seed()
while(True):
    
    for y in range(Y):
        for x in range(X):#przechodzimy przezkażdy punkt (x,y) i wypełniamy go odpowiednim znakiem
            #max(a,b) - większa z a i b
            # abs(a) - modół z a
            # abs(cX-x) - odległość x od środkowego X
            #odległość punktu (x,y) od środka == bok
            if max(( abs(cX-x), abs(cY-y) )) == bok:  
                print('█', end='')
            else:
                print(' ', end='')
        print()#przechdzimy do kolejnego rzędu
        
    print()
    
    if(kierunek):#zwiększenie/ zmniejszenie boku
        bok+=1
    else:
        bok-=1
        
    if(bok-1 <0 or bok+1>maxBok):# sprawdzenie czy powinniśmy zmienić kierunek
        kierunek=not kierunek
        
    time.sleep(refreshRate) #czekanie na odświerzenie
    os.system('clear');
