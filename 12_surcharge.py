import re
import pandas


# Function goes here 
# WANRING: The response is returned in Title case
# functions go here
def string_checker(choice, options):

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


# Main routine

pay_method = [
  ["cash", "ca"],
  ["credit", "cr"]
]

# loop until exit code...
name = ""
while name != "xxx":
  name = input("Name: ")
  if name == "xxx":
    break
  
  # Ask for payment method
  how_pay = "invalid choice"
  while how_pay == "invalid choice":
    how_pay = input("Please choose a payment method (cash / credit)? ").lower()
    how_pay = string_checker(how_pay, pay_method)

  # Ask for sub total (for testing purposes)
  subtotal = float(input("Sub total? $"))

  if how_pay == "Credit":
    surcharge = 0.05 * subtotal
  else:
    surcharge = 0

  total = subtotal + surcharge
    
  print("Name: {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} | " 
        "Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))



