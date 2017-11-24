class Graph:

    def __init__(self):
        self._table = {}

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self._table.keys())

    def addVertex( self, v ):
        if v not in self._table.keys():
            self._table[v] = set([])

    def addEdge( self, v1, v2):
        if not v1 in self._table.keys():
            self.addVertex(v1)
        self._table[v1].add(v2)
        if not v2 in self._table.keys():
            self.addVertex(v2)
        self._table[v2].add(v1)

    def areNeighbours( self, v1, v2 ):
        return v2 in self._table[v1]


    


