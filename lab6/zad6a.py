#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:20:24 2017

@author: shinigami
"""

def prep(tekst):
    result = list(tekst.lower())
    for c in tekst:
        if(not (c.isalpha())):
            result.remove(c)
    
    return "".join(result)
def cezar(tekst, shift):
    shift= shift%25
    
    result= list(prep(tekst));
    for (i,c) in enumerate(result):
        result[i] = chr(ord(c)+shift)
    return "".join(result)

def deCezar(tekst, shift):
    shift= shift%25    
    result= list(prep(tekst));
    for (i,c) in enumerate(result):
        result[i] = chr(ord(c)-shift)
      
    return "".join(result)

def podstawieniowy(tekst,alfabet):
    result = list(prep(tekst))
    
    for (i,c) in enumerate(result):
        result[i] = alfabet[(ord(c)-ord('a'))];
        print(ord(c),ord('a'),(ord(c)-ord('a')),alfabet[(ord(c)-ord('a'))])
        
s = input()
print (s,prep(s),cezar(s,1),deCezar(cezar(s,1),1))
print (s,prep(s),podstawieniowy(s,"abcdefgi"))