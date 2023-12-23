# Battleship
Battleship is an exciting game that can be played by anyone looking for a challenge.

The aim of Battleship is to be a engaging game and easy to understand so that the players have a good time.
This is done by explaining the game mechanics in a clearly and graphical manner.

Visit the deployed Battleship's game here: [https://pp3-85rhrl-771c69ab8a44.herokuapp.com/](https://pp3-85rhrl-771c69ab8a44.herokuapp.com/)

![Battleship! in different screen sizes](docs/images/amiresponsive.png)

## How to play
Battleship is a single player game based on the popular game from the same name which dates back to World War I, for more information about the original Battleship game, please visit its [Wikipedia page here](https://en.wikipedia.org/wiki/Battleship_(game)).

To play Battleship, simply start by typing down your name/nickname and hitting enter. A board will be generated and displayed with ships placed randomly which the player cannot see.

The game then asks the user to type in the row and column (known as coordinates) of the desired shot with the top left corner having row and column 0 and 0 respectively.

If the shot was a "Hit" or "Miss", the respective message is displayed and the board is updated with an "X" for a sunken ship or a "O" for a missed shot for the given coordinates. 

The objective is to sunk all ships before the player runs out of turns (missiles).

## Features

### Existing Features

- __Logo__
    - At the top of the terminal screen a Battleship image made by characters is displayed with the name of the game next to it.

    ![Logo](docs/images/01-logo.png)

- __Welcome message__
    - Below the logo a welcome message is displayed.
    - The game settings are displayed which include; Board size, number of ships and number of turns.
    - An explanation of how to target the rows and columns.
    - How are the Hit or Miss shots are displayed on the board.
    - The game's objective.

    ![Welcome message](docs/images/02-welcome.png)

- __Player's name__
    - To better address the player and give personalized messages, the game asks the player to type in their name.

    ![Player's name](docs/images/03-playername.png)

- __Game's statistics__
    - On every turn, the game's statistics (turns left, number of hits and ships remaining) are displayed so the player knows how they're doing.

    ![Player's name](docs/images/04-gamestats.png)

