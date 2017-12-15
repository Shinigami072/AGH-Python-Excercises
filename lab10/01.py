#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 09:43:50 2017

@author: shinigami
"""

class Node:
    def __init__(self,data):
            self.prev=None
            self.next=None
            self.data=data
    def __str__(self):
        return str(self.data)
        
class BidirectionalList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        
    def printList(self):
        n = self.head
        while n:
            print (n, end =", ")
            n = n.next
        print(" ",self.size)
    def printListRev(self):
        n = self.tail
        while n:
            print (n, end =", ")
            n = n.prev
        print(" ",self.size)
    
    def remove(self,index):
         n= self.head
         i=0;
         while n and i != index-1:
             i+=1;
             n = n.next
         prevNode = n.prev
         nextNode = n.next
         
         prevNode.next = nextNode
         nextNode.prev = prevNode
         self.size-=1
         return n
    
    def popT(self):
        if not self.head:
            return None
        else:
            n = self.tail
            newTail= n.prev
            newTail.next = None
            self.tail = newTail
            self.size-=1
            return n
    
    def pop(self):
        if not self.head:
            return None
        else:
            n = self.head
            newHead = n.next
            newHead.prev = None
            self.head = newHead
            self.size-=1
            return n

    def insert(self,data,index):
        if not self.head:
            n = Node(data)
            self.head=n
            self.tail=n
            self.size=1
        else:
            n = self.head
            i=0;
            while n and i != index:
                i+=1;
                n = n.next
            nextNode = n.next
            prevNode = n
        
            newNode = Node(data)
            newNode.prev = prevNode
            newNode.next = nextNode
            
            prevNode.next = newNode
            nextNode.prev = newNode
            self.size+=1
            
            
    def push(self,data):
         if not self.head:
            n = Node(data)
            self.head=n
            self.tail=n
            self.size=1
         else:
            self.size+=1
            n = self.head
            new = Node(data)
            
            new.next = n
            
            n.prev=new
            self.head = new
    def getMax(self):
        n = self.head
        maxNode=n;
        while n:
            if(n and n.data > maxNode.data):
                maxNode =n
            n = n.next
        return maxNode;
    def add(self,data):
        if not self.head:
            n = Node(data)
            self.head=n
            self.tail=n
            self.size=1;
        else:
            n = self.tail
            new = Node(data)
            new.prev= n
            
            self.size+=1
            
            n.next = new
            
            self.tail = new
      
        
lb = BidirectionalList()
lb.add("1add")
lb.printList()
lb.add("2add")
lb.add("3add")
lb.printList()
lb.push("4push")
lb.push("5push")
lb.printList()
lb.insert("6insert",1)
lb.insert("7insert",4)
lb.printList()  
print(lb.pop())    
print(lb.popT())    
print(lb.remove(2))        
lb.printList()  
lb.printListRev()  
print(lb.getMax())        
lb.push("hjagearkjhgnjahglrahrglkarhuogrhrgiu")
print(lb.getMax())        
lb.printList()  

