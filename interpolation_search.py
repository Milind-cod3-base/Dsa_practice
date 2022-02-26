
#interpolation search with recursion

def interpolationSearch(arr, lo, hi,x):

    #since array is sorted already, an element must be in range defined by corner
    
    if (lo<=hi and x>=arr[lo] and x <=arr[hi]):

        #probing the position with keeping uniform distribution in mind

        pos = lo + ((hi-lo) // (arr[hi] - arr[lo])*(x-arr[lo]))

        #condition of target found
        if arr[pos]==x:
            return pos
        
        #if x is larger, x is in right subarray
        if arr[pos] <x:
            return interpolationSearch(arr, pos+1, hi,x)

        #if x is smaller, x is in left subarray
        if arr[pos]>x:
            return interpolationSearch(arr,lo,pos-1,x)

    return -1