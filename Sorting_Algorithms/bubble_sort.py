
#takes two element and compares them and keep traversing further in the list

#worst case scenario: reverse sorted array O(n2)
#best case scenario: already sorted array O(n)

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#drivers code

A = [64, 34, 25, 12, 22, 11, 90]

x= bubbleSort(A)

print(x)