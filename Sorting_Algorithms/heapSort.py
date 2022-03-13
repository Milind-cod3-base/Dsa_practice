
#python program for implementation of heap sort

# to heapify subtree rooted at index i
#n is the size of heap


# function to sort array of given size


def heapify(arr,n,i):

    largest = i  #initialise largest as root

    l = 2 * i + 1 # all the left elements are 2*i+1
    r = 2 * i + 2 # right ones are 2*i+2

    #check if left child of root exists and is greater than root
    if l<n and arr[largest] < arr[l]:  #if l<n it means that still its in the height of heap, hence it exists.

        largest = l    #assigning largest variable to left child

    
    #check if the right child exists and is greater than root
    if r<n and arr[largest]< arr[r]:

        largest = r

    #changing root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] #making a swap

        # heapify the root
        heapify(arr, n , largest)


#main funcion to sort an array of given size
def heapSort(arr):

    n = len(arr)

    #build a maxHeap
    for i in range(n//2 - 1, -1, -1): #going in reverse
        heapify(arr, n, i)

    #one by one extracting the number/elements in decending order

    for i in range(n-1,0, -1):
        arr[i],arr[0] = arr[0], arr[i]  #swapping first and last element of sorted heap
        heapify(arr, i, 0)


# Driver's code

arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")

#printing new array
for i in range(n):

    print("%d" % arr[i], end = " ") 