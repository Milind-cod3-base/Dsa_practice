import math

def JumpSearch(arr,x,n):

    #finding block size to be jumped
    step = math.sqrt(n)

    #finding element in the list

    prev = 0
    while arr[int(min(step,n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >=n:
            return -1

    
    #linear search in the block range

    while arr[int(prev)] <x:

        prev +=1

        #if we reached next block or end, element is not present in the array

        if prev == min(step,n):
            return -1
        
        #if element is found
        if arr[int(prev)]== x:
            return prev

        return -1

#Driver code to test

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]

x = 55
n = len(arr)

#find index of x using jumpsearch

index = JumpSearch(arr,x,n)

#print the index where 'x' is located

print("Number %d is at index %d" %(x, index))