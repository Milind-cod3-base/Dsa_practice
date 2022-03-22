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

def bucketSort(x):
    arr= []
    slot_num = 10 # 10 means 10 slots, each slot's size is 0.1

    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets 
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])

    # Concatenate the result
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):

            x[k] = arr[i][j]
            k +=1

    return x

# Driver code

x = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434]

print("Sorted Array is")
print(bucketSort(x))