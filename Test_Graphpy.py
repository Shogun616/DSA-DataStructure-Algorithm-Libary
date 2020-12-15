import unittest

from graph import Graph

class Test_Graph_isEmpty(unittest.TestCase):
    def test_empty_graph( self ):
        Grh = Graph()
        self.assertEqual( Grh.isEmpty(), True )
        
class Test_Graph_Size(unittest.TestCase):
    def test_empty_graph( self ):
        Grh = Graph()
        self.assertEqual( Grh.size(), 0 )

    def test_nonempty_graph( self ):
        Grh = Graph()
        Grh.addVertex(28)
        self.assertEqual( Grh.size(), 1 )

class Test_Graph_addVertex(unittest.TestCase):
    def test_empty_graph( self ):
        Grh = Graph()
        self.assertEqual( Grh.size(), 0 )

    def test_nonempty_graph( self ):
        Grh = Graph()
        Grh.addVertex(99)
        self.assertEqual( Grh.size(), 1 )

class Test_Graph_addEdge(unittest.TestCase):
    def test_empty_graph( self ):
        Grh = Graph()
        self.assertEqual( Grh.isEmpty(), True )

    def test_nonempty_graph( self ):
        Grh = Graph()
        Grh.addEdge(11,44)
        self.assertEqual( Grh.isEmpty(), False )

class test_empty_areNeighbours(unittest.TestCase):
    def test_empty_graph( self ):
        Grh = Graph()
        Grh.addEdge(11,44)
        self.assertEqual( Grh.areNeighbours(11,44), True)

    def test_nonempty_graph( self ):
        Grh = Graph()
        Grh.addEdge(28,44) 
        self.assertEqual( Grh.areNeighbours(28,44), True)

    def test_notNeighbours_graph( self ):
        Grh = Graph()
        Grh.addEdge(28,44)
        Grh.addEdge(11,28)
        self.assertEqual( Grh.areNeighbours(11,44), False)
