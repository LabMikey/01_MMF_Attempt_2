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


# *************  Main Routine *************

# Set up dictionaries / Lists needed to hold data

# Ask user if they have used the program before & and show instructions of necessary

# Loop to get ticket details
        # start of loop

        # initialise loop so that it runs at least once
        name = ""
        count = 0
        MAX_TICKETS = 5

        while name != "xxx" and count < MAX_TICKETS:

            # tells user how many seats are left
            if count < 4:
                print("you have {} seats "
                      "left".format(MAX_TICKETS - count))

            # Warns user that only one seat is left!
            else:
                print("*** There is ONE seat left!! ***")

            # Get details...

            # Get name (can't be blank)
            name = input("name:")
            count += 1
            print()

        if count == MAX_TICKETS:
            print("You have sold all the available tickets!")
        else:
            print("You have sold {} tickets.  \n"
                  "There are {} places still available"
                  .format(count, MAX_TICKETS - count))


            # Get ticket holder name and check its not blank
        name = not_blank("Name: ")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method (and apply surcharge of necessary)



# Calculate Total sales and profit

# Output data to text file

