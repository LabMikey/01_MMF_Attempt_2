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

    # Get ticket holder name and check its not blank
        name = not_blank("Name: ")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # ask for payment method (and apply surcharge of necessary)



# Calculate Total sales and profit

# Output data to text file

