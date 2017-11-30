# -*- coding: utf-8 -*-
import math
def pierwsze(n):
    #deklaracja tablicy, pokazującej czy dana liczba jest pierwsza
    pierwsze = [False]*2 + [True]*(n-2)
    #Deklaracja tablicy do przechowywania końcowych liczb pierwszych 
    ppierwsze =[0]*n
    ppi=0;# licznik liczb pierwszych
    d=math.sqrt(n) #obliczenie pierwiastka z n, musimy sprawdzić jedynie liczbymniejsze od tego pierwiastka

    for (i,p) in enumerate(pierwsze):#przechodzimy przez listę liczbpierwszych (i - sprawdzana liczba, p - czy jest pierwsza)
        if(i>d):
            break #zakończenie sprawdzania jeżeli i > pierwiastka z n
        if(not p):
            continue # pominięcie jeśeli i nie jest liczbą pierwszą
        
        for delete in range(i*i,n,i):
            pierwsze[delete]=False#usunięcie wszyskich wielokrotności liczby pierwszej
    for (i,p) in enumerate(pierwsze):
        if(p):
            ppierwsze[ppi]=i #dodanie liczby pierwszej do listy liczb pierwszych
            ppi+=1;#zwiększenie licznika liczb pierwszych
    return ppierwsze[0:ppi] #zwracamy wszyskie liczby pierwsze



d = ((input()).split(" "))
d = [int(i) for i in d]
print (d)
counts = [0]*(max(d)+1)
for i in d:
    counts[i]+=1;
    
print (counts)
pierw = pierwsze(max(d));
print (pierw)
delete = []
for i in d:
    if(i in pierw and not i in delete):
        if(counts[i]%2 != 0):
            delete.append(i);
            
for i in delete:
    while(i in d):
        d.remove(i)
print(d);            