#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:38:17 2017

@author: shinigami
"""

cyfry = "0123456789abcdefghijklmnopqrstuvwxyz";
def zam10NaSystem(system,numer):
    global cyfry
    wynik = ""
    
    while( numer > 0):
        wynik=(cyfry[numer%system])+wynik #dodaj cyfrę do wyniku
        numer-=numer%system; #pomniejsz liczbę o pobraną cyfrę
        numer//=system     
        #powtórz aż przetwożysz wszyskie cyfry
        
    return wynik;

def zamSystemNa10(system,numer):
    global cyfry
    wynik = 0
    
    for c in numer:
        wynik*=system
        cyfra = cyfry.index(c) #uzyskaj wartość cyfry w dziesiętnym
        if(cyfra>=system): #sprawdz poprawność
            print("błędne dane")
        wynik+=cyfra 
        #powtórz dla każdej cyfry, podnieś do odbowiedniej potęgi poprzez mnożenie
        
    return wynik;    


#start programu
system1 = (int)(input("podaj System: "))
liczba = input("podaj liczbę({})".format(system1))
system2 = (int)(input("podaj System: "))

print(
      "liczba ({}):".format(system2)
      +
      zam10NaSystem(system2,
                     zamSystemNa10(system1,liczba)
        ))

