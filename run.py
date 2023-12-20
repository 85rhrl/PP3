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

#logo()

class Game:
    """
    Sets the game
    """

    def __init__(self, type):
        self.board_size = 5
        self.num_ships = 5
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