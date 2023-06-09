import random

# index = 0 player, index 1 = computer
points = [0, 0]


class Grid:
    """
    A class to create the boards and place the ships.
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
        """
        Prints grids.
        """
        print(f"{self.name}'s board:")
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()
        print()

    def place_ship(self):
        """
        Places ships on the boards.
        """
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


def starter_messages():
    """
    Prints welcome messages
    """
    print(80*"_")
    print("\n Welcome to Battlesips Game!")
    print()
    print("Everyone has 3-3 ships.")
    print("The goal is to guess all the computers ships coordinates first.")
    print("On the board * means undiscovered field.")
    print("S means there is a ship and X is a ship that's been hit.")
    print(80*"_")
    print()
    player_name = input("What is your name?: \n")
    while not len(player_name) > 2:
        print("Please provide a name (min 3 characters): ")
        player_name = input("What is your name?: \n")
    return player_name


def take_input():
    """
    Takes input from the user, validates the coordinates. Puts them
    in the grid checks for hit and reacts accordingly.
    Calls create_computer_guess or reset_game function.
    """
    player_x = input(f"Enter row number (0-{players_grid.size - 1}): \n")

    while not player_x.isdigit() or not 0 <= int(player_x) < players_grid.size:
        print(f"{player_x} is not a valid input, please try again!")
        player_x = input(f"Enter row number (0-{players_grid.size - 1}): \n")

    player_y = input(f"Enter column number (0-{players_grid.size - 1}): \n")

    while not player_y.isdigit() or not 0 <= int(player_y) < players_grid.size:
        print(f"{player_y} is not a valid input, please try again!")
        player_y = input(f"Enter column number(0-{players_grid.size - 1}): \n")
    player_guess = (int(player_x), int(player_y))
    if player_guess in players_grid.guesses:
        print("You can't guess the same coordinates again...")
        take_input()
    else:
        players_grid.guesses.append(player_guess)
    if player_guess in computers_grid.ships:
        computers_grid.grid[player_guess[0]][player_guess[1]] = "X"
        points[0] += 1
        print("It's a hit!💥")
    elif computers_grid.grid[player_guess[0]][player_guess[1]] == "*":
        computers_grid.grid[player_guess[0]][player_guess[1]] = "M"
        players_grid.guesses.append(player_guess)
        print("You missed! ")
    print(f"Scores: {player_name}: {points[0]}, Computer: {points[1]}")
    if points[0] == 3:
        print("Congratulations You Won!🎉")
        reset_game()
    create_computer_guess()


def create_computer_guess():
    """
    Creates random num for computer and puts
    the guess in the grid. Checks for hit
    and reacts accordingly. Prints the grids.
    Calls reset game or take_input function.
    """
    computer_x = random.randint(0, computers_grid.size - 1)
    computer_y = random.randint(0, computers_grid.size - 1)
    computer_guess = (int(computer_x), int(computer_y))
    if computer_guess not in computers_grid.guesses:
        computers_grid.guesses.append(computer_guess)
    else:
        create_computer_guess()
    computers_grid.guesses.append(computer_guess)
    print(f"Computer guessed: {computer_guess}")
    if players_grid.grid[computer_guess[0]][computer_guess[1]] == "S":
        players_grid.grid[computer_guess[0]][computer_guess[1]] = "X"
        points[1] += 1
        print("The computer has a hit!💥")

    elif players_grid.grid[computer_guess[0]][computer_guess[1]] == "*":
        players_grid.grid[computer_guess[0]][computer_guess[1]] = "M"
        computers_grid.guesses.append(computer_guess)
        print("The computer missed!")
    if points[1] == 3:
        print(f"Scores: {player_name}: {points[0]}, Computer: {points[1]}")
        print("Ouups... the Computer Won!🎉")
        reset_game()
    players_grid.print_grid()
    computers_grid.print_grid()
    print(f"Scores: {player_name}: {points[0]}, Computer: {points[1]}")
    take_input()


def reset_game():
    """
    Resets everything for the starter values.
    """
    new_game = input("Would you like to start a new game? yes/no \n")
    if new_game.lower() == "yes":
        points[0] = 0
        points[1] = 0
        players_grid.guesses = []
        players_grid.ships = []
        computers_grid.ships = []
        computers_grid.place_ship()
        computers_grid.guesses = []
        players_grid.grid = [
            ["*"] * players_grid.size
            for _ in range(players_grid.size)
        ]
        computers_grid.grid = [
            ["*"] * players_grid.size
            for _ in range(players_grid.size)
        ]
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


if __name__ == '__main__':
    player_name = starter_messages()
    players_grid = Grid(4, 3, player_name, type="Player")
    computers_grid = Grid(4, 3, "Computer", type="Computer")
    players_grid.place_ship()
    players_grid.print_grid()
    computers_grid.place_ship()
    computers_grid.print_grid()
    start_game()
