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
tablica = [];
for y in range(Y):
    tablica.append(list(" "*X))

def display():
    global tablica
    global X
    global Y
    for y in range(Y):
        print("".join(tablica[y]))
    print("\n");
def randomDrop():
    global tablica
    global X
    global Y
    tablica[0][random.randint(0,X-1)]='x'
def downOne():
    global tablica
    global X
    global Y
    tablica.insert(0,list(" "*X))
    tablica.pop(Y)
    
while( True ):
    downOne()
    randomDrop()
    display()
    time.sleep(refreshRate)
    os.system('clear');

