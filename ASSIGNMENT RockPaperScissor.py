########################################
## Rock Paper Scissors Program        ##
## Animikh Aich                       ##
## animikhaich@gmail.com              ##
########################################

from random import choice

# Make the list of options
choice_set = ['Rock', 'Paper', 'Scissors']
user_points = 0
computer_points = 0

# Infinite Loop
while True:
    # Request the user to enter the option
    user_input = input('Rock, Paper or Scissors?: ')
    # Chose a random element from Rock, Paper or Scissors
    random_choice = choice(choice_set)

    # If the user wants to quit, display the game summary and exit the loop
    if user_input.lower() == 'quit' or user_input.lower() == 'bye':
        print('\n\nFinal Scores: User = {} | Computer = {}'.format(user_points, computer_points))
        if user_points > computer_points:
            print("Congratulations! You win!")
        elif user_points == computer_points:
            print("Draw!")
        else:
            print("Hurray! I won!")
        break

    # If It is a draw, provide suitable message and don't count scores
    elif random_choice.lower() == user_input.lower():
        print("Computer's choice:", random_choice)
        print("Draw! Let's Do it again")

    # For all possible combinations, add score to user or PC depending on who wins
    else:
        print("Computer's choice:", random_choice)
        if user_input.lower() == 'rock' and random_choice.lower() == 'scissors':
            user_points += 1
            print('You win!')
        elif user_input.lower() == 'rock' and random_choice.lower() == 'paper':
            computer_points += 1
            print('I win!')
        elif user_input.lower() == 'paper' and random_choice.lower() == 'scissors':
            computer_points += 1
            print('I win!')
        elif user_input.lower() == 'paper' and random_choice.lower() == 'rock':
            user_points += 1
            print('You win!')
        elif user_input.lower() == 'scissors' and random_choice.lower() == 'rock':
            computer_points += 1
            print('I win!')
        elif user_input.lower() == 'scissors' and random_choice.lower() == 'paper':
            user_points += 1
            print('You win!')
        else:
            # If the user enters anyting other than the required input
            print('Please Enter Valid Input')
            continue

    # Print the score summary for every time the game is played
    print('Current Scores: User = {} | Computer = {}\n'.format(user_points, computer_points))
