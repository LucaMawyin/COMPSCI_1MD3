from typing import List

def search(n:int, a:List[int]):

    # Found 
    if n == a[len(a)//2]:
        return True
    
    # Bottom of list and not found
    elif n != a[len(a)//2] and (len(a) == 1):
        return False
    
    # Number is greater than middle
    elif n > a[len(a)//2] and len(a) > 1:
        return search(n, a[(len(a)//2) + 1:])
    
    # number is less than middle
    else:
        return search(n, a[:len(a)//2])