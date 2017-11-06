#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:27:37 2017

@author: shinigami
"""
suma =0
for i in range(300000000+1):
    suma+=1.0/3.0
    if(i%1000 == 0):
        print(i,suma)