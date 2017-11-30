# -*- coding: utf-8 -*-

ceny = [ 1, 5, 8, 9,10,16,17,20,24,26]
dlug = [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
dl = (int)(input())
def cutToMoney(cut):
    money =0
    for c in cut:
        money+=ceny[(dlug.index(c))]
    return money;

def getKey(key):
    return (float)(key[0]/key[1])
def greedy(dl):
    global ceny
    global dlug
    greedyTab =[];
    for i in range(len(ceny)):
        greedyTab.append((ceny[i],dlug[i]));
    print (greedyTab)
    greedyTab=(sorted(greedyTab, key=getKey,reverse=True))
    print (greedyTab)
    cut = []
    while(dl >0):
        for cd in greedyTab:
            if(cd[1]<=dl):#wybieramy lokalnie najlepszą cenę
                cut.append(cd[1])
                dl-=cd[1]#zmniejszamy pret
                break;#przechodzimy do kolejnego punktu cięcia
    return cut



backPackTab =[
        (0,0,[]),
        (1,1,[1]),
        (2,5,[2]),
        (3,8,[3])]
backPackTabCount = 3;
def backpack(dl):
    global ceny
    global dlug
    global backPackTab
    global backPackTabCount
    if(dl<=backPackTabCount):
        return backPackTab[dl];

    for i in range(len(backPackTab),dl+1):
        for t_dlug in dlug:
            if(t_dlug> i):
                break;

            if(i <= backPackTabCount):
                cached =backPackTab[i]
            else:
                cached = None
            new = (i,backPackTab[i-t_dlug][1]+ceny[t_dlug-1],backPackTab[i-t_dlug][2]+[t_dlug])

            if(cached != None):
                if(new[1] >= cached[1]):
                    backPackTab[i]=new;
            else:
                backPackTab.append(new)
                backPackTabCount=new[0]

    return backPackTab[dl]



cut =greedy(dl)
print(cut ,cutToMoney(cut))
print(backPackTab)
cut = backpack(dl)[2]
print(backPackTab)
print(cut ,cutToMoney(cut))
