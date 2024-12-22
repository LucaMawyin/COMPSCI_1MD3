import random

def guess():
    num = random.randint(1,100)
    guess = int(input("Guess a number: "))

    while num != guess:
        if num > guess:
            print("Too high")
        else: 
            print("Too low")
        guess = int(input("Guess a number: "))
    print("Correct")