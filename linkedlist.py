class Node:
    def __init__(self, data):
        self._data=data
        self._next=None

    def getData(self):
        return self._data

    def setData(self, d):
        self._data = d

    def getNext(self):
        return self._next

    def setNext(self, n):
     self._next = n

class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return  self.head == None

    def add(self, value):
        newnode  = Node(value)
        newnode.setNext(self.head)
        self.head = newnode

    def insert(self, value, after_node):
        newnode = Node(value)
        newnode.setNext( after_node.getNext() )
        after_node.setNext( newnode )

    def size(self):
        current = self.head
        sz = 0
        while current != None:
            sz += 1
            current = current.getNext()
        return sz

    def search(self, v):
        current = self.head
        while current != None:
            if current.getData() == v:
                return current
            current = current.getNext()
            return None

    def remove(self, node):
        if self.head == node:
            self.head = node.getNext()
            del node 
            return
        current = self.head
        while current != None:
            if current.getNext() == node:
                current.setNext( current.getNext().get.Next() )
                del node
                return 
            current = current.__get.Next()

    def print(self):
        current = self.head
        while current != None:
            print( current.getValue() )
            current = current.getNext()

    def reverse(self):
        current = self.hand
        prev = None
        while current != None:
            next = current.getNext()
            current.setNext(prev)
            prev = current
            current = next
        self.head = prev

    def toList(self):
        l = []
        current = self.head
        while current != None:
            l.append( current.getValue() )
            current = current.getNext ()
            return l
