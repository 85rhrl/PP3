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

    def __init__(self, board_size, num_ships, player_name, type):
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_name = player_name
        self.type = type
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
    
    def add_ship(self, x, y, type="cpu"):
        if len(self.ships) >= self.num_ships:
            print("Error: you can't add more ships!")
        else:
            self.ships.append((x, y))
            # Mark ships with "S" on player's board
            if self.type == "player":
                self.board[x][y]: "S"

def random_point(board_size):
    """
    Helper function to return a random integer between 0 and board_size
    """
    return randint(0, board_size -1)

def valid_coordinates(x, y, board):
    pass

def populate_board(board):
    pass

def make_guess(board):
    pass

def play_game(cpu_board, player_board):
    pass

def new_game():
    """
    Prints the logo and starts a new game.
    """
    logo()
    board_size = 5
    num_ships = 5
    scores["cpu"] = 0
    scores["player"] = 0
    print("#" * 35)
    print(" Welcome to Battleship!")
    print(f" Board size: {board_size}. Number of ships: {num_ships}")
    print(" Top left corner is row: 0, col: 0")
    print("#" * 35)
    player_name = input("Please enter your name/nickname: \n")
    print("-" * 35)

    cpu_board = Game(board_size, num_ships, "CPU", type="cpu")
    player_board = Game(board_size, num_ships, player_name, type="player")

    for ship in range(num_ships):
        populate_board(player_board)
        populate_board(cpu_board)
    
    play_game(cpu_board, player_board)