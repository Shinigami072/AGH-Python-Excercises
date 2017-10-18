# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a= (float)(input("a="))
b= (float)(input("b="))
print("Możliwe działaznia:\n+\n-\n\\\n*\n^")
znak=(input("działanie:"))


if znak == "+":
    wynik=a+b
elif znak=="-":
    wynik=a-b
elif znak=="\\":
    wynik=a/b
elif znak=="*":
    wynik=a*b
elif znak=="^":
    wynik=a**b
else:
    wynik="?"



print(a,znak,b,"=",wynik);

