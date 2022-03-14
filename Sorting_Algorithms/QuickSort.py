
def partition(start, end, array):

    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]


    # This loop runs till start pointer crosses end pointer, and when it does we swap the pivot with element on end pointer

    while start < end:


        while start < len(array) and array[start] <= pivot:
            start +=1   # Increment the start pointer till it finds an element greater than pivot


            # Decrement the end pointer till it finds an element less than pivot
            while array[end] > pivot:

                end -=1

            
            if (start < end):  #if start and end have not crossed each other, swap the numbers on start and end
                array[start], array[end] = array[end], array[pivot_index]

    # Swap pivot element with element on end pointer. This puts pivot on its correct sorted place.

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end     # Returning end pointer to divide the array into 2


# The main function which implements the Quick Sort algorithm

def quick_sort(start, end, array):

    if (start < end):

        # p is partitioning index, array[p] is at right place

        p = partition(start, end, array)

        # Sort elements before partition and after partition
        quick_sort(start, p -1, array)
        quick_sort(p+1 , end, array)      # Recursive function calling



# Driver's code

array = [ 10, 7, 8, 9, 1, 5 ]
quick_sort(0, len(array) -1 , array)

# Printing sorted array using f-string which is newly introduced in Python 3.6

print(f'Sorted array: {array}') # here due to f-string, {array} becomes replaceable. It increases more readability.

