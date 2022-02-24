#this is to do Binary search in a list.

#this is a type of recursive algorithm

def BinarySearch(arr,l,r,x):   #where x is th target value and l is the leftmost element (start element) and r is the right-most element (end)

    #checking the base case

    if r>=1:
        mid = l + (r-1) //2

        #if element is present at the middle
        if arr[mid] == x:
            return mid