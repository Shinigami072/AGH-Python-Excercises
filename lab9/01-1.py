import random
random.seed()
import math

def initTab(n):
    tab = [0]*n;
    #inicjalizujemy każdy element losową wartością
    for i in range(n):
        tab[i]=random.randint(1,100);

    return tab
def verifySort(tab):
    for i in range(1,len(tab)):
        if(tab[i]<tab[i-1]):
            return False
    return True

def partitionQS(tab,start,end):
    
    #wybieramy pivot
    pivot = random.randint(start,end-1);
    tab[pivot],tab[start] = tab[start],tab[pivot]#przemieszczamy pivot na początek 
    pivot =start;#aktualizujemy pozycję 
    
    i=start #ustawiamy licznik liczbmniejczych od pivot, będzie to miejsce w którym ostatecznie wyląduje pivot
    for j in range(start+1,end):#przechodzimy prez liczby poza pivot
        if(tab[j]<=tab[pivot]):
            i+=1#zwiększamy licznik liczb większych od pivot
            tab[i],tab[j] = tab[j],tab[i]#namieniamy liczbę mniejszą od pivot,
            #z liczbą, która znajduje sie pod licznikiem
  
    tab[pivot],tab[i] = tab[i],tab[pivot]
    #ustawiamy pivot na swoim miejscu
    return i #zwracamy miejsce na którym ustawiliśmy pivot

def quickSort(tab,start,end):
    if(start <end):
        pivot =partitionQS(tab,start,end)
        quickSort(tab,start,pivot)
        quickSort(tab,pivot+1,end)
        
    return tab

def merge(tab,start,pivot,end):
    tTab = tab[start:end+1] #kopiujemy wartośći do tymczasowej tablicy
    i = start #ustawiamy index na początek łązonyvh tablic
   
    Ai = 0 #index tablicy a
    Al = (pivot-start)+1#długość tablicy a
    Bi = 0 #index tablicy b
    Bl = (end-pivot) #długość tablicy b
    
    #wstawiamy najmniejsze elemnty tablicy A i B
    #aż skończą się elemnty jednej z tablic
    while(Ai<Al and Bi<Bl):
            #sprawdzamy któryz elentów jest mniejszy
            if(tTab[Ai] < tTab[Al+Bi]):
                tab[i]=tTab[Ai]#dodajemy element z tablicy A
                i+=1#przesówamy index łączonej tablicy
                Ai+=1#przesówamy index tablicy A
            else:
                tab[i]=tTab[Al+Bi] #dodaemy element tablicy B
                i+=1
                Bi+=1
    #dodajemy nie dodane elementy tablicy A
    while(Ai<Al):
        tab[i]=tTab[Ai]
        i+=1
        Ai+=1
    #dodajemy niedodane elementy tablicy B
    while(Bi<Bl):
        tab[i]=tTab[Al+Bi]
        i+=1
        Bi+=1
    
def mergeSort(tab,start,end):
    if(end>start):
        pivot = math.floor((start+end)/2)
        mergeSort(tab,start,pivot)
        mergeSort(tab,pivot+1,end)
        merge(tab,start,pivot,end)
        
    return tab


#funkcje pomocnicze do indexów kopca
def getParent(n):
    return math.floor((n-1)/2)
def getLeft(n):
    return 2*n+1
def getRight(n):
    return 2*n+2
# funkcja pomocnicza zamiany elementów
def swap(tab,i,j):
    tab[i],tab[j] = tab[j],tab[i]
    
def repairHeap(tab,start,end):
    root = start; #pierwszym rodzicem jest pobracy rodzic
    
    while(getLeft(root) <= end):#wykonujemy do momentu aż rozic nie ma co najmniej 1 dziecka
        
        swaper =root #ustawiamy index elmentu do zmiany na rodzica
        if(tab[getLeft(root)] > tab[root]): #sprawdzamy czy rodzic jest większy od 1 dziecka
            swaper=getLeft(root)
            
        if(getRight(root) <=end and tab[swaper] < tab[getRight(root)]):
            #sprawdzamy czy rodzic ma 2 dziecko i czy jest większe od elemty pod swaper
            #(1 dzieko,rodzic)
            swaper =getRight(root)
        
        #jeżeli rodzic jest mniejszy od któregoś z dzieci
        if( not root == swaper):
            swap(tab,swaper,root) #zamieniamy je miejscami
            root = swaper #i przechodzimy do naprawy kopca zamienionego elementu
        else:
            break # inaczej kończymy wykonywanie

def buildHeap(tab):
    size = len(tab)
    parent = getParent(size-1) #pobieramy ostatniego rodzica kopca    
    
    while(parent >= 0):
        repairHeap(tab,parent,size-1) #naprawiamy warunek kopca dla niego
        parent-=1 #pobieramy poprzedniego rodzica kopca
    
def heapSort(tab):
    buildHeap(tab) # budujemy kopiec
    i = len(tab)-1 #pobieramy ostatni element kopca, 
    # jest on jednocześnie ostatnim elementem tablicy
    
    while(i>0):
        swap(tab,0,i) #zamieniamy ostatni elemenent tablicy z pierwszym
        #pierwszy element jest największy
        i-=1 #ostani element tablicy jest posortowany, sortujemy pozostałe elementy
        repairHeap(tab,0,i) #naprawiamy kopiec dla pozostałych elementów
        #powyższe wykonujemy aż przejdziemy przez wszyskie elementy tablicy
        
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

SIZE = 25
n = initTab(SIZE)
print("unsorted",n)
selectonSort(n)
print("selectonSort", n, verifySort(n))

n = initTab(SIZE)
print("unsorted",n)
insertionSort(n)
print("insertionSort", n, verifySort(n))


n = initTab(SIZE)
print("unsorted",n)
bubbleSort(n)
print("bubbleSort", n, verifySort(n))

n = initTab(SIZE)
print("unsorted",n)
quickSort(n,0,len(n))
print("quicksort", n, verifySort(n))

n = initTab(SIZE)
print("unsorted",n)
mergeSort(n,0,len(n)-1)
print("mergesort", n, verifySort(n))

n = initTab(SIZE)
print("unsorted",n)
heapSort(n)
print("heapsort", n, verifySort(n))