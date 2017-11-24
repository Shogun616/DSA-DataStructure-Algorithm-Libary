import unittest

#from graph import Graph
#from linkedlist import LinkedList
#from node import Node
#from BinarySearchTree import BinarySearchTree
#from Test_BinarySearchTree import *

#from tests.linkedlist_test import *
#from tests.doublelinkedlist_test import *

from Test_Graphpy import *

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

Grh = Graph()

Grh.addVertex(5)
Grh.addVertex(9)
Grh.addVertex(11)
Grh.addVertex(44)
Grh.addVertex(15)
Grh.addVertex(28)
Grh.addVertex(51)
Grh.addVertex(72)
Grh.addVertex(88)
Grh.addVertex(99)

#print(Grh.areNeighbours(5,15))


print(Grh.isEmpty())

if __name__=='__main__':
    unittest.main(verbosity=2)