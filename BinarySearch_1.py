#this is to do Binary search in a list.

#this is a type of recursive algorithm

def BinarySearch(arr,l,r,x):   #where x is th target value and l is the leftmost element (start element) and r is the right-most element (end)

    #checking the base case

    if r>=1:
        mid = l + (r-1) //2

        #if element is present at the middle
        if arr[mid] == x:
            return mid

        #if element is greater than the middle, than it is present on the right sub-array

        if arr[mid] <x:
            return BinarySearch(arr, mid+1,r,x)   #right recursion created
        
        #if element is less than the middle, we go to the left sub array only

        else:
            return BinarySearch(arr,l,mid-1,x)          #left recursion created

    else:
        return -1     #it means element is not inside the array