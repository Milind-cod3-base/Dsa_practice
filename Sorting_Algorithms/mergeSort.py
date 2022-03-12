def mergeSort(arr):

    if len(arr)>1:

        mid = len(arr)//2   #finding the mid point of the array and storing as an integer in case lenght is odd numbers

        # dividing the array elements

        #left side
        L = arr[:mid]

        #right side 
        R = arr[mid:]

        #sorting the left side
        mergeSort(L)

        #sorting right side
        mergeSort(R)

       
