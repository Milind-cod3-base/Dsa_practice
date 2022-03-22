# Bucket sort is used to sort input which is uniformly distributed over a range.

# Here Lists are called buckets

# It is better than others in sorting uniformly distributed range data as it uses time complexity of O(1)

def insertionSort(b):    #sorting individual buckets
    for i in range(1,len(b)):
        up = b[i]
        j = i -1 
        while j>= 0 and b[j] > up:
            b[j+1] = b[j]
            j -= 1
        
        b[j + 1] = up
    

    return b 