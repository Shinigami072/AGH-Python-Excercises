#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:57:05 2017

@author: shinigami
"""
import math

def pascal(n):
    #elemanty końcowe
    if(n==1):
        return [[1]] #zwrócenie tablicy tablic zawierającej tablicę pierwrzego rzędu
    if(n ==2):
        b = pascal(n-1) #pobranie tablicy tablic dla poprzedniego rzędu
        b.append([1,1]) #dopisanie do tablicy, 2 rzędu
        return b

    #tu zaczynaja się rekurencyjne wywołanie
    b = pascal(n-1) #pobranie tablicy tablic dla poprzedniego rzędu
    c = [1,1]#utworzenie tablicy rozpoczętej i zakończonej jedynkami
    #b[n-2] tablica dla poprzedniego rzędu
    for i in range(1,len(b[n-2])): #przejście po wszyskich elementach poprzedniego rzędu
        c.insert(1,
                 b[n-2][i]+b[n-2][i-1]) # wpisanie symu dwóch powyższych liczb do obecnego rzędu
    b.append(c); # dopisanie nowo utworzonej tablicy do tablicy tablic
    return b #zwrócenie tablicy tablic dla obecnego rzędu

def drawPascal(n):
    length = len(n); #pobranie ilości rzędów z wielkości tablicy
    maxWidth = len(n[length-1]) # pobranie długości ostatniego rzędu
    maxValue = max(n[length-1]) #pobranie maksymalnej wartości z ostatniego rzędu
    maxValueLength = len(str(maxValue)) #pobranie ilości cyfr jakich potrzebujemy do zapisania tej liczby
    
    if(maxValueLength%2 ==0):
        maxValueLength+=1# dodanie 1 w celu wyśrodkowania
        
    spaceWidth = maxWidth*(maxValueLength+1)/2 #obliczenie połowy długości maksymalnego rzędu
    
    for row in n:
        pad = (int)(spaceWidth-(len(row)*(maxValueLength+1)/2)) # obliczenie różnicy między długością obecnego rzędu a maksymalnego
        print(" "*pad,end="")#wypełnienie róznicy spacjami
        for number in row:
            print("{:{width}d}".format(number,width=maxValueLength), end=" ")#wydrukowanie liczby na ekran
        print();#przejście do następnego wiersza
        
    
i = (int)(input())
drawPascal(pascal(i))#wywołanie funkcji pascal zwróci nam tablicę tablic, 
#zawierającą reprezentację trójkąta pascala, następnie wyprowadzimy ją na
#ekran za pomocą funkcji drawPascal
