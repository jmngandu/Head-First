import random
winner = ''
random_choice = random.randint(0,2)
computer_choice = random_choice
if random_choice == 1:
    computer_choice = 'rock'
elif random_choice == 2:
    computer_choice = 'paper'
elif random_choice == 3:
    computer_choice = 'scissor'
    user_choice = input('rock, paper or scissors?')
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'
print('The', winner, 'wins!')

