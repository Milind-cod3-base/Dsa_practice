#this is selection sort algorithm, to sort an unsorted array

# runs in O(n2) time complexity abd O(1) space complexity

#in this we take whole array and find minimum in it and place the minimum at the beginning and then we reduce the array size by 1 and find minimum in that subarray, and looping until the end

def SelectionSort(arr,n):

    for i in range(n):

        min_indx = i      #assuming the first element as minimum, and if later its not minimum, we will alter the value

        for j in range(i+1,n):   #a for loop to check in the rest of the subarray
            
            if A[min_indx] > A[j]:
                min_indx = j

        A[i], A[min_indx] = A[min_indx], A[i]  #elements swapped - first and last interchanged position
    