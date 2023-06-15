# Battleships Game

[Click here to visit the live page.](https://battleships-game-ts.herokuapp.com/)

This game is a Battleships Game created using Python and runs in the Code Institute mock terminal on Heroku.

To read about original battleships game [click here.](https://en.wikipedia.org/wiki/Battleship_(game))

In this game both players (user, computer) has a grid/board of 4x4 and 3 ships. The goal is to guess the opponent ship's coordinates first. In this version every ship occupies only one field.


## User Stories ##

* As a visiting user i would like to set a user name.

* As a visiting user i would like to avoid any errors if i insert invalid data.

* As a visiting user i would like to see, what is happening after every turn. (e.g: Points and board updated)

* As a visiting user i would like to have an obvius indication when the game finished.


## Target audiance ##

* People whom interested in playing a simple online game.

* People whom interested in playing a game that mainly depends on luck.

## Features ##

* Automatically created boards for both players.

![screenshot of the game when boards printed](/docs/printed-boards.png)

* The player can insert a user name.

* The ships are randomly placed and the player can not see where the computer's ships are.

* The player can see her/his ships

* Input validation so that the user can not insert coordinates, that are not within the grid's size or guess the same coordinates twice.

* A message indicates after guessing if it was a hit or missed both foe player and computer.

* A message indicates when someone wins the game.

* After the game ends the player easily can start a new game or finish the game.

## Future features ##

* The player can select the size of the board.

* The user can select the number of the ships.

* The user can place her/his own ships.

* There will be bigger ships than 1 field.


## Planning ##

I used a chart to make easyer to build the game logic.

![screenshot of the chart created for game logic.](/docs/battleships-chart.png)


## Bugs ##

* I did not check for ship coordinates when placing multiple ships so sometimes i had just two ships on a grid.
    * Solved by checking if the coordinates are already on the grid.

## Remaining Bugs ##

* There is not any bugs remained.

## Validator Testing ##

* PEP8
    * No error were found with CI Python Linter

    ![screenshot of the python linter result.](/docs/python-linter.png)

## Testing ##

* The code were passed through the Code Institute PEP8 linter and no error were found.
* The game tested manually no invalid input accepted and the user can not guess the same twice.
* Ships placed as expected.
* Points and grids always updated as expected.
* When game ends winner printed and if selected game reset as expected.

* Negative coordinates inserted:
    * ![screenshot of invalid negative input message.](/docs/negativ-value-input.png)

* Too high or invalid data inserted for coordinates:
    * ![screenshot of invalid coordinates message.](/docs/invalid-coordinates.png)

* Same coordinate again:
    * ![screenshot of same coordinates message.](/docs/same-coordinates.png)

* Invalid input when asking if new game:    
    * ![screenshot of invalid inputs when new game.](/docs/incorrect-input-newgame.png)

* Winner displayed:
    * ![screenshot of winner printed.](/docs/winner-indicated.png)

## Deployment ##

* This project was deployed isung Code Institute's mock terminal for Heroku.

* Steps for deployment:
    * Fork or clone this repository
    * Create a new Heroku app
    * Set the buildpacks to Python and NodeJS in that order
    * Reveal config vars and set the key to PORT and the value to 8000
    * Link Heroku app to the repository
    * Click on Deploy


## Credits ##

* Code Institute for the deployment terminal
* Code Institute project example readme
* [W3 Scools](https://www.w3schools.com/) when i was struggling with something. 




