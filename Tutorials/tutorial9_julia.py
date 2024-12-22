##############################
#         Tutorial 9         #
#        Dictionaries        #
##############################

#  A dictionary is a data structure that contains key value pairs.

dictionary = {
    "A": ["apple","aardvark","ant"],
    "B": ["banana","bird","butter"],
    "C": ["carrot","cat","cheese"]
}

#   DICTIONARY FUNCTIONS
#     d.get(key) - returns the values of specified key 
#     d.items() - returns a list of key value pairs
#     d.values() - returns a list of values
#     d.keys() - returns a list of keys

print("Values of A:",dictionary.get("A"))
print("Items:",dictionary.items())
print("Values:",dictionary.values())
print("Keys:",dictionary.keys())

###########################
#        Exercises        #
# #########################

def invert(dict):
    '''
    Returns a new dictionary where the values and keys are inverted. 

    d = {1:[2,3], 2:[1,3,5], 4:[1,4]}
    >>> invert(d)
    {1:[2,4], 2:[1], 3:[1,2], 4:[4], 5:[2]}
    ''' 

    d = {}

    for key in dict:
        for elem in dict[key]:
            if elem in d:
                d[elem].append(key)
            else:
                d[elem] = [key]


    return d


def min_value(dict):
    '''
    Get the key of the minimum value of the dictionary. 

    d = {
        "COMPSCI 1MD3" : 90,
        "COMPSCI 1JC3" : 75,
        "MATH 1ZA3" : 60,
        "MATH 1B03" : 80
    }

    >>> min_value(d)
    "MATH 1ZA3"

    '''

    # Inefficient but whatever
    min = float("inf")
    min_name = ""

    for key in dict:
        if dict[key] < min:
            min = dict[key]
            min_name = key

    return min_name


    

def list_to_dict(list):
    '''
    Convert a list of lists into a dictionary.


    l = [['a', 1], ['b', 2], ['c', 3], ['a', 4]]
    >>> list_to_dict(l)
    d = {
        'a' : [1,4],
        'b' : [2],
        'c' : [3]
    }
    '''

    d = {}

    for l in list:
        key = l[0]
        if key in d:
            for i in l[1:]:
                d[key].append(i)
        else:
            d[key] = l[1:]
    
    return d


def average_salary (employees):
    '''
    Given a dictionary of employees (see format), return the average salary.

    employees = {
        "Manager" : {
                "name" : "Alice",
                "age" : 50,
                "salary" : 100000 
                },
        "Assistant" : {
                "name" : "Bob",
                "age" : 35,
                "salary" : 85000 
                },
        "Intern" : {
                "name" : "Carol",
                "age" : 20,
                "salary" : 40000 
                }
    }
    '''

    count = 0
    sal_tot = 0

    for e in employees:
        count += 1
        sal_tot += employees[e]["salary"]
    
    return sal_tot/count


