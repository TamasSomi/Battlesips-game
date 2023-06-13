
    print(f"Computers ship: {computers_grid.ships}")
    print(f"players ship: {players_grid.ships}")
    size = players_grid.size
    return size


size = create_boards


# Takes input from user, validates the data and puts in in the grid
def take_input():
    player_x = input(f"Please enter row number (0-{size - 1}): ")

    while not player_x.isdigit() or not (0 <= int(player_x) < size):