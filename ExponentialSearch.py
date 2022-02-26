
#find element x in a sorted array using Exponenetial Search

#A recursive Binary Search function returns location of x in given array[l...r]
#or  else -1 is returned

def BinarySearch(arr,l,r,x):

    if r>=l:
        mid = l + (r-1) //2

        if arr[mid]==x:
            return mid     #if element is present at the middle

        if arr[mid] > x:
            #if element is smaller than the mid element
            return BinarySearch(arr,l,mid-1,x):

        return BinarySearch(arr,mid+1,r,x)    #else it can be only on the right side
    
    return -1

