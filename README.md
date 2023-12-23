# Battleship
Battleship is an exciting game that can be played by anyone looking for a challenge.

The aim of Battleship is to be a engaging game and easy to understand so that players have a good time.
This is done by explaining the game's mechanic in a clearly and graphical manner.

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

    ![Game statistics](docs/images/04-gamestats.png)

- __Feedback__
    - After every turn, a message will be displayed to let the player know if their shot hit or miss a ship.
    - The game statistics are updated and displayed.
    - The board is updated to show the respective character ("X" for hit, "O" for miss).
    - At the very top of the terminal screen, the player can see their last shot coordinates.

    ![Feedback](docs/images/05-hit-board-update.png)

- __Input validation and error-checking__
    - For an improved user experience, all inputs are validated:
        - The player's name/nickname must be have a length 1 and 20 characters.
        ![Name validation](docs/images/06-name-validation.png)
        
        - The row and column must be an integer that is inside the board.
        - The game asks the player for new coordinates when guessing the same location twice.
        ![Coordinates validation](docs/images/07-coord-validation.png)

- __Game Result__
    - Battleship will congratulate the player if all ships were destroyed:
    ![Victory](docs/images/08-victory.png)

    - Battleship will let the player when they ran out of turns and ships are still floating:
    ![Defeat](docs/images/09-defeat.png)

    - After the game's result, Battlefield asks the player if they would like to play again.