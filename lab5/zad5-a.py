#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:23:43 2017

@author: shinigami
"""

for i in range(20):
    x = 1.123456789*10e14*i/20
    result1 = x + 0.1 - x
    result2 = x - x + 0.1
    print(x,result1,result2)