#this is the first search algorithm, using linear search algorithm to find an element in a list and if it is not there, return -1.

def LinearSearch(arr,x):    #defining a function with arr and x as parameters. x is the target value

    if x in arr:
        return arr.index(x)
    
    else:
        return -1
    