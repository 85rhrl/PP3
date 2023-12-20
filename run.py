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
            return "Great! You hit one ship!"
        else:
            return "Dang! You missed"
    
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
    pass

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
    pass

def play_game(player_board):
    pass

def new_game():
    """
    Prints the logo and starts a new game.
    """
    logo()
    board_size = 5
    num_ships = 5
    print("#" * 35)
    print(" Welcome to Battleship!")
    print(f" Board size: {board_size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("#" * 35)
    player_name = input("Please enter your name/nickname: \n")
    print("-" * 35)
    
    player_board = Game(board_size, num_ships, player_name)

    for ship in range(num_ships):
        print(f"Ship {ship+1} of {num_ships}")
        populate_board(player_board)
    
    play_game(player_board)

new_game()