
import re
import pandas


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

  return ticket_price 

# functions go here
def string_check(choice, options):

  for var_list in options:

    # if the snack is in one of the lists, return the full 
    if choice in var_list:

      # Get full name of snack and put it
      # in title case so it looks nice when outputted
      chosen = var_list[0].title()
      is_valid = "Yes"
      break

    # If the chosen is not valid, set is_valid to no
  else:
    is_valid = "No"

  # if the snack is not OK - ask question again
  if is_valid == "Yes":
    return chosen
  else:
    print("Sorry that is not a valid options\n")
    return "invalid choice"


# ********** Main routine ***********

# set up dictionaries / lists needed to hold data

# intialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

# lists for string checking function etc

valid_snacks = [
  ["popcorn", "p", "corn", "a"],
  ["M&M's", "m&m's", "mms", "m", "b"],  # first item is M&M
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "d"],
  ["orange juice", "orange", "juice", "oj", "j"]
]

yes_no = [
  ["yes", "y"],
  ["no", "n"] 
]

# regular expression to find if item starts with a number
number_regex = "^[1-9]"

# initialise lists (to make data-frame in due cource)
all_names = []
all_tickets = []


popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# holds all snack orders...
snack_order = []

# Data Frame Dicttionary
# Data Frame Dictionary
movie_data_dict = {
  'Name': all_names,
  'Ticket': all_tickets,
  'Popcorn': popcorn,
  'Water': water,
  'Pita Chips': pita_chips,
  'M&Ms': mms,
  'Orange Juice': orange_juice
}

# cost of each snack
price_dict = {
  'Popcorn': 2.5,
  'Water': 2,
  'Pita Chips': 4.5,
  'M&Ms': 3,
  'Orange Juice': 3.25
}


# Ask user if they have used the progarm before & show instructions

# Loop to get ticket details
while name != "xxx" and ticket_count < MAX_TICKETS:

  # list to hold snack order, gets reset for each open
  snack_row = []

  # check numbers of ticket limit has not been exceeded...
  check_tickets(ticket_count, MAX_TICKETS)

  # **** Get details for each ticket... ****

  # Get name (cant be blank)
  name = not_blank("Name: ")

  # end the loop if the exit code is entered
  if name == "xxx":
    break

  # get ticket price based on age
  ticket_price = get_ticket_price()
  # if age is invalid, restart loop (and get name again)
  if ticket_price == "invalid ticket price":
    continue

  ticket_count += 1
  ticket_sales += ticket_price

  # add name and ticket price to lists
  all_names.append(name)
  all_tickets.append(ticket_price)

  # get snacks
# ask user if they want a snack 
check_snack = "invalid choice"
while check_snack == "invalid choice":
  want_snack = input("Do you want to order snacks? ").lower()
  check_snack = string_check(want_snack, yes_no)

  # If they say yes, ask what snacks they want (and add to our snack list)
  if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
      
      snack_row = []
      
      # ask user for desired snack and put it in lowercase
      desired_snack = input("Snack: ").lower()

      if desired_snack == "xxx":
        break
      
      # if item has a number, separate it into 2 (number / snack)
      if re.match(number_regex, desired_snack):
        amount = int(desired_snack[0])
        desired_snack = desired_snack[1:]
      
      else:
        amount = 1
        desired_snack = desired_snack
      
      # remove white space around snack
      desired_snack = desired_snack.strip()

      # check if snack is valid
      snack_choice = string_check(desired_snack, valid_snacks)
      print("Snack Choice: ", snack_choice)

      # check snack amount is valid (less than 5)
      if amount >= 5:
        print("Sorry - we have a four snack maximum")
        snack_choice = "invalid choice"

      # add snack And amount to list...
      snack_row.append(amount)
      snack_row.append(snack_choice)

      # check that snack is not the exit code before adding
      if snack_choice != "xxx" and snack_choice != "invalid choice":
        snack_order.append(snack_row)



  # get payment method (ie: work out if surcharge is needed)

# End of ticket / snacks / payment Loop 

# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

# calculate ticket porfit...
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

# Tell user if they have unsold tickets...
if ticket_count == MAX_TICKETS:
  print("You have sold all available tickets!")

else:
  print("You have sold {} tickets.  \n"
        "There are {} places still available".format(ticket_count,
                                                      MAX_TICKETS - ticket_count))
