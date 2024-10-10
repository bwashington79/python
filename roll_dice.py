import random

roll =  random.randint(1,6)

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Correct! They rolled a " + str(roll))
else: 
    print("Sorry your guess of " + str(guess) + " was incorrect.")
    print("The computer rolled a " + str(roll))
