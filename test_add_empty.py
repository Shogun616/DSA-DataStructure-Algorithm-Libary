import unittest

from linkedlist import LinkedList

class Test_LinkedList_Add(unittest.TestCase):
    def test_create_empty_list(self):
        ll = LinkedList()
        self.assertEqual( ll.isEmpty(), True )
        self.assertEqual( ll.size(), 0 )

    def test_add_empty_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        self.assertEqual( ll.size(), 1 )

    def test_add_nonempty_list( self ):
        ll = LinkedList()
        ll.add( 50 )
        ll.add( 100 )
        self.assertEqual( ll.size(), 2 )
