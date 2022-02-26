#this is the first search algorithm, using linear search algorithm to find an element in a list and if it is not there, return -1.

def LinearSearch(arr,x):    #defining a function with arr and x as parameters. x is the target value

    if x in arr:
        return arr.index(x)
    
    else:
        return -1
    
#driver code

arr = [2,3,4,10,40]
x = 10

#making it ready to print

result = LinearSearch(arr,x)   #saving the function in a variable and saving the print values there


#print the conclusion whatever the result comes

if result == -1:
    print('The target is not in the list')

else:

    print('The target is at %d position in the list' % result)

    