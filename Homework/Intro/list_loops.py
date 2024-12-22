from typing import List

def get_even(L: List[int]) -> List[int]:
    """
    Return a list containing the even elements of L.

    >>> get_even([])
    []
    >>> get_even([1, 3])
    []
    >>> get_even([2, 1, 2])
    [2, 2]
    """
    #TODO



def get_even_average(L: List[int]) -> float:
    """
    Returns the average of all even values of L. If there are no even
    values in L, it returns 0.

    >>> get_even_average([])
    0.0
    >>> get_even_average([1, 3])
    0.0
    >>> get_even_average([2, 1, 2])
    2.0
    >>> get_even_average([2, 1, 4, 4])
    3.33333333333333
    """
    #TODO



def get_even_average2(L: List[int]) -> float:
    evens = get_even(L)
    if evens == []:
        return 0.0
    return sum(evens)/len(evens)





def replace_with(L: List[int], x: int, y: int)-> None:
    """
    TODO

    >>> L = [1, 2, 3]
    >>> replace_with(L, 2, 4)
    >>> L
    [1, 4, 3]

    >>> L = [1, 1, 1]
    >>> replace_with(L, 1, 10)
    >>> L
    [10, 10, 10]
    """
    #TODO
    



def sum_between(start: int, end: int):
    """
    Returns the sum of all numbers between start and end inclusive.

    >>> sum_between(0, 0)
    0
    >>> sum_between(10, 20)
    165
    >>> sum_between(20, 10)
    0
    """
    #TODO
    
    


def dot_product(vector1: List[float], vector2: List[float]) -> float:
    """
    Returns the dot product of vector1 * vector2. Assume the
    vectors are of the same length.

    >>> dot_product([1, 2, 3], [4, 5, 6])
    >>> 32
    """
    #TODO




def num_of_perfect_squares(n: int) -> int:
    """
    Returns the number of perfect square between 0 and n
    inclusive.

    >>> num_of_perfect_squares(0)
    1
    >>> num_of_perfect_squares(1)
    2
    >>> num_of_perfect_squares(100)
    11
    >>> num_of_perfect_squares(101)
    11
    """
    #TODO



    









    
