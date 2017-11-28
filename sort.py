

class bubbleSort:

 def bubbleSort( alist ):

   for passnum in range( len(alist)-1,0,-1 ):
       for i in range( passnum ):
           if alist[i] > alist[i+1]:
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] =  temp

 
class insertionSort:

 def insertionSort( alist ):

     for index in range( 1, len(alist) ):
         currentvalue = alist[index]
         position = index

         while position > 0 and alist[position-1] > curretnvalue:
             alist[position] = alist[position-1]
             position = position - 1

         alist[position] = currentvalue


class selectionSort:

 def selectionSort( alist ):

     for start_pos in range( 0, len(alist) ):
         positionOfMin=start_pos
         for i in range( start_pos+1, len(alist)):
             if alist[i] < alist[positionOfMin]:
                 positionOfMin=i

         temp = alist[positionOfMin]
         alist[positionOfMin] = alist[start_pos]
         alist[start_pos] = temp

class shellSort:

    def shellSort(array):

        gap = len(array) //2

        while gap > 0:

            for i in range( gap, len(array)):
                val = array[i]
                j = i
                while j >= gap and array[j - gap] > val:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = val
            gap //= 2