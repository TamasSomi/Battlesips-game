import random


class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [["*"] * size for _ in range(size)]
        self.ships = []

    def print_grid(self):
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()

    def place_ship(self):
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)

            if self.grid[x][y] == "*":
                self.grid[x][y] = "S"
                break


grid = Grid(3)
grid.place_ship()
grid.print_grid()

