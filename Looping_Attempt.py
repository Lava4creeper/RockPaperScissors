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
          user_choice()
        else:
          print(error)
      except ValueError:
        print(error)
    else:
      print("You have selected continuous mode")
      user_choice()
def user_choice():
  while True:
    rps_choice = input("Please select Rock (r), Paper (p) or Scissors (s)").lower()
    if rps_choice == 'r' or rps_choice == 'rock':
      rps_choice = "rock"
      print("You have selected {}".format(rps_choice))
    elif rps_choice == 's' or rps_choice == 'scissors':
      rps_choice = "scissors"
      print("You have selected {}".format(rps_choice))
    elif rps_choice == 'p' or rps_choice == 'paper':
      rps_choice = "paper"
      print("You have selected {}".format(rps_choice))
    else:
      print('Error. {} is not a valid input. Please enter Rock (r), Paper (p) or Scissors (s)'.format(rps_choice))
check_rounds()