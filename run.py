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
            x = random.randit(0, self.size - 1)
            y = random.randit(0, self.size - 1)

            if self.grid[x][y] == "*":
                self.add_ship(x, y)
                break


grid = Grid(4)
grid.print_grid()
