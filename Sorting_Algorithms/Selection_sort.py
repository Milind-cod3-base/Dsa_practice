#this is selection sort algorithm, to sort an unsorted array

# runs in O(n2) time complexity abd O(1) space complexity

#in this we take whole array and find minimum in it and place the minimum at the beginning and then we reduce the array size by 1 and find minimum in that subarray, and looping until the end

def SelectionSort(arr,n):

    for i in range(n):

        min_indx = i      #assuming the first element as minimum, and if later its not minimum, we will alter the value

        for j in range(i+1,n):   #a for loop to check in the rest of the subarray
            
            if arr[min_indx] > arr[j]:
                min_indx = j

        arr[i], arr[min_indx] = arr[min_indx], arr[i]  #elements swapped - first and last interchanged position
    
    return arr  #bug fixed
    


#drivers code written

arr = [63,22,43,11,12]     

n = len(arr)

A2 = SelectionSort(arr,n)

print(A2)   #printing of selection sorted array donne


