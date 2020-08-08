class Node:
    def __init__(self, d=None, nextNode = None):
        self.data = d
        self.nextNode = nextNode

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.nextNode
    
    def setNext(self,newNext):
        self.nextNode = newNext

class Linkedlist:
    def __init__(self, h = None):
        self.head = h
        self.last = self.head
    
    def insertFirst(self, d):
        newNode = Node(d)
        newNode.setNext(self.head)
        self.head = newNode
        if self.last is None:
            self.last = self.head
        
    def printList(self):
        p = self.head
        while (p != None):
            print (p.data)
            p = p.nextNode

    def countList(self):
        c = 0
        p = self.head
        while (p != None):
            c += 1
            p = p.nextNode
        
        # after the while loop, c is the number of valid data in the list
        return c
    
    def search(self, d):
        current = self.head
        found = False
        while current is not None and found is False:
            if current.getData() == d:
                found = True
            else:
                current = current.getNext()
            
        if current is None:
             print("Data not in list")
             
        return current
    
    def delete(self, d):
        current  = self.head
        previous = None 
        found = False
        
        while current is not None and found is False:
            if current.getData() == d:
                found = True
                if previous is not None:
                    if current == self.last:
                        self.last = previous

                    previous.setNext(current.getNext())
                else:
                    self.head = self.head.getNext()
            else:
                previous = current
                current = current.getNext()
        
        if current is None:
            print("Data not in list")

    def getLast(self):         
        # run in O(n) 
        if self.head is None:            
            return None
        else:    
            current = self.head
            while current is not None:
                if current.getNext() is None:
                    return current                  #this is the last node
                else:
                    current = current.getNext()     #move to the next node  
    
    def getLastQuick(self):
        # run in O(1)    
        return self.last

print("HELLO! WELCOME TO LINKED LIST")
myList = Linkedlist()
myList.printList()
print("Size: ", myList.countList())

myList.insertFirst(9)
myList.insertFirst(7)
myList.insertFirst(8)
myList.insertFirst(3)
myList.insertFirst(4)
myList.insertFirst(1000)

myList.printList()
print("Size: ", myList.countList())

node = myList.search(1000)
if node is not None:
    print (node.getData())

print ("delete 3")
myList.delete(3)
myList.printList()
if myList.getLast() is not None:    
    print ("Last node", myList.getLast().getData())
else:
    print("The list has no end")

print ("delete 1000")
myList.delete(1000)
myList.printList()
if myList.getLastQuick() is not None:    
    print ("Last node", myList.getLastQuick().getData())
else:
    print("The list has no end")

print ("delete 9")
myList.delete(9)
myList.printList()
if myList.getLastQuick() is not None:    
    print ("Last node", myList.getLastQuick().getData())
else:
    print("The list has no end")

print ("delete 2000")
myList.delete(2000)
myList.printList()
if myList.getLastQuick() is not None:    
    print ("Last node", myList.getLastQuick().getData())
else:
    print("The list has no end")