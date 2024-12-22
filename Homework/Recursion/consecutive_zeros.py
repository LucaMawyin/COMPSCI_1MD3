'''

How many bitstrings are there of length n which do not have 4 consecutive 0s

'''

def num_bitstrings(n):
    if n <= 3:
        return 2**n
    return num_bitstrings(n-1) + num_bitstrings(n-2) + num_bitstrings(n-3) + num_bitstrings(n-4)