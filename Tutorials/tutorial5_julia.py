####################### 
#    COMPSCI 1MD3     #
#     TUTORIAL 5      #
#        Loops        #
#######################

# Range: Similar to slicing, will start at first number given
#       and end before the second number. To skip, you can
#       add a third number that indicates the steps you are taking

# 1. What will be the output of the code? 
'''
for i in _______:
    print (i)

a) range(5)
b) range(4,8)
c) range(-1)
d) range(5,11,2)
e) range(4,9,-1)
f) range(9,4,-1)
'''
#1. Create a function that prints all multiples of an integer a up to an integer b
def multiples(a,b):
    '''
    Prints all multiples of a up to b

    >>> multiples(5,30)
        5
        10
        15
        20
        25
        30
    '''
    return 0

#2. Create a function that checks if a list is sorted 
def is_sorted(list):
    '''
    Checks if a list is sorted 
    
    >>> is_sorted([1,2,3,4])
        True
    >>> is_sorted([1,2,4,3])
        False
    
    '''

    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            return False    
    return True

    pass

#3. Create a function that given two binary strings, returns the sum of them
def binary_sum(s1,s2):
    '''
    Sums two binary strings
    >>> binary_sum("1","1")
        "10"
    >>> binary_sum("110","011")
        "1001"
        
    '''

    sum = ""

    carry = False
    for i in range (len(s1)-1,-1,-1):

        if carry:
            if s1[i] == "0" and s2[i] == "0":
                sum = "1"+sum
                carry = False
            elif (s1[i] == "0" and s2 == "1") or (s1[i] == "1" and s2 == "0"):
                sum = "0" + sum            
            else:
                sum = "1" + sum

        else:
            if s1[i] == "0" and s2[i] == "0":
                sum = "0" + sum

            elif (s1[i] == "0" and s2 == "1") or (s1[i] == "1" and s2 == "0"):
                sum = "1" + sum
            else:
                carry = True
                sum = "0" + sum

    if carry:
        sum = "1"+sum

    return sum

#4. Given a list of numbers, return True if the substring 1,2,3 is in the list
def list_123(l):
    '''
    Returns true if the substring [1,2,3] is in l

    >>> list_123([5,4,1,2,3])
        True
    >>> list_123([1,1,2,4,3])
        False
    '''

#5. Print a triangle as shown below
def print_triangle(height):
    '''
    Prints a triangle of * where the number of 
    stars corresponds to the row number

    >>> print_triangle(5):
            *
           ***
          *****
         *******
        *********
    '''


    for i in range (height):
        print(" " * (height-i-1) + "*" * (2*i+1))
