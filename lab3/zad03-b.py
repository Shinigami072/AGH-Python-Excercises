#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:46:40 2017

@author: shinigami
"""

import time
import os
import random
random.seed()
refreshRate = 0.3
X = 79
Y = 21
krok =1;
maxkrok =min((X-1)//2,(Y-1)//2);
kierunek =True
while(True):
    for y in range(Y):
        for x in range(X):
            if max(( abs(((X-1)//2)-x), abs(((Y-1)//2)-y) ))== krok:
                print('█', end='')
            else:
                print(' ', end='')
        print()
    print()
    
    if(kierunek):
        krok+=1
    else:
        krok-=1
    if(krok-1 <0 or krok+1>maxkrok):
        kierunek=not kierunek
    time.sleep(refreshRate)
    os.system('clear');
