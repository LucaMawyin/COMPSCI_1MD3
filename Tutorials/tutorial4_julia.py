###################
#   Tutorial 4    #
###################

##########################
#  Looping over Strings  #
##########################


# 1. Write a function reverse_words that, given a sentence, reverses every other word.
def reverse_words (sentence):
    '''
    Returns a version of the sentence where every other word is reversed. 
    
    >>> reverse_words("I really love apples and bananas.")
        "I yllaer love selppa and .sananab"
    '''

    sentence = sentence.split()
    new_sentence = ""
    index = 1

    for word in sentence:
        if index % 2 == 0:
            new_sentence += word[::-1] + " "
        else:
            new_sentence += word + " "
        index += 1

    return new_sentence

# 2. Write a function that, given a string, returns the character that appears most consecutively
def consecutive_char(string):
    '''
    Returns a character that has the longest consecutive appearance, as well as how long that appearance was.
    
    >>> consecutive_char("aakfsdifjabbbbc")
        "bbbb", 4
    >>> consecutive_char("bookkeeper")
        "oo", 2
    '''

    longest_char = ""
    longest_num = 0
    last_char = string[0]
    current_num = 0

    for letter in string:
        if letter == last_char:
            current_num += 1
        else:
            if current_num > longest_num:
                longest_num = current_num
                longest_char = last_char
            last_char = letter
            current_num = 1

    return longest_char*longest_num,longest_num
    
# 3. Write a function that, given a string and a character, returns a new string that replaces all vowels with that character
def replace_vowel(string,c):
    '''
    Returns a new string where each vowel has been replaced by the character c.
    
    >>> replace_vowel("Hi My Name Is Bob", "*")
        "H* My N*m* *s B*B"
    '''

    vowels = "aeiou"
    new_string = ""

    for char in string:
        if vowels.lower() in vowels:
            new_string += c
        else:
            new_string += char
 
    return new_string


# 4. Write a function that, given a string, counts how many letters, numbers, and symbols there are
def type_count (string):
    '''
    Prints the number of letters, numbers, and symbols in the string.
    '''

    letters = 0
    numbers = 0
    symbols = 0

    for c in string:
        if c.isalpha():
            letters += 1
        elif c.isdigit():
            numbers += 1
        elif not c.isspace():
            symbols +=1

    print ("Letters: {}\n".format(letters) + "Numbers: {}\n".format(numbers) + "Symbols: {}".format(symbols))

# 5. Write a function that, given a string, capitalizes every word in the string.
def capitalize(string):
    '''
    Returns a new string where the first letter of every word in the string has been capitalized. 

    >>> capitalize("once upon a time")
        "Once Upon A Time"
    '''

    string = string.split()
    new_string = ""

    for word in string:
        new_string += word.capitalize() + " "
    
    return new_string
