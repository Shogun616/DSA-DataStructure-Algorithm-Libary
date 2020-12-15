class BinarySearchTree:
    
    def __init__(self, data=None):
        self._data=data
        self._left=None
        self._right=None

    def getData(self):
        return self._data

    def setData(self, d):
        self._data=d

    def isEmpty(self):
        return self._left == self._right == self._data == None

    def insert(self, x):
        if self.isEmpty():
            self.setData( x )
        elif x < self.getData():
            if self._left:
                self._left.insert( x )
            else:
               self._left = BinarySearchTree( x )
        else:
            if self._right:
                self._right.insert( x )
            else:
                self._right = BinarySearchTree( x )

    def print(self):
        if self._left:
            self._left.print()
        print(self.getData() )
        if self._right:
            self._right.print()

    def find(self, x):
        if not self.getData():
            return None

        if self.getData() == x:
            return self
        elif self.getData() > x:
            if self._left:
                 return self._left.find(x)
            else:
                return None
        else:

            if self._right:
                 return self._right.find(x)
            else:
                 return None
      
    def size(self):
        sz = 0
        if self._left:
            sz += self._left.size()
        if self.getData():
            sz += 1
        if self._right:
            sz += self._right.size()
        return sz

    def toList(self):
        l =[]
        if self._left:
            l = l + self._left.toList()
        if self.getData():
            l.append( self.getData() )
        if self._right:
            l = l + self._right.toList()
        return l

    def delete(self, x, parent = None):
        if x < self.getData():
            self._left = self._left.delete(x, self)
        elif x > self.getData():
            self._right = self._right.delete(x, self)
        else:

            if parent==None:
                self.setData( None )
            elif not self._left:
                return self._right
            elif not self._right:
                return self._left
            else:
                (psucc, succ) = self._right._findMin( self )
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                    succ.left = self.left
                    succ.right = self.right
                    return succ
                return self

    def _findMin( self, parent ):
        if self._left:
            return self._left._findMin(self._left, self)
        else:
            return (parent, self)
