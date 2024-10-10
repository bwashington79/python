import random

choices = ["scissors", "paper", "rock"]
rand = random.randint(0, 2)

print(rand)
computer_choice = choices[rand]


user_choice = input('Do you want rock, paper, or scissors?\n')

if computer_choice == user_choice:
    print('TIE')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("YOU WON")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("YOU WON")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print("YOU WON")
else:
    print('You lose and the computer WINS')