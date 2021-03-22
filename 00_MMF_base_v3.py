# import statements
import re
ImportError


# functions go here

# checks that ticket name is not blank
def not_blank(question):
    valid = False

    while not valid:
        response = input(question)

        # If name is not blank, program continues
        if response != "":
            return response
        else:
            print("Sorry - this can't be blank")


# checks for an interger more than 0
def int_check(question):
    error = "Please enter a whole number that is more than 13 and 130"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks number of tickets left and warns user
# if maximum is being approached
def check_tickets(tickets_sold, ticket_limit):
  # tells user how many seats are left
  if tickets_sold < ticket_limit - 1:
    print("You have {} seats "
          "left".format(ticket_limit - tickets_sold))
  
  # warns user that only one seat is left!
  else:
    print("*** There is ONE seat left!! ***")
  
  return""


# gets ticket price based on age
def get_ticket_price():

  #get age (between 12 and 130)
  age = int_check("Age: ")

  # check that age is valid...
  if age < 12:
      print("sorry you are too young for this movie")
      return "invalid ticket price"
  elif age > 130:
      print("That is very old - it looks like a mistake")
      return "invalid ticket price"

  if age < 16:
      ticket_price = 7.5
  elif age < 65:
      ticket_price = 10.5
  else:
      ticket_price = 6.5


# ********** Mian routine ***********

# set up dictionaries / lists needed to hold data

# initialise lists (to make data-frame in due cource)
all_names = []
all_tickets = []
  