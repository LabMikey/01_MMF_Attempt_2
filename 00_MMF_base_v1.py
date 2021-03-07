# import statements


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

# checks for an interger between two values

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

# *************  Main Routine *************

# Set up dictionaries / Lists needed to hold data

# Ask user if they have used the program before & and show instructions of necessary

# Loop to get ticket details
        # start of loop

# initialise loop so that it runs at least once
MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0


while name != "xxx" and ticket_ticket_count < MAX_TICKETS:

    # tells user how many seats are left
    if ticket_count < MAX_TICKETS - 1:
        print("you have {} seats "
              "left".format(MAX_TICKETS - ticket_count))

    # Warns user that only one seat is left!
    else:
        print("*** There is ONE seat left!! ***")

    # Get details...

    # Get name (can't be blank)
    name = not_blank("Name:")

    # end loop if the exit code is entered
    if name == "xxx":
        break

    # main routine goes here
    age = int_check("Age: ")

    # check that age is valid...
    if age < 12:
        print("sorry you are too young for this movie")
        continue
    elif age > 130:
        print("That is very old - it looks like a mistake")
        continue

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price

ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit:")

if ticket_count == MAX_TICKETS:
    print("You have sold all the available tickets!")
else:
    print("You have sold {} tickets.  \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))

            # Get ticket holder name and check its not blank


    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method (and apply surcharge of necessary)



# Calculate Total sales and profit

# Output data to text file

