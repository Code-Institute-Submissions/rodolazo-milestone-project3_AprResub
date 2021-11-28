import random

def system_card():
  """Get a random card from list"""
  list_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(list_cards)
  return card


print(system_card())



