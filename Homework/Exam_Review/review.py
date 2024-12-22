def sum_prefix(values,k):

    if k <= 0 or not len(values):
        return []

    return [values[0]] + sum_prefix(values[1:],(k-values[0]))

def subset_sum(L,value):

    if value == 0:
        return True
    
    if len(L) == 0:
        return False
    
    return subset_sum(L[1:], value) or subset_sum(L[1:], value-L[0])

def sum_even (L):
    if len(L) == 0:
        return 0
    
    if not L[0] % 2:
        return L[0] + sum_even(L[1:])
    
    return sum_even(L[1:])

def is_anagram(s1,s2):
    if len(s1) > len(s2) or len(s2) > len(s1):
        return False
    
    else:
        for char in s1:
            if s1.count(char) > s2.count(char) or s1.count(char) < s2.count(char):
                return False
            
        return True
    
def dic_inverse(d):

    newD = {}

    for key in d:
        
        for word in d[key]:
            if word in newD:
                newD[word].append(key)
            else:
                newD[word] = [key]

    return newD