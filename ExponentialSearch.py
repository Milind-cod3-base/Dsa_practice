
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

def exponentialSearch(arr,n,x):

    if arr[0]==x:
        return 0    #if element is present at the first location
    

    #find range for binary search, i is doubled at every iteration

    i = 1

    while i<n and arr[i] <=x:
        i = i*2
    
    #after getting a range, which is between i//2 and i, its good to use a binary search

    return BinarySearch(arr,i // 2, min(i,n-1),x) #as i could cross the range of list (as it is doubled everytime), minimum of last element and i is taken. Which comes first.


# driver code

arr = [2,3,4,10,40]
n = len(arr)
x = 10  #target to be found in the list

result = exponentialSearch(arr,n,x)
