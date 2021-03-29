import pandas

# intialise 

all_names = ['Rangi', 'Manaia', 'Kini', 'Havaka', 'Cameron']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Data Frame Dicttionary
movie_data_dict = {
  'Name': all_names,
  'Popcorn': popcorn,
  'Water': water,
  'Pita Chips': pita_chips,
  'M&Ms': mms,
  'Orange Juice': orange_juice
  }

test_data = [
  [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
  [[1, 'Popcorn'], [1, 'Orange Juice'], [2, 'M&Ms']],
  [[1, 'Water'], [1, 'Orange Juice']],
  [[2, 'Popcorn'], [1, 'Water']],
  [[2, 'Pita Chips']]
]

count = 0
for client_order in test_data:

  # Assume no snacks have been bought...
  for item in snack_lists:
    item.append(0)
  
  # print(snack_lists)

  # Get order (hard coded for easy testing)...
  snack_order = test_data[count]
  count += 1

  for item in snack_order:
    if len(item) > 0:  
      to_find = (item[1])
      amount = (item[0])
      add_list = movie_data_dict[to_find]
      add_list[-1] = amount

print()
print("Names:", all_names)
print("Popcorn: ", snack_lists[0])
print("M&Ms:", snack_lists[1])
print("Pita Chips:", snack_lists[2])
print("Water:", snack_lists[3])
print("Orange Juice", snack_lists[4])
print()
# print details...
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')
print(movie_frame)