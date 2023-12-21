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
~~~~~~~~~\___________________________________________________________/~~~~~~~~~~""")

def victory():
    """ Victory text """

    print(r"""
 `7MMF'   `7MF'`7MMF' .g8'''bgd MMP""MM""YMM   .g8""8q. `7MM'''Mq.`YMM'   `MM'
   `MA     ,V    MM .dP'     `M P'   MM   `7 .dP'    `YM. MM   `MM. VMA   ,V  
    VM:   ,V     MM dM'       `      MM      dM'      `MM MM   ,M9   VMA ,V   
     MM.  M'     MM MM               MM      MM        MM MMmmdM9     VMMP    
     `MM A'      MM MM.              MM      MM.      ,MP MM  YM.      MM     
      :MM;       MM `Mb.     ,'      MM      `Mb.    ,dP' MM   `Mb.    MM     
       VF      .JMML. `"bmmmd'     .JMML.      `"bmmd"' .JMML. .JMM. .JMML.""")

def defeat():
    """ Defeat text """

    print(r"""
 `7MM'''Yb. `7MM'''YMM  `7MM'''YMM `7MM'''YMM        db   MMP""MM""YMM
   MM    `Yb. MM    `7    MM    `7   MM    `7       ;MM:  P'   MM   `7 
   MM     `Mb MM   d      MM   d     MM   d        ,V^MM.      MM      
   MM      MM MMmmMM      MM""MM     MMmmMM       ,M  `MM      MM      
   MM     ,MP MM   Y  ,   MM   Y     MM   Y  ,    AbmmmqMA     MM      
   MM    ,dP' MM     ,M   MM         MM     ,M   A'     VML    MM      
 .JMMmmmdP' .JMMmmmmMMM .JMML.     .JMMmmmmMMM .AMA.   .AMMA..JMML.""")

class Game:
    """
    Sets the game
    """

    def __init__(self, board_size, num_ships, player_name):
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_name = player_name
        self.board = [[" - " for x in range(board_size)] for y in range(board_size)]
        self.guesses = []
        self.ships = []
    
    def print_it(self):
        """ Prints only the contents of the board's list with white spaces in-between """
        for row in self.board:
            print(" ".join(row))
    
    def guess(self, x, y):
        self.guesses.append((x, y))
        
        if (x, y) in self.ships:
            self.board[x][y] = " X "
            return True
        else:
            self.board[x][y] = " O "
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
        print("\nPlease enter an integer number.")
        return False
    
    except IndexError:
        print(f"\nPlease enter an integer between 0 and {board.board_size-1}.")
        return False
    
    finally:
        if (x, y) in board.guesses:
            print("\nYou have already guessed that location, try another.")
            return False
    
    return True

def populate_board(board):
    ship_x = random_point(board.board_size)
    ship_y = random_point(board.board_size)
    print(ship_x, ship_y)
    # Check if there is a ship in that location
    while (ship_x, ship_y) in board.ships:
        ship_x = random_point(board.board_size)
        ship_y = random_point(board.board_size)
    board.add_ship(ship_x, ship_y)

def make_guess(board):
    """
    Gets input from user and calls valid_coordinates
    """

    while True:
        x = input("\nPlease enter row: ")
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
        print(f"\n Turns left: {num_turns}      Number of hits (X): {num_hits}       Battleships still floating: {num_ships - num_hits}\n")
        player_board.print_it()
        if num_turns == 1 and num_ships-num_hits == 1:
            print("\nLast turn, aim carefully!")
        #print(player_board.ships)
        x, y = make_guess(player_board)
        logo()
        if player_board.guess(x, y):
            print(f"\n Great job {player_board.player_name}! You hit one ship!")
            num_hits += 1
            if num_ships-num_hits == 1:
                print(" One more ship to destroy!")
        else:
            print(f"\n Dang {player_board.player_name}! You missed.")
        num_turns -= 1
        
    if num_hits == num_ships:
        victory()
    else:
        defeat()        

def new_game():
    """
    Prints the logo and starts a new game.
    """
    logo()
    board_size = 5
    num_ships = 5
    num_turns = 10
    print("~" * 80)
    print("                           Welcome to Battleship!")
    print(f"                     Board size: {board_size}. Number of ships: {num_ships}")
    print('    Top left corner is row: 0, col: 0.  On the board "O" = miss and "X" = hit')
    print("~" * 80)
    player_name = input("Please enter your name/nickname: \n")
    print("-" * 80)
    
    player_board = Game(board_size, num_ships, player_name)

    for ship in range(num_ships):
        populate_board(player_board)

    play_game(player_board, num_turns, num_ships)

new_game()
