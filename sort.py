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

         while position > 0 and alist[position-1] > currentvalue:
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

class heapSort:

 def heapify(array, n, i):
        largest=i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and array[i] < array[l]:
            largest = l

        if r < n and array[largest] < array[r]:
            largest = r

        if largest != i:
            array[i], array[largest] = array[largest],array[i]
            
            heapSort.heapify(array, n, largest)

 def heapSort(array):
        n = len(array)

        for i in range(n, -1, -1):
            heapSort.heapify(array, n, i)

        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapSort.heapify(array, i, 0)

class mergeSort:

 def merge(array, l, m, r):
     n1 = m - l + 1
     n2 = r - m

     L = [0] * (n1)
     R = [0] * (n2)

     for i in range(0, n1):
         L[i] = array[l + i]

     for i in range(0, n2):
         R[j] = array[m + 1 + j]

     i = 0
     j = 0
     k = l

     while i < n1 and j < n2:
         if L[i] <= R[j]:
             array[k] = L[i]
             i += 1
         else:
             array[k] = R[j]
             j += 1
         k += 1

     while i < n1:
         array[k] = L[i]
         i += 1
         k += 1

     while j < n2:
         array[k] = R[j]
         j += 1
         k += 1

 def mergeSort(array, l, r):
     if l < r:

        m = (l+(r-1))/2

        mergeSort.merge(array, l, m)
        mergeSort.merge(array, m + 1, r)
        mergeSort.merge(array, l, m, r)

class quickSort:

    def partition(arr,low,high):
        i = ( low-1 )         # index of smaller element
        pivot = arr[high]     # pivot
 
        for j in range(low , high):
 
        # If current element is smaller than or
        # equal to pivot
            if   arr[j] <= pivot:
         
            # increment index of smaller element
               i = i+1
               arr[i],arr[j] = arr[j],arr[i]
 
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return ( i+1 )
   

    def quickSort(arr,low,high):
        if low < high:
            
           pi = partition(arr,low,high)
        
           quickSort(arr, low, pi-1)
           quickSort(arr, pi+1, high)
