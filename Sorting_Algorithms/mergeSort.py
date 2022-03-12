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

       
        i =j = k=0

        #copying data to temporary arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1

            else:
                arr[k] = R[j]
                j+=1
            
            k+=1

        #checking if element is left
        while i < len(L):
            arr[k] = R[j]

            i +=1
            k +=1

        while j < len(R):
            arr[k] = R[j]

            j+=1
            k+=1
            


