# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 11:09:41 2017

@author: shinigami
padający śnieg
test : 11x7
true : XxY
odświeźanie 0.3s
"""
import time
import os
import random
random.seed()
refreshRate = 0.3
X = 80
Y = 18
tablica = [-1];


def display():
    for y in range(Y):
        for x in range(X):
            if(tablica[x] == y):
                print("o", end='')
            print(".", end='')
        print()

def randomDrop():
    tablica.insert(0,random.randint(0,X-1))
    tablica.pop()
    
while( True ):
    randomDrop()
    display()
    time.sleep(refreshRate)
    os.system('clear');


