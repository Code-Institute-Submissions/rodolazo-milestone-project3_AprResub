# 21 GAME

Equally well known as Twenty-One, the objective of this game is to attempts to beat the dealer that in this case is going to be the system by getting a count as close to 21 as possible, without going over 21.

![21 Game ](https://raw.githubusercontent.com/rodolazo/milestone-project3/main/images/responsive.png)

## Card values/scoring
It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value.

## Betting
At the beginning of the game the player and the system receive two cards. The first card of the system is visible for the user. After that the program is going to request the user if he wants another card

## Rules
* If both the system and the user go over 21, the user lose the game
* If both have the same score , it is a draw
* If both are below 21 and both have differents scores, The winner is the one with the highest score

## Features
* When the game starts there is a nice logo printed in the console
![Logo](https://raw.githubusercontent.com/rodolazo/milestone-project3/main/images/logo.png)
* To get the previous logo I used the online tool [Text to ASCII generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something)
![Text to ASCI](https://raw.githubusercontent.com/rodolazo/milestone-project3/main/images/logogenerator.png)

* The main scrit have the following functions:
    * random_card() . This function acts like the dealer, and its function is to get a random card
    * get_score(). This function calculate the sum of all the cards
    * compare_score(). This function decides who is the winner
    * screen_clear() . This function clear the console screen everytime the user decides to play again
    * main() . This is the main function and its function is to initialize the game and call all the functions

## Testing
- Python
    - No syntax errors were founded
    ![Python Validator](https://raw.githubusercontent.com/rodolazo/milestone-project3/main/images/errors.png)

## Deployment
- The siste was deployed to Heroku
![Heroku](https://raw.githubusercontent.com/rodolazo/milestone-project3/main/images/21game.png)

## Credits
- To clear the console so that everytime the user decides to play again I used the code offered by Tutorialspoint in the following [link](https://www.tutorialspoint.com/how-to-clear-screen-in-python)
- No external libraries were used

## Future improvements
- Normally, when this game is played, all the cards used in one game are removed from the deck, and that is a real advantage for people like and know how to count cards. In this case the likelihood to have any card are all the time the same, so it would be a nice feauture to be include in a future release.


