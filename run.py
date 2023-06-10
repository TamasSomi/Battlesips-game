import random



class Grid:
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.grid = [["*"] * size for _ in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_grid(self):
        print(f"{self.name}'s board: \n")
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()
        print()

    def place_ship(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            if self.grid[x][y] == "*":
                self.ships.append((x, y))
                if self.type == "Player":
                    self.grid[x][y] = "S"
                break


players_grid = Grid(3, 1, "Tommy", type="Player")
computers_grid = Grid(3, 1, "Computer", type="Computer")
players_grid.place_ship()
players_grid.print_grid()
computers_grid.place_ship()
computers_grid.print_grid()
size = players_grid.size

def check_guess(attacker_grid, defender_grid, x, y):
    if (x, y) in defender_grid.ships:
        print("It's a hit!")
        defender_grid.grid[x][y] = "X"

    else:
        defender_grid.grid[x][y] = "M"
        print("Miss!")
    
    defender_grid.guesses.append((x, y))
    defender_grid.print_grid()
    attacker_grid.print_grid()

    if attacker_grid.type == "Player":
        print("The computer's turn:")

        computer_x = random.randint(0, attacker_grid.size - 1)
        computer_y = random.randint(0, attacker_grid.size - 1)
        check_guess(computers_grid, players_grid, computer_x, computer_y)
    else:
        print("Your turn:")
        check_input()


def check_input():
    player_x = input(f"Please enter row number (0-{size - 1}: ")
    while not player_x.isdigit() or not (0 <= int(player_x) < size):
        print(f"{player_x} is not a valid input, please try again!")
        player_x = input(f"Please enter row number (0-{size - 1}): ")

    player_y = input(f"Please enter column number (0-{size - 1}): ")

    while not player_y.isdigit() or not (0 <= int(player_y) < size):
        print(f"{player_y} is not a valid input, please try again!")
        player_y = input(f"Please enter column number (0-{size - 1}): ")
    player_guess = (int(player_x), int(player_y))
    if player_guess in  players_grid.guesses:
        print("You can't guess the same coordinates again...")
        check_input()
    else:
        players_grid.guesses.append(player_guess)
        check_guess(players_grid, computers_grid, int(player_x), int(player_y))

def check_winner(grid):
    for ship in grid.ships:
        x, y = ship
        if grid.grid[x][y] != "X":
            return False
        
    print(f"{grid.name} is the Winner!")
    play_again = input("Would you like to play again? (yes / no): ").lower()
    if play_again = "yes":
        reset_game()
    else:
        print("Thanks for playing!")
        exit()

check_input()



