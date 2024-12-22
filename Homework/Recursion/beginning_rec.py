from typing import Dict, List

"""
All functions in this file are intended to be implemented recursively
"""


def fact(n:int)->int:
    """
    Returns n factorial, i.e., n!
    Assume n >= 0.
    >>> fact(0)
    1
    >>> fact(1)
    1
    >>> fact(5)
    120
    """
    if n <= 1:
        return 1
    return n * fact(n-1)



def fib(n:int)->int:
    """
    Returns nth Fibonacci number
    Assume n >= 0.
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(5)
    5
    >>> fib(10)
    55
    """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def get_length(s: str)-> int:
    """
    Returns the length of s. Do not use len or a loop.
    """

    if s == "":
        return 0

    return 1 + get_length(s[1:])

def count_char(s: str, char: str)-> int:
    """
    Returns the number of times char appears in s.
    Do not use len or a loop.
    """

    return 0 if s == '' else (char == s[0]) + count_char(s[1:], char)



    
def is_palindrome(s: str)-> bool:
    """
    Returns True iff s is a palindrome.
    Do not use rev or a loop.
    """

    return (len(s) <= 1) or ((s[0] == s[-1]) and is_palindrome(s[1:-1])) 



def reverse(s: str) -> str:
    """
    Returns the reverse of s.
    """

    if len(s) <= 1:
        return s

    return reverse(s[1:]) + s[0]


def remove_first(s: str, char: str)-> str:
    """
    Returns a version of s with the first occurence of char removed.

    >>> remove_first()
    """

    if len(s) == 0:
        return ""

    elif char == s[0]:
        return s[1:]

    return s[0] + remove_first(s[1:],char)


def replace_all(s:str, old: str, new: str)->str:


    if len(s) == 0:
        return ""

    return new + replace_all(s[1:],old,new) if s[0] == old else s[0] + replace_all(s[1:],old,new)


def replace_at(s:str, i: int, char: str)->str:
    """
    >>> replace_at("abcd", 2, "z")
    "abzd"
    >>> "a" + replace_at("bcd", 1, "z")
    >>> "a" + "b" + replace_at("cd", 0, "z")
    """

    if i > len(s): return s

    elif not i:
        return char + s[1:]

    return s[0] + replace_at(s[1:],i-1,char)

def remove_first_k(s:str, char:str, k:int) ->str:
    # Remove first k amount of instances of char in s


    if s == "" or not k:
        return s

    if s[0] == char:
        return remove_first_k(s[1:],char,k-1)

    return s[0] + remove_first_k(s[1:],char,k)


def delete_at(s:str, i: int)->str:
    
    return s if len(s) == 0 else (s[1:] if not i else s[0] + delete_at(s[1:],i-1))

def delete_chunk(s: str, start: int, end: int):
    """
    >>> delete_chunk("0123456789", 3, 7)
    "01289"
    """

    if start > end or start > len(s):
        return s

    # Start is 0 so we start counting down our end
    if not start:
        return delete_chunk(s[1:],start,end-1)

    # Derived from not start and not end <- DeMorgan's
    # We've reached end of our chunk
    if not end:
        return s[1:]

    return s[0] + delete_chunk(s[1:],start-1,end-1)
        

def is_near_palindrome(s: str)-> bool:
    """
    Returns True iff s can be turned into a palindrome by removing
    up to 1 character.

    >>> is_near_palindrome("tacocamt")
    True
    >>> is_near_palindrome("11111111101111")
    True
    >>> is_near_palindrome("111111111011110")
    False
    """

    if len(s) <= 2:
        return True

    if s[0] == s[-1]:
        return is_near_palindrome (s[1:-1])

    return is_palindrome(s[:-1]) or is_palindrome(s[1:])
            
    

def is_k_near_palindrome(s: str, k: int)-> bool:
    """
    Returns True iff s can be turned into a palindrome by removing
    up to k characters.
    """

    if len(s) <= k+1:
        return True

    
    # Ran out of chances
    if not k:
        return is_palindrome(s)

    if s[0] == s[-1]:

        # We still have another chance
        return is_k_near_palindrome (s[1:-1], k)

    # Lose a chance
    return is_k_near_palindrome(s[:-1],k-1) or is_k_near_palindrome(s[1:],k-1)


def power_set(L: List[int]) -> List[List[int]]:
    """
    Returns the powerset of L.
    """

    if not len(L):
        return [[]]
    
    return power_set(L[:-1]) + add_to_each(power_set(L[:-1]), L[-1])


def add_to_each(sets, x):
    L = sets.copy()
    for sub_list in L:
        sub_list.append(x)
    return L


def f(L):

    if len(L) <= 1:
        return L

    head = L[0]
    tail = L[1:]

    a = []
    b = []

    for x in tail:
        if x > head:
            b.append(x)
        else:
            a.append(x)
    return f(a) + [head] + f(b)