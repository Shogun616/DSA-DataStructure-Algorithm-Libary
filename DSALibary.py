#import unittest

#from graph import Graph
#from linkedlist import LinkedList
#from node import Node
#from BinarySearchTree import BinarySearchTree
#from Test_BinarySearchTree import *

#from tests.linkedlist_test import *
#from tests.doublelinkedlist_test import *

#from Test_Graphpy import *




#ll = LinkedList()

#print(ll.isEmpty() )



#BST = BinarySearchTree()


#BST.insert(5)
#BST.insert(9)
#BST.insert(11)
#BST.insert(44)
#BST.insert(15)
#BST.insert(28)
#BST.insert(51)
#BST.insert(72)
#BST.insert(88)
#BST.insert(99)



#print(BST.find(5).getData() )

#print(BST.isEmpty() )

#Grh = Graph()

#Grh.addVertex(5)
#Grh.addVertex(9)
#Grh.addVertex(11)
#Grh.addVertex(44)
#Grh.addVertex(15)
#Grh.addVertex(28)
#Grh.addVertex(51)
#Grh.addVertex(72)
#Grh.addVertex(88)
#Grh.addVertex(99)

#print(Grh.areNeighbours(5,15))

#Grh = Graph()

#g.addEdge( "A", "B" )
#g.addEdge( "A", "E" )
#g.addEdge( "B", "C" )
#g.addEdge( "C", "D" )
#g.addEdge( "C", "G" )
#g.addEdge( "D", "H" )
#g.addEdge( "E", "I" )
#g.addEdge( "F", "J" )
#g.addEdge( "G", "K" )
#g.addEdge( "I", "M" )
#g.addEdge( "J", "N" )
#g.addEdge( "L", "P" )
#g.addEdge( "M", "N" )
#g.addEdge( "N", "O" )
#g.addEdge( "O", "P" )


#print( g.findDFSPath( "M", "H" ) )
# Should be
#  ['M', 'I', 'E', 'A', 'B', 'C', 'D', 'H']

#g = Graph()
#g.addVertex("STHLM")
#g.addVertex("OREBRO")
#g.addVertex("LIDK")
#g.addVertex("GBG")
#g.addVertex("HELBG")
#g.addVertex("LUND")
#g.addVertex("KRIST")
#g.addVertex("JONK")
#g.addVertex("LINK")

#g.addEdge( "STHLM",  "OREBRO", 75 )
#g.addEdge( "OREBRO", "LIDK",   25 )
#g.addEdge( "LIDK",   "GBG",    50 )
#g.addEdge( "GBG",    "HELBG",  5 )
#g.addEdge( "HELBG",  "LUND",   5 )
#g.addEdge( "LUND",   "KRIST",  20 )
#g.addEdge( "KRIST",  "JONK",   15 )
#g.addEdge( "HELBG",  "JONK",   35 )
#g.addEdge( "JONK",   "LINK",   100 )
#g.addEdge( "LINK",   "STHLM",  30 )

#print( g.findCheapestPath( "STHLM", "LUND" ) )
# Should be:
#  (['STHLM', 'LINK', 'JONK', 'HELBG', 'LUND'], 170)



#print(Grh.isEmpty())

#if __name__=='__main__':
 #   unittest.main(verbosity=2)

from sort import bubbleSort, insertionSort, selectionSort, shellSort

import random, time
mylist=[]

for i in range(100000):
    mylist.append( random.randint(1,100))

t1 = time.time()
insertionSort.insertionSort(mylist)
t2 = time.time()

print( "Insertion sort took {:.4f} seconds".format(t2-t1))


#mylist = [54,26,93,17,77,31,44,55,20]
#selectionSort.selectionSort(mylist)
#print(mylist)




