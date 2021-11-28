import random
import os
from design import texto

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
        list_cards.append(1)

    return sum(list_cards)

def compare_score(my_score, system_score):
  """ Compares system score and personal score and decide who wins"""
  if my_score > 21 and system_score > 21:
    return "You lose. You went over"

  if my_score == system_score:
    return "Draw"  
  elif my_score == 0:
    return "You win, you got a 21"
  elif my_score > 21:
    return "You lose, you went over 21"
  elif system_score == 0:
      return "You lose, the system got a 21"  
  elif system_score > 21:
    return "You win, the system went over 21"
  elif my_score > system_score:
    return "You win"
  else:
    return "You lose"

def screen_clear():
   # Clean console screen 
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def main():
    #Get two cards using the function random_card()
    mycards_list = []
    system_list = []
    is_over = False

    for item in range(2):
            mycards_list.append(random_card())
            system_list.append(random_card())

    # Let the user to ask for another card and stop the game when is 21 or over
    while not is_over:
        mycards_score = get_score(mycards_list)
        system_score = get_score(system_list)

        print(f"The first card of the system is {system_list[0]}")
        print(f"My cards are: {mycards_list} and my score is {mycards_score}")

        if mycards_score == 0 or mycards_score >21 or system_score == 0:
            is_over = True
        else:
            ask_card = input("Type 'y' to get another card or 'n' to finish the game: ").lower()
            if ask_card == 'y':
                mycards_list.append(random_card())
            else:
                is_over = True

    #If the system score is less than 17 then has to deal a new card
    while system_score != 0 and system_score < 17:
        system_list.append(random_card())
        system_score = get_score(system_list)

    #Print Final result
    print(f"They system cards are: {system_list} and its score is: {system_score}")
    print(f"Your cards are: {mycards_list} and your score is: {mycards_score}")
    print(compare_score(mycards_score, system_score))


#Ask to play the game again
while input("Would you like to play 21 game? <y> or <n>: ").lower() == 'y':
    screen_clear()
    print(texto)
    main()












