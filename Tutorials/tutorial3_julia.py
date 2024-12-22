###################
#   Tutorial 3    #
###################

#############
#  Strings  #
#############

def short_long_short(s1,s2):
    '''
    This function takes two strings and returns a new string
        of the form shortlongshort, where short is the shorter
        string and long is the longer string

    >>> short_long_short("b","aaa")
    "baaab"
    >>> short_long_short("blue","red")
    "redbluered"
    '''
    
    if (len(s1) > len(s2)):
        return s2+s1+s2
    return s1+s2+s1

def even_chars(s):
    '''
    This function takes a string input and returns only the
    even characters of it in reverse order

    >>> even_chars("Hello World!")
    "!lo le"
    '''

    return s[::-2]

'''
Assume, s = "Hello World!".
Using string slicing.

d) How could you obtain "Hello"?

e) How could you obtain "World!"?

f) How could you obtain "!dlroW"?

g) How could you obtain "HloWrd"?
'''

###############
#   If/else   #
###############

#These practice questions are inspired by https://codingbat.com/python
#A good resource for practicing functions and logic

def speeding(speed,birthday):
    '''

    You are driving a little too fast, and a police officer stops you.
    Write code to compute the result: "no ticket", "small ticket", "big ticket"
    If speed is 60 or less, the result is no ticket. If speed is between 61 and 80 inclusive,
    the result is small ticket. If speed is 81 or more, the result is a big ticket.
    Unless it is your birthday. If it is, your speed can be 5 higher in all cases.

    >>> speeding(60,False)
    no ticket
    >>> speeding(65,True)
    no ticket
    >>> speeding(65,False)
    small ticket

    '''

    tolerance = 0

    if (birthday):
        tolerance += 5
    
    if (speed <= 60 + tolerance):
        return "No Ticket"
    
    elif (speed <= 80 + tolerance):
        return "Small Ticket"
    
    return "Big Ticket"


def three_sum(a,b,c):
    '''
    Given 3 int values, a b c, return their sum. However,
    if one of the values is the same as another of the values,
    it does not count towards the sum.

    >>> three_sum(3,1,3)
    1
    >>> three_sum(1,2,3)
    6
    >>> three_sum(3,3,3)
    0
    '''

    if (a == b and a == c):
        return 0
    
    elif (a == b):
        return c
    
    elif (a == c):
        return b
    
    elif (b == c):
        return a
    
    return a+b+c


# Remove the redundant code (WEEK 3 PRACTICE)

def math(a,b,c):
    if a + b > 30:
        return "A"
    elif c > 30:
        if a >= b:
            return "B"
        elif a == b:
            return "C"
    # elif c > 35:
        # return "D"
    else: 
        # if a + b > 30:
            # return "E"
        return "F"

    # return 0


def check_grade(score):
    ''' if score >= 90:
        if score >= 95:
            return "A+"
        else:
            return "A"
    else:
        if score >= 80:
            if score >= 85:
                return "B+"
            else:
                return "B"
        else:
            return "C" '''
    
    # Most of this is redundant and needs restructuring
    '''
    if score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    return "C"

    This works
    '''

    # But this works better

    scoreStr = ["A+","A","B+","B","C"]

    return -(score-80)//5    
