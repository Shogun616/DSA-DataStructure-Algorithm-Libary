import unittest

from BinarySearchTree import BinarySearchTree

class Test_BinarySearchTree_isEmpty(unittest.TestCase):
    def test_empty_tree( self ):
        BST = BinarySearchTree()
        self.assertEqual( BST.isEmpty(), True )

    def test_nonempty_tree( self ):
        BST = BinarySearchTree(5)
        self.assertEqual( BST.isEmpty(), False )

class Test_BinarySearchTree_Size(unittest.TestCase):
    def test_empty_tree( self ):
        BST = BinarySearchTree()
        self.assertEqual( BST.size(), 0 )

    def test_nonempty_tree( self ):
        BST = BinarySearchTree(28)
        self.assertEqual( BST.size(), 1 )

class Test_BinarySearchTree_Insert(unittest.TestCase):
    def test_insert_from_empty_tree( self ):
        BST = BinarySearchTree()
        self.assertEqual( BST.size(), 0 )

    def test_insert_from_nonempty_tree( self ):
        BST = BinarySearchTree(88)
        self.assertEqual(BST.size(), 1 )

class Test_BinarySearchTree_find(unittest.TestCase):
    def test_find_empty_tree( self ):
        BST = BinarySearchTree()
        self.assertEqual(BST.find(11), None )

    def test_find_non_empty_tree( self ):
        BST = BinarySearchTree(51)
        self.assertNotEqual(BST.find(51), None )

#class Test_BinarySearchTree_print(unittest.TestCase):
  #  def test_print_empty_tree( self ):
  #      BST = BinarySearchTree()
  #      self.assertEqual(BST.print(), 0 )

  #  def test_print_non_empty_tree( self ):
  #      BST = BinarySearchTree(9)
  #      self.assertEqual(BST.print(), 1 )

class Test_BinarySearchTree_toList(unittest.TestCase):
    def test_toList_empty_tree( self ):
        BST = BinarySearchTree()
        self.assertEqual(BST.toList(), [] )

    def test_toList_non_empty_tree( self ):
        BST = BinarySearchTree(72)
        self.assertEqual(BST.toList(), [72])

    def test_toList_tree_with_children( self ):
        BST = BinarySearchTree(72)
        BST.insert(10)
        BST.insert(99)
        self.assertEqual(BST.toList(), [10,72,99])
