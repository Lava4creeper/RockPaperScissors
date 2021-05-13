#Functions
def choice_checker(question):
  valid = False
  while not valid:
    #Ask user for choice
    response = input(question).lower()
    if response == 'r' or response == 'rock':
      response = 'Rock'
      print('You selected {}'.format(response))
    if response == 'p' or response == 'paper':
      response = 'Paper'
      print('You selected {}'.format(response))
    if response == 's' or response == 'scissors':
      response = 'Scissors'
      print('You selected {}'.format(response))
#Main Routine
user_choice = choice_checker("Choose rock, paper, or scissors: ")

