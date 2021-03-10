def yes_no(question):
  error = "please answer yes / no"

  valid = False
  while not valid:
    # ask question and put pesponse in lowercase
    response = input(question).lower()

    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
        print(error)

# main routine goes here
for item in range(0, 6):
  want_snacks = yes_no("Do you want any snacks? ")
  print("Answer OK, you said", want_snacks)
  print()