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
                if self.type == "player":
                    self.grid[x][y] = "S"
                break


players_grid = Grid(3, 1, "Tommy", type="player")
computers_grid = Grid(3, 1, "Computer", type="Computer")
players_grid.place_ship()
players_grid.print_grid()
computers_grid.place_ship()
computers_grid.print_grid()

def check_guess(attacker_grid, defender_grid, x, y):
    if (x, y) in defender_grid.ships:
        print("It's a hit!")
        defender_grid.grid[x][y] = "X"
    else:
        print("Miss!")
    
    defender_grid.guesses.append((x, y))
    defender_grid.print_grid()

    if attacker_grid.type == "Computer":
        print("The computer's turn:")

        computer_x = random.randint(0, attacker_grid.size - 1)
        computer_y = random.randint(0, attacker_grid.size - 1)
        check_guess(computers_grid, players_grid, computer_x, computer_y)
    else:
        print("Your turn:")

