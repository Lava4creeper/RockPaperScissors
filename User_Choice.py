#Functions
def choice_checker(question):
  valid = False
  error = 'Error. Please enter Paper, Scissors or Rock'
  while not valid:
    #Ask user for choice
    response = input(question).lower()
    if response == 'r' or response == 'rock':
      response = 'Rock'
      print('You selected {}'.format(response))
    elif response == 'p' or response == 'paper':
      response = 'Paper'
      print('You selected {}'.format(response))
    elif response == 's' or response == 'scissors':
      response = 'Scissors'
      print('You selected {}'.format(response))
    else:
      print(error)
#Main Routine
user_choice = ""
rps_list = ['rock', 'paper', 'scissors']
while user_choice != 'xxx':
  user_choice = choice_checker("Choose rock, paper, or scissors: ")