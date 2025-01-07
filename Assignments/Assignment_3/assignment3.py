from typing import List

# Inserts string into Trie
def insert(data, s: str)-> None:
    if s == "":
        return
    if len(s) == 1:
        if s in data:
            data[s][1] = True
        else:
            data[s] = [{}, True]
    if s[0] in data:
        insert(data[s[0]][0], s[1:])
    else:
        data[s[0]]= [{}, False]
        insert(data[s[0]][0], s[1:])

# Number of trues in a tree
def count_words(data)->int:
    """
    Returns the number of words encoded in data. You may assume
    data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> count_words(data)
    6
    """

    total = 0

    for key in data:

        # Adding each True to our sum
        total += int(data[key][1]) + count_words(data[key][0])

    return total

# Moving down tree through each char of word until we reach bottom and return if true/false
def contains(data, s: str)-> bool:
    """
    Returns True if and only if s is encoded within data. You may
    assume data is a valid trie.

    >>> data = {}
    >>> insert(data, "tree")
    >>> insert(data, "trie")
    >>> insert(data, "try")
    >>> insert(data, "trying")
    
    >>> contains(data, "try")
    True
    >>> contains(data, "trying")
    True
    >>> contains(data, "the")
    False
    """

    if not len(s):
        return True
    
    return (s[0] in data) and contains(data[s[0]][0],s[1:])

# Just finding height of Trie
def height(data)->int:
    """
    Returns the length of longest word encoded in data. You may
    assume that data is a valid trie.

    >>> data = {}
    >>> insert(data, "test")
    >>> insert(data, "testing")
    >>> insert(data, "doc")
    >>> insert(data, "docs")
    >>> insert(data, "document")
    >>> insert(data, "documenting")

    >>> height(data)
    11
    """

    heightList = []

    # 0 height
    if not len(data):
        return 0
    
    for key in data:

        # Adding height of each word to list
        heightList.append (1 + height(data[key][0]))

    # Returning only the max height (longest word length)
    return max(heightList)

# Just counting length of dictionary at given subtree
def count_from_prefix(data, prefix: str)-> int:
    """
    Returns the number of words in data which starts with the string
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professionnal")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> count_from_prefix(data, 'pro')
    5
    """
    
    if not len(prefix):
        return count_words(data)
    
    if prefix[0] not in data:
        return 0
    
    return count_from_prefix(data[prefix[0]][0], prefix[1:])

# Go down Trie until prefix is ""
# Then return every word from iterated tree that's valid
# Add prefix to valid word
def get_suggestions(data, prefix:str)-> List[str]:
    """
    Returns a list of words which are encoded in data, and starts with
    prefix, but is not equal to prefix. You may assume data is a valid
    trie.

    data = {}
    >>> insert(data, "python")
    >>> insert(data, "pro")
    >>> insert(data, "professionnal")
    >>> insert(data, "program")
    >>> insert(data, "programming")
    >>> insert(data, "programmer")
    >>> insert(data, "programmers")

    >>> get_suggestions(data, "progr")
    ['program', 'programming', 'programmer', 'programmers']
    """


    try:
        if not len(prefix):
            return getWords(data)
        
        # Adding current char to each element in list
        # Otherwise will return word - prefix
            # Ex. prog -> [ram,ramming...]
        return addToAll(get_suggestions(data[prefix[0]][0], prefix[1:]),prefix[0])
    except KeyError:
        return []

# Gets all valid words in a Trie
# NOT TO BE USED OUTSIDE OF get_suggestions
def getWords(data:dict,prefix=""):

    wordList = []

    # Reached bottom of Trie
    if not len(data):
        return wordList

    # Going through each branch in Trie
    for key in data:

        # Starting word
        word = prefix + key

        # Word is complete
        if data[key][1]:
            wordList.append(word)

        # Go through rest of words in Trie
        wordList += getWords(data[key][0], word)

    return wordList

# Adds s to each element in list
# NOT TO BE USED OUTSIDE OF get_suggestions
def addToAll(list:List[str], s:str) -> List[str]:

    for i in range (len(list)):
        list[i] = s + list[i]

    return list