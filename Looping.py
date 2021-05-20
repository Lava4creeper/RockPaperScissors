def check_rounds():
  while True:
    response = input('How many rounds: ')

    round_error = 'Please type either <enter> or an integer that is more than 0'
    if response != "":
      try:
        response = int(response)
        print(response)
        if response < 1:
          print(round_error)
          print(response)
      except ValueError:
        print(round_error)
        print(response)
    else:
      print("Infinite")
check_rounds()