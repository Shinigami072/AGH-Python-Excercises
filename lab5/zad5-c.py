# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
Created on Mon Nov  6 11:33:09 2017

@author: shinigami
"""

x = (float)(input("x:"))
y = (float)(input("y:"))    

if(x == 0 and y==0):
    print(x,y,"Środek układu współżędnych")
elif(x==0):
    print(x,y,"Oś X układu współżędnych")
if(y==0):
    print(x,y,"Oś Y układu współżędnych")
    
elif(x>0):
    if(y>0):
        print(x,y,"I ćwiartka układu współżędnych")
    else:
        print(x,y,"IV ćwiartka układu współżędnych")
else:
    if(y>0):
        print(x,y,"II ćwiartka układu współżędnych")
    else:
        print(x,y,"III ćwiartka układu współżędnych")
