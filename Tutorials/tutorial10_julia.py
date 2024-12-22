from typing import List

###########################
#     Tutorial 10         #
#      Recursion          #
###########################

'''
Recursion: defining a problem in terms of a simpler version of itself
i.e. a function that calls itself, with a smaller input 

Needs:
    - Base case: stopping point for recursion, check for this FIRST 
    - Recursive case: calls function itself
        - input needs to be smaller than current function call
            - i.e. counter is less, string length is smaller, etc.

Tips:
    - Helpful to use an auxiliary function which does recursive call
    - Start with the base case

'''

def increasing_combinations(n, k):
    '''
    Given two positive integers n and k, generate and 
    print all possible combinations of k increasing integers
    where the integers are from the first n natural numbers

    >>> increasing_combinations (5,3)
    1 2 3
    1 2 4
    1 2 5
    1 3 4
    1 3 5
    1 4 5
    2 3 4
    2 3 5
    2 4 5
    3 4 5
    '''
    
    if n == k:
        printList(1,n)
    
    return printList(n-(k-1), n) + increasing_combinations(n, k-1)

def printList(length,end):

    for i in range (length):
        print


def bottles(money, price, return_reward):
    '''
    You want to buy bottles of milk. When you return your bottle, 
    your deposit is returned. Given the money you have, the price of a bottle,
    and the reward for returning a bottle, return how many bottles 
    of milk you can buy. 

    '''

print(bottles(16,2,1))

'''
Merge sort is a 'divide and conquer' sorting algorithm where you 
follow these steps.
1. Divide list into two halves until it can't be divided (lists are length 1)
2. Each subarray is sorted using merge sort
3. Merge the sorted subarrays back in sorted order

Functions needed:
    - merge_sort to execute main algorithm
    - merge to merge two subarrays together

'''

def mergeSort(a):

    if len(a) == 1:
        return a
    
    return merge(mergeSort(a[:len(a)//2]), mergeSort(a[len(a)//2:]))

def merge(a,b):

    if not len(a):
        return b
    
    if not len(b):
        return a

    if a[0] > b[0]:
        return [b[0]] + merge(a,b[1:])
    
    return [a[0]] + merge(a[1:],b)
