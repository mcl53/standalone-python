from random import randint
import os
import time


class Board:
    def __init__(self):
        board = []
        for x in range(4):
            board.append(["O"] * 4)
        self.board = board
        ships = []
        self.ships = ships


players = []


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


class Player:
    def __init__(self, p_num):
        clear()
        name = input("Player " + str(p_num) + ", enter your name: ")
        self.name = name
        self.board = Board()
        players.append(self)
        sunk_count = 0
        self.sunk = sunk_count


player_1 = Player(1)
player_2 = Player(2)


def print_board(player_in):
    for row in player_in.board.board:
        print(" ".join(row))
    print()


def print_after_guess(player_in, turn_in):
    clear()
    print("Turn", turn_in)
    print(player_in.name)
    print_board(player_in)


def other_player(player_in):
    for x in players:
        if player_in.name != x.name:
            return x.name


def random_row(board_in):
    return randint(0, len(board_in.board) - 1)


def random_col(board_in):
    return randint(0, len(board_in.board[0]) - 1)


for player in players:
    ship_r_one = random_row(player.board)
    ship_c_one = random_col(player.board)

    ship_one = (ship_r_one, ship_c_one)
    player.board.ships.append(ship_one)

    ship_r_two = ship_r_one
    ship_c_two = ship_c_one

    while ship_r_two == ship_r_one and ship_c_two == ship_c_one:
        ship_r_two = random_row(player.board)
        ship_c_two = random_col(player.board)

    ship_two = (ship_r_two, ship_c_two)
    player.board.ships.append(ship_two)

    ship_r_three = ship_r_one
    ship_c_three = ship_c_one

    while (ship_r_three == ship_r_one and ship_c_three == ship_c_one) or (ship_r_three == ship_r_two and ship_c_three == ship_c_two):
        ship_r_three = random_row(player.board)
        ship_c_three = random_col(player.board)

    ship_three = (ship_r_three, ship_c_three)
    player.board.ships.append(ship_three)


#for i in players:
 #   print(i.board.ships)


def hit_ship(guess_in, player_in):
    ship_hits = []
    index = 0
    for i in player_in.board.ships:
        ship_hits.append(0)
        if guess_in == i:
            ship_hits[index] = 1
        index += 1
    if 1 in ship_hits:
        return True
    else:
        return False


winner = False
for turn in range(1, 100):
    if winner:
        break
    for player in players:
        other_p = other_player(player)
        time.sleep(5)
        print_after_guess(player, turn)
        try:
            guess_row = int(input("Guess Row: ")) - 1
            guess_col = int(input("Guess Col: ")) - 1
            is_num = True
        except ValueError:
            print_after_guess(player, turn)
            print("Please guess a number")
            is_num = False
        if is_num:
            guess = (guess_row, guess_col)
            hit = hit_ship(guess, player)
            if hit and player.board.board[guess_row][guess_col] != "*":
                player.board.board[guess_row][guess_col] = "*"
                print_after_guess(player, turn)
                print("Congratulations! You sunk " + other_p + "'s battleship!")
                player.sunk += 1
                if player.sunk == 3:
                    print(player.name + " sank all three ships")
                    print(player.name + " is the winner!")
                    winner = True
                    break
            elif hit and player.board.board[guess_row][guess_col] == "*":
                print_after_guess(player, turn)
                print("You got that one already")
            else:
                if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                    print_after_guess(player, turn)
                    print("Oops, that's not even in the ocean.")
                elif player.board.board[guess_row][guess_col] == "X":
                    print_after_guess(player, turn)
                    print("You guessed that one already.")
                else:
                    player.board.board[guess_row][guess_col] = "X"
                    print_after_guess(player, turn)
                    print("You missed " + other_p + "'s battleship!")


# Suggestions of additions:
# 1.) Two player game + allow the player to enter their name - COMPLETE
# 2.) Allow the player to pick the location of battleships
# 3.) Display the grid coordinates on the side of the board
# 4.) Different sizes of ships
# 5.) Rematches and statistics and stuff
