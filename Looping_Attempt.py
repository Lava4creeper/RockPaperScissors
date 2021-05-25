#defining my functions
def check_rounds():
  while True:
    error = "Please press <enter> for continuous mode or enter a whole number bigger than 0"
    response = input("How many rounds would you like to play?")
    if response != "":
      try:
        response = int(response)
        if response > 0:
          print("You have selected {} rounds.".format(response))
          user_choice(response)
        else:
          print(error)
      except ValueError:
        print(error)
    else:
      print("You have selected continuous mode")
      user_choice()
def user_choice(total_rounds):
  while True:
    rps_user = input("Please select Rock (r), Paper (p) or Scissors (s)").lower()
    if rps_user == 'r' or rps_user == 'rock':
      rps_user = "rock"
      print("You have selected {}".format(rps_user))
      rps_user = 1
      rps_computer(total_rounds, rps_user)
    elif rps_user == 'p' or rps_user == 'paper':
      rps_user = "paper"
      print("You have selected {}".format(rps_user))
      rps_user = 2
      rps_computer(total_rounds, rps_user)
    elif rps_user == 's' or rps_user == 'scissors':
      rps_user = "scissors"
      print("You have selected {}".format(rps_user))
      rps_user = 3
      rps_computer(total_rounds, rps_user)
    elif rps_user == 'xxx':
      print('Exit code "xxx" used.' )      
    else:
      print('Error. {} is not a valid input. Please enter Rock (r), Paper (p) or Scissors (s)'.format(rps_user))
def rps_computer(total_rounds, rps_user):
  import random
  rps_computer = random.randint(0, 3)
  if rps_computer == 1:
    print('Computer has selected "rock"')
    computer_vs_user(total_rounds, rps_user, rps_computer)
  elif rps_computer == 2:
    print('Computer has selected "paper"')
    computer_vs_user(total_rounds, rps_user, rps_computer)
  elif rps_computer == 3:
    print('Computer has selected "scissors"')
    computer_vs_user(total_rounds, rps_user, rps_computer)
def computer_vs_user(total_rounds, rps_user, rps_computer):
#  while rps_user != 'xxx':
    if rps_user == 1:
      if rps_computer == 1:
        print("Rock vs Rock! It's a tie!")
      elif rps_computer == 2:
        print("Rock vs Paper! Computer wins!")
      else:
        print("Rock vs Scissors! Player Wins!")
    if rps_user == 2:
      if rps_computer == 1:
        print("Paper vs Rock! Player wins!")
      elif rps_computer == 2:
        print("Paper vs Paper! It's a tie!")
      else:
        print("Paper vs Scissors! Computer Wins!")
    if rps_user == 3:
      if rps_computer == 1:
        print("Scissors vs Rock! Computer Wins!")
      elif rps_computer == 2:
        print("Scissors vs Paper! Player Wins!")
      else:
        print("Scissors vs Scissors! It's a tie!")


check_rounds()