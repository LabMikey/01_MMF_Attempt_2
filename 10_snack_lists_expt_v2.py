# intialise 

names = ['Rangi', 'Manaia', 'Kini', 'Havaka', 'Cameron']

popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

snack_menu_dict = {
  'Popcorn': popcorn,
  'Water': water,
  'Pita chips': pita_chips,
  'M&Ms': mms,
  'Orange Juice': orange_juice
}

test_data = [
  [[2, 'Popcorn'], [1, 'Pita Chips'], [1, 'Orange Juice']],
  [[1, 'Pita Chips'], [1, 'Orange Juice'], [2, 'M&Ms']],
  [[1, 'Water']]
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
      add_list = snack_menu_dict[to_find]
      add_list[-1] = amount

print(snack_lists)