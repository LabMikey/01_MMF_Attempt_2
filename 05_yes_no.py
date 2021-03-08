def yes_no(question):
  error = "please answer yes / no"

  valid = False
  while not valid:
    # ask question and put pesponse in lowercase
    response = input(question).lower()

    if response == "Yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
        print(error)

# main routine