import random
random.seed()

def initTab(n):
    tab = [0]*n;
    #inicjalizujemy każdy element losową wartością
    for i in range(n):
        tab[i]=random.randint(1,100);

    return tab

def selectonSort(n):
    for x in range(len(n)):
        #wybieramy najmniejszą wartość(jej index) w zakresie (x-końca tablicy)
        min = x
        for i in range(x,len(n)):
            if(n[min]>n[i]):
                min=i

        #zamieniamy miejscami najmniejszy element z elementem x
        n[min],n[x] = n[x],n[min]

    return n

def insertionSort(n):
    for i in range(1,len(n)):
        #pobieramy kolejny element
        insVal = n[i];
        #sprawdzamy czy jest mniejszy od już pobranych elementów
        j = i-1;
        while (j>=0 and n[j]>insVal):
            #przesówamy większe  elementy w prawo
            n[j+1]=n[j]
            #przechodzimy do elementu j-1
            j-=1
        #w tym momencie jesteśmy nad elementem mniejszym od wstawianej wartości
        #mamy większewartości przesunięte w prawo
        # i bezpośrednio naprawo od nas jest skopiowany element od nas większy
        n[j+1]=insVal

    return n

def bubbleSort(n):
    isSorted = False
    sortingCount = 1;
    size = len(n)
    while(not isSorted and sortingCount <=size):
        #Zmieniamy flage w nadzieji że posortowaliśmy tablice
        isSorted = True
        #sprawdzamy elementy od 0 do SortCount
        for i in range(size-sortingCount):
            if(n[i] > n[i+1]):#Jeżeli znaleźliśmy nieposortowane elementy zamieniamy je miejscami
                n[i], n[i+1] = n[i+1],n[i]
                #Ustawiamy flagę
                isSorted = False
        #zwiększamySortCount
        sortingCount+=1
    return n;

SIZE = 10
n = initTab(SIZE)
print(n)
print(selectonSort(n))
n = initTab(SIZE)
print(n)
print(insertionSort(n))
n = initTab(SIZE)
print(n)
print(bubbleSort(n))