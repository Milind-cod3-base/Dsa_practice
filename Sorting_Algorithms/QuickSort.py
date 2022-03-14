
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