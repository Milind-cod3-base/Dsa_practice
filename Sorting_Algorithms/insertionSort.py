def insertionSort(arr):

    for i in range(1,len(arr)):   #starting from the second element of the list
        
        key = arr[i]

        j = i-1  #move elements of arr[0..i-1] that are greater than key to one position ahead of their current position

        while j>=0 and key < arr[j]:

            arr[j+1] = arr[j]   #shifting elements further

            j -=1  

        arr[j+1] = key


# Driver code to run the function above

arr = [12,11,13,5,6]

insertionSort(arr)

#printing the sorted array

for i in range(len(arr)):

    print("%d" %arr[i], end=",")


