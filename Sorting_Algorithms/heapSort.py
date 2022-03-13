
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
