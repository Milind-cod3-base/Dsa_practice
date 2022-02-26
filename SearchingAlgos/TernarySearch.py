#While binary search is log2n, ternary search 2*log3n (hence it takes more time in worst case and it is not desirable for worst case)


#ternary function defined 

def ternarySearch(arr,l,r,x):

    if (r>=1):

        mid1= l + (r-1) //3
        mid2 = mid1 + (r-1) //3

        #if x is present at mid1
        if arr[mid1] == x:
            return mid1
        
        #if x is present at the mid2
        if arr[mid2] == x:
            return mid2
        
        #if x is present in left  one -third
        if arr[mid1] > x:
            return ternarySearch(arr,l,mid1-1,x)
        
        if arr[mid2] < x:
            return ternarySearch(arr,mid+2,r,x) #if x is presnet in right one third
        
        #if x is prsent in middle one third
        return ternarySearch(arr,mid1+1,mid2-1,x)

    return -1   #reaching at the end, if element is not present than return -1

    #after this drivers code could be written.