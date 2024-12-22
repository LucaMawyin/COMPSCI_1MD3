from typing import List, Dict, TextIO

import random


def associate_pair(d: Dict[str, List[str]], key: str, value: str):
    '''Add the key-value pair to d. keys may need to be associated with
    multiple values, so values are placed in a list.
    Assumption: key is immutable
    '''
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

    


def make_dictionary(file_name: str) -> Dict[str, List[str]]:
    '''Return a dictionary where the keys are words in f and the value
    for a key is the list of words that were found to follow the key in f.
    '''

    d = {}
    context = ("","")

    file = open(file_name,"r")

    for line in file:
        for word in line.split():
            associate_pair(d,context,word)
            context = (context[-1],word)
    associate_pair(d,context,"")

    file.close()

    return d

def update_dictionary(d,file_name: str,k:int) -> Dict[str, List[str]]:
    '''Return a dictionary where the keys are words in f and the value
    for a key is the list of words that were found to follow the key in f.
    '''

    context = ("",)*k

    file = open(file_name,"r")

    for line in file:
        for word in line.split():
            associate_pair(d,context,word)
            context = context[1:] + (word,)
    associate_pair(d,context,"")

    file.close()


def mimic_text(word_dict: Dict[str, List[str]], num_words: int) -> str:
    """Based on the word patterns in word_dict, return a string that mimics
    that text, and has num_words words.
    """

    story = ""
    context = random.choice(list(word_dict.keys()))

    for _ in range(num_words):

        word = word_dict[context][random.randint(0,len(word_dict[context])-1)]
        story += word + " "
        context = context[1:] + (word,)

    return story

def full_dictionary(k:int) -> Dict[str, List[str]]:
    d = {}
    d = update_dictionary(d,"alice.txt",k)
    d = update_dictionary(d,"hamlet.txt",k)
    d = update_dictionary(d,"homer.txt",k)

    return d

def collapse_dictionary(d):
    for key in d:

        temp = {}

        for word in d[key]:
            
            if word in temp:
                temp[word] += 1

            else:
                temp[word] = 1

        d[key] = temp


def append_dictionary(file_name: str, d: Dict[str, List[str]], k:int) -> None:
    #TODO
    return




def mimic_text2(word_dict: Dict[str, List[str]], num_words: int, k: int) -> str:
    #TODO
    return
