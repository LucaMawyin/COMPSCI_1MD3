from typing import List
import matplotlib.pyplot as plot
import random


def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L


def selection_sort(L):

    # Swap smallest element with current element
    for i in range(len(L)):

        # Swap current with smallest
        temp = L[i]
        minimum = find_min_index(L,i)
        L[i] = L[minimum]
        L[minimum] = temp
        


def find_min_index(L, i):
    """
    Returns the index of the smallest number, starting from index i

    >>> find_min_index([8,2,4,11], 0)
    1
    >>> find_min_index([8,2,4,11], 2)
    2
    """

    minIndex = i

    for j in range(i, len(L)):
        if L[j] < L[minIndex]:
            minIndex = j

    return minIndex
    

def insert_into1(L, i):
    """
    >>> L = [2,3,4,1,5]
    >>> insert_into(L, 3)
    >>> L
    [1,2,3,4,5]
    >>> L = [2,4,3,1,5]
    >>> insert_into(L, 2)
    >>> L
    [2,3,4,1,5]
    """

    # Literally just bubbling downwards
    for j in range (i,0,-1):
        if (L[j-1] > L[j]):
            temp = L[j-1]
            L[j-1] = L[j]
            L[j] = temp

        

def insert_into2(L, i):

    temp = L[i]

    # Moving everything upwards until we get to where temp belongs
    while i-1 >= 0 and temp <= L[i-1]:

        L[i] = L[i-1]
        i -= 1

    L[i] = temp

def insert_into3(L, sortedIndex):

    # Create temp variable for last element
    temp = L[len(L)-1]

    # Remove last element from list
    L.pop()

    for i in range(sortedIndex+1):

        # If the temp < L[i] then it must be inserted at i
        if temp < L[i]:
            L.insert(i,temp)
            return

    # temp belongs at the very end of the list
    L.insert(sortedIndex, temp)

def insertion_sort1(L):
    for i in range(len(L)):
        insert_into1(L,i)
    
# [4,6,2,3,6,8]
# [4,4,6,2,3,6] 8
# [4,8,6,2,3,6]
# [4,4,8,6,2,3] 6

def insertion_sort2(L):

    for i in range(1,len(L)):
        insert_into2(L, i)

def insertion_sort3(L):

    for i in range(1,len(L)):
        insert_into3(L, i)

    i = 1
    while i < len(L) or L != sorted(L):
        insert_into3(L,i)
        i +=1


def bubble_sort1(L):
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp


def bubble_sort2(L):

    sorted = False

    while not sorted:

        sorted = True
        
        j = 1
        for i in range(len(L)-j):

            if L[i] > L[i+1]:
                temp = L[i]
                L[i] = L[i+1]
                L[i+1] = temp

                sorted = False

        j+=1



def quicksort(L):
    if len(L) <= 1:
        return L
    x = L[0]
    a,b = [],[]
    for num in L[1:]:
        if num < x:
            a.append(num)
        else:
            b.append(num)
    return quicksort(a) + [x] + quicksort(b)

# ========================================================
    

def system_sort(L: List[int]) -> None:

    #Sort the items in L in non-descending order.
    L.sort()


if __name__ == "__main__":
    from timing import time_listfunc
    bubble1, bubble2 = [], []
    insertion1, insertion2,insertion3 = [], [], []
    selection= []
    quick, system = [], []
    x = []
    m = 10000
    
    for n in range(1, 50):
        x.append(n)
        #bubble1.append(time_listfunc(bubble_sort1, n, m))
        #bubble2.append(time_listfunc(bubble_sort2, n, m))
        #insertion1.append(time_listfunc(insertion_sort1, n, m))
        #insertion2.append(time_listfunc(insertion_sort2, n, m))
        insertion3.append(time_listfunc(insertion_sort2, n, m))
        selection.append(time_listfunc(selection_sort, n, m))
        #quick.append(time_listfunc(quicksort, n, 1))
        #system.append(time_listfunc(system_sort, n, 1))
        
    #plot.plot(x, bubble1, label = "bubble1")
    #plot.plot(x, bubble2, label = "bubble2")
    #plot.plot(x, insertion1, label = "insertion1")
    #plot.plot(x, insertion2, label = "insertion2")
    plot.plot(x, insertion3, label = "insertion3")
    plot.plot(x, selection, label = "selection1")
    #plot.plot(x, quick, label = "quick")
    #plot.plot(x, system, label = "system")
    plot.legend()
    plot.show()