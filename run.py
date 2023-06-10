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

