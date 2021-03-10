
# Valid snacks hold list of all snacks
# Each item in valid snacks is a list with
# Valid options for each snack <full name, full letter (a - e)
# , and possible abbreviations etc>
valid_snacks = [
  ["popcorn", "p", "corn", "a"],
["M&M's", "m&m's", "mms", "m", "b"],  # first item is M&M
  ["pita chips", "chips", "pc", "pita", "c"],
  ["water", "w", "d"]


# initialise variables
snack_ok = ""
snack = ""

# loop three times to make testing quicker
for item in range(0, 3):

  # ask user for desired snack and put it in lowercase
  desired_snack = input("Snack: ").lower()

  for var_list in valid_snacks:

    # if the snack is one of the lists, return the full 
    if desired_snack in var_list:

      # get full name of snack 
