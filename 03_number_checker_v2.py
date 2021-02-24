# functions go here


# checks for an interger more than 0
def int_check (question):
    error = "Please enter a whole nuber that is more than 13 and 130"

    valid = False
    while not valid:

        # ask user for number and check it is valid
        try:
            response = int(input(question))

            if response <= 0:
                print(error)
                else:
                    return response
