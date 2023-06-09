class Grid:
    def __init__(self):
        self.grid = [["*"] * 4 for _ in range(4)]

    def ship(self, row, col):
        return self.grid[row][col]

    def guess(self, row, col):
        return self.grid[row][col]

    def print_grid(self):
        for row in self.grid:
            for col in row:
                print(col, end=" ")
            print()



grid = Grid()
grid.print_grid()
