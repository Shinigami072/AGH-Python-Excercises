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



d = ((input()).split(" ")) #pobieramy linię z wejścia - dzielimy ją za pomocą spacji na tablicę
d = [int(i) for i in d]#tworzymy tablicę intów stworzonych ze stringów z oryginalnej tablicy
print (d) #wyświetlamy tablicę
counts = [0]*(max(d)+1) #tworzymy tablicę liczników długości największego elementu w tablicy
#w tej tablicy na indexie i znajduje się ilość powtórzeń liczby i
for i in d:
    counts[i]+=1; #przechodzimy przez wszyskie liczby w d i zwięksmy odpowiadający im licznik
    
print (counts) #wyświetlamy utworzoną tablicę
pierw = pierwsze(max(d)); #używamy funkcji do utworzenia tablicy kolejnych liczb pierwszych
print (pierw) # wyświetlamy je
delete = [] #tworzymy listę do ununięcia
for i in d: #przechodzimy przez naszą tablice wyjściową
    if(i in pierw and not i in delete):#jeżeli dana liczba jest pierwsza i nie oznaczyliśmy jej do usunięcia
        if(counts[i]%2 != 0):#sprawdzamy czy trzeba  ją usunąć
            delete.append(i);#jeżeli tak dopisujemy do listy
            
for i in delete:
    while(i in d):#usuwamy wszyskie wystąpienia w d
        d.remove(i)
print(d);            #wyświetlamy tablicę końcową
