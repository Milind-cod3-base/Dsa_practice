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
            