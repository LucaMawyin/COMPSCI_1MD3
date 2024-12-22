###########################
# COMPSCI 1MD3 Tutorial 6 #
#      Nested Loops       #
###########################

# Write a function that prints all primes up to a certain number
# using the Sieve of Eratosthenes:
#   starting at 2, for each number, cross off all multiples of that number
#   then 

def primes(n):
    '''
    Prints all prime numbers up to a certain number n

    >>> primes(15)
        2
        3
        5
        7
        11
        13
    >>> primes(2)
        2
    >>> primes(1)
    '''

    for num in range (2,n+1):
        prime = True

        for factor in range(2,(num//2)+1):

            if num%factor == 0:
                prime = False
        
        if prime:
            print(num)



def primes_sieve(n):
    """
    Prints all primes up to a certain number n
        using the Sieve of Eratosthenes
    >>> primes_sieve(15)
        2
        3
        5
        7
        11
        13
    >>> primes_sieve(2)
        2
    >>> primes_sieve(1)
    """

    is_prime = [True] * (n+1)

    for i in range (2,n+1):
        if is_prime[i]:
            for j in range (i,n+1,i):
                is_prime[j] = False


def matrix_multiplication(a,b):
    """
    Multiplies two matrices a and b
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]

    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
    >>> matrix_multiplication(A,B)
        [114, 160, 60, 27]
        [74, 97, 73, 14]
        [119, 157, 112, 23]
    """
    result = []
    for i in range(len(a)):
        row = [0]*len(b[0])
        result.append(row)

    rowA = len(a)
    rowB = len(b)
    colB = len(b[0])

    for i in range(rowA):
        for j in range(colB):
            for k in range(rowB):
                result[i][j] += a[i][k] * b[k][j]

    for i in result:
        print(i)

    

A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]

B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
matrix_multiplication(A,B)