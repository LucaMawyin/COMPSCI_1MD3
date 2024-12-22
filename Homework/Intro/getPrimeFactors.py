
from typing import List

# Get prime factors of int n
# Uses recursion

def isPrime(n:int) -> bool:
    for i in range(2,n-1):
        if n%i == 0:
            return False
    return True

def getPrimeFactors(n:int, d:int) -> int:
    if d > n:
        return 
    
    elif n%d == 0:
        return getPrimeFactors(n/d,n/d)

    else:
        return getPrimeFactors(n,d+1)