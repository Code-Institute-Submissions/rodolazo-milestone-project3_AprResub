import random

def random_card():
  """Get a random card from list"""
  list_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(list_cards)
  return card

def get_score(list_cards):
    """Get the sum of the cards Return 0 if you get 21"""
    if sum(list_cards) == 21 and len(list_cards) == 2:
        return 0

    if sum(list_cards) > 21 and 11 in list_cards:
        list_cards.remove(11)
        list_card.append(1)

    return sum(list_cards)


mycards_list = []
system_list = []

for item in range(2):
    mycards_list.append(random_card())
    system_list.append(random_card())

mycards_score = get_score(mycards_list)
system_score = get_score(system_list)

print(f"The first card of the system is {system_list[0]}")
print(f"My cards are: {mycards_list} and my socre is {mycards_score}")






