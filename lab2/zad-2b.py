#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:38:17 2017

@author: shinigami
"""

cyfry = "0123456789abcdef";
def zam10NaSystem(system,numer):
    global cyfry
    wynik = ""
    
    while( numer > 0):
        wynik=(cyfry[numer%system])+wynik
        numer-=numer%system;
        numer//=system      
    return wynik;

def zamSystemNa10(system,numer):
    global cyfry
    wynik = 0
    
    for c in numer:
        wynik*=system
        cyfra = cyfry.index(c)
        if(cyfra>=system):
            print("błędne dane")
        wynik+=cyfra
        
    return wynik;    

system1 = (int)(input("podaj System: "))
liczba = input("podaj liczbę({})".format(system1))
system2 = (int)(input("podaj System: "))

if(system1 > 16 or system2 > 16):
    for i in range(16,max(system1,system2)) :
        cyfry+=chr(ord('f')+(i-15))
print(cyfry)
print("({})".format(system2)+zam10NaSystem(system2,zamSystemNa10(system1,liczba)))

#print(zam10NaSystem(system,15))

#chr()
#ord()