def insertionSort(arr):

    for i in range(1,len(arr)):   #starting from the second element of the list
        
        key = arr[i]

        j = i-1  #move elements of arr[0..i-1] that are greater than key to one position ahead of their current position

        while j>=0 and key < arr[j]:

            arr[j+1] = arr[j]   #shifting elements further

            j -=1  

        arr[j+1] = key
