

def bubbleSortOptimized(arr):

    n = len(arr)

    for i in range(n):   #traverse through all array elements
        swapped = False

        #last i elements are already in place

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:

                arr[j], arr[j+1] = arr[j+1],arr[j]

                swapped = True   #means swapping has been done


        if swapped == False:  #if no two elements were swapped within the bubble, break

            break


#drivers code
A  =  [64, 34, 25, 12, 22, 11, 90]

bubbleSortOptimized(A)

print("Sorted Array")

for i in range(len(A)):
    print("%d" %A[i], end=" ")