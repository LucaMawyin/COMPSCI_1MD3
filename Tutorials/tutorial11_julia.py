########################################
#           Tutorial 11                #
#            Recursion                 #
########################################

def tower_of_hanoi(n, start, to, aux):
    '''
    Executes the tower of hanoi for n discs
    '''

    if n == 1:
        print("Moving disc 1 from", start,"to",to)
        return
    tower_of_hanoi(n-1,start,aux,to)
    print("Moving disc",n,"from",start,"to",to)
    tower_of_hanoi(n-1,aux,to,start)


def is_interleaved(string_a, string_b,string_c):
    '''
    Returns true if string C is an 
    interleaving of string A and string B

    >>> is_interleaved("abc","def","adebcf")
    True
    '''

    if len(string_c) != (len(string_a) + len(string_b)):
        return False

    if len(string_a) == 1 and len(string_b) == 1:
        return string_c.count(string_a) == string_c.count(string_b)
    
    if not len(string_a):
        return string_c == string_b
    
    if not len(string_b):
        return string_a == string_c
    
    if string_c[0] == string_a[0]:
        return is_interleaved(string_a[1:],string_b,string_c[1:])
    
    if string_c[0] == string_b[0]:
        return is_interleaved(string_a,string_b[1:],string_c[1:])
    
    return False

def subset_sum(list, value):
    '''
    Checks if a subset of the list adds up to the value
    '''

    if not len(list):
        return not value
    
    if not value:
        return True

    if len(list) == 1:
        return list[0] == value
    
    return subset_sum(list[1:],value-list[0]) or subset_sum(list[1:],value)

