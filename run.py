from random import randint

def logo():
    """ Battleship logo """

    print(r"""
    ╔╗ ┌─┐┌┬┐┌┬┐┬  ┌─┐┌─┐┬ ┬┬┌─┐        # #  ( )
    ╠╩╗├─┤ │  │ │  ├┤ └─┐├─┤│├─┘     ___#_#___|__
    ╚═╝┴ ┴ ┴  ┴ ┴─┘└─┘└─┘┴ ┴┴┴   _  |____________|  _
                          _=====| | |            | | |==== _
                    =====| |.---------------------------. | |====
      <--------------------'   .  .  .  .  .  .  .  .   '--------------/
        \                                                             /
         \_______________________________________________WWS_________/""")

class Game:
    """
    Sets the game
    """

    def __init__(self, board_size, num_ships, player_name):
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_name = player_name
        self.board = [["-" for x in range(board_size)] for y in range(board_size)]
        self.guesses = []
        self.ships = []
    
    def print_it(self):
        """ Prints only the contents of the board's list with white spaces in-between """
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            print("Great! You hit one ship!")
            return True
        else:
            print("Dang! You missed")
            return False
    
    def add_ship(self, x, y):
        if len(self.ships) >= self.num_ships:
            print("Error: you can't add more ships!")
        else:
            self.ships.append((x, y))

def random_point(board_size):
    """
    Helper function to return a random integer between 0 and board_size
    """
    return randint(0, board_size -1)

def valid_coordinates(x, y, board):
    """
    Validates the coordinates from player
    """
    try:
        # Convert str to int
        x = int(x)
        y = int(y)
        # Coordinates inside board?
        board.board[x][y] in board.board
    
    except ValueError:
        print("Please enter an integer number.")
        return False
    
    except IndexError:
        print(f"Please enter an integer between 0 and {board.board_size-1}.")
        return False
    
    finally:
        if (x, y) in board.guesses:
            print("You have already guessed that location, try another.")
            return False
    
    return True


def populate_board(board):
    ship_x = random_point(board.board_size)
    ship_y = random_point(board.board_size)
    print(ship_x, ship_y)
    # Check if there is a ship in that location
    while (ship_x, ship_y) in board.ships:
        print("Ship already in that location, trying again")
        ship_x = random_point(board.board_size)
        ship_y = random_point(board.board_size)
        print(ship_x, ship_y)
    board.add_ship(ship_x, ship_y)
    print("Ship added")

def make_guess(board):
    """
    Gets input from user and calls valid_coordinates
    """

    while True:
        x = input("Please enter row: ")
        y = input("Please enter column: ")
        if valid_coordinates(x, y, board):
            # Convert to int
            x = int(x)
            y = int(y)
            board.guess(x, y)
            return x, y
            break


def play_game(player_board, num_turns, num_ships):
    num_hits = 0

    while num_turns > 0 and num_hits < num_ships:
        print(f"Turns left: {num_turns}")
        print(f"Battleships still floating: {num_ships - num_hits}")
        player_board.print_it()
        x, y = make_guess(player_board)
        print(player_board.guesses)
        print(player_board.ships)
        if player_board.guess(x, y):
            num_hits += 1
            print(f"number of hits: {num_hits}")
        num_turns -= 1
    
    if num_hits == num_ships:
        print("YOU WIN!!!")
    else:
        print("YOU LOSE!!!")
        

def new_game():
    """
    Prints the logo and starts a new game.
    """
    logo()
    board_size = 5
    num_ships = 5
    num_turns = 10
    print("#" * 35)
    print(" Welcome to Battleship!")
    print(f" Board size: {board_size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("#" * 35)
    player_name = input("Please enter your name/nickname: \n")
    print("-" * 35)
    
    player_board = Game(board_size, num_ships, player_name)
    player_board.print_it()
    for ship in range(num_ships):
        print(f"Ship {ship+1} of {num_ships}")
        populate_board(player_board)
    
    #x, y = make_guess(player_board)
    #print(player_board.guesses)
    #print(player_board.ships)
    play_game(player_board, num_turns, num_ships)
    #player_board.print_it()

new_game()