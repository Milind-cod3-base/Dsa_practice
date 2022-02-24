
#first binary search was done in recursive mode

#now binary search is been done in iterative mode


#earlier recursive method was used where same function was called again and again, by reducing input size everytime. This time I will be doing it manually

def BinarySearchIterative(arr,l,r,x):
    while l<=r:
        mid = l + (r-l) // 2

        #check if element is at mid
        if arr[mid]==x:
            return mid
        
        #if its on left sub array

        elif arr[mid]> x:

            r = mid -1

        else:

            l = mid + 1
    
    #if it reaches here, it means after running the whole while loop, it didnt find the element in the list

    return -1

#driver code

arr = [2,3,4,10,40]

x= 10 