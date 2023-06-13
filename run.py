import random

# index = 0 player, index 1 = computer
points = [0, 0]


class Grid:
    """
    A class to create the board and place the ship.
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.grid = [["*"] * size for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_grid(self):
        print(f"{self.name}'s board:")
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()
        print()

    def place_ship(self):
        self.ships = []
        ships_to_place = computers_grid.num_ships
        while ships_to_place > 0:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            if (x, y) in self.ships:
                continue

            if self.grid[x][y] == "*":
                self.ships.append((x, y))
                if self.type == "Player":
                    self.grid[x][y] = "S"
                ships_to_place -= 1
        return self.ships


print(30*"_")
print("\n Welcome to Battlesips Game!")
print(30*"_")
print()
player_name = input("What is your name?: ")
while not len(player_name) > 2:
    print("Please provide a name (min 3 characters): ")
    player_name = input("What is your name?: ")

players_grid = Grid(4, 3, player_name, type="Player")
computers_grid = Grid(4, 3, "Computer", type="Computer")
players_grid.place_ship()
players_grid.print_grid()
computers_ship = computers_grid.place_ship()
computers_grid.print_grid()
print(f"Computers ship: {computers_grid.ships}")
print(f"players ship: {players_grid.ships}")
size = players_grid.size


# Takes input from user, validates the data and puts in in the grid
def take_input():
    player_x = input(f"Please enter row number (0-{size - 1}): ")

    while not player_x.isdigit() or not (0 <= int(player_x) < size):
        print(f"{player_x} is not a valid input, please try again!")
        player_x = input(f"Please enter row number (0-{size - 1}): ")

    player_y = input(f"Please enter column number (0-{size - 1}): ")

    while not player_y.isdigit() or not (0 <= int(player_y) < size):
        print(f"{player_y} is not a valid input, please try again!")
        player_y = input(f"Please enter column number (0-{size - 1}): ")
    player_guess = (int(player_x), int(player_y))
    if player_guess in players_grid.guesses:
        print("You can't guess the same coordinates again...")
        take_input()
    else:
        players_grid.guesses.append(player_guess)
    if player_guess in computers_ship:
        computers_grid.grid[player_guess[0]][player_guess[1]] = "X"
        computers_grid.print_grid()
        points[0] += 1
        print("It's a hit!💥")
        print(f"Scores: {player_name}: {points[0]}, Computer: {points[1]}")
    elif computers_grid.grid[player_guess[0]][player_guess[1]] == "*":
        computers_grid.grid[player_guess[0]][player_guess[1]] = "M"
        players_grid.guesses.append(player_guess)
    if points[0] == 3:
        print("Congratulations You Won!🎉")
        reset_game()
    create_computer_guess()


# Creates random num for computer and puts the guess in the grid
def create_computer_guess():
    computer_x = random.randint(0, computers_grid.size - 1)
    computer_y = random.randint(0, computers_grid.size - 1)
    computer_guess = (int(computer_x), int(computer_y))
    if computer_guess not in computers_grid.guesses:
        computers_grid.guesses.append(computer_guess)
    else:
        create_computer_guess()
    computers_grid.guesses.append(computer_guess)
    if players_grid.grid[computer_guess[0]][computer_guess[1]] == "S":
        players_grid.grid[computer_guess[0]][computer_guess[1]] = "X"
        players_grid.print_grid()
        points[1] += 1
        print("The computer has a hit!💥")
        print(f"Scores: {player_name}: {points[0]}, Computer: {points[1]}")
    elif players_grid.grid[computer_guess[0]][computer_guess[1]] == "*":
        players_grid.grid[computer_guess[0]][computer_guess[1]] = "M"
        computers_grid.guesses.append(computer_guess)
    print(f"Computer guessed: {computer_guess}")
    if points[1] == 3:
        print("Ouups... the Computer Won!🎉")
        reset_game()

    players_grid.print_grid()
    computers_grid.print_grid()
    take_input()


# Resets the game
def reset_game():
    new_game = input("Would you like to start a new game? yes/no ")
    if new_game.lower() == "yes":
        global computers_ship
        points[0] = 0
        points[1] = 0
        players_grid.guesses = []
        players_grid.ships = []
        computers_grid.ships = []
        computers_ship = computers_grid.place_ship()
        computers_grid.guesses = []
        players_grid.grid = [["*"] * size for _ in range(size)]
        computers_grid.grid = [["*"] * size for _ in range(size)]
        players_grid.place_ship()
        players_grid.print_grid()
        computers_grid.print_grid()
        start_game()
        return
    elif new_game.lower() != "yes" and new_game.lower() != "no":
        print("Incorrect input...")
        return reset_game()
    else:
        print(30*"_")
        print(f"\n Thank you for playing {player_name}!")
        print(30*"_")
        exit()


def start_game():
    take_input()


start_game()
