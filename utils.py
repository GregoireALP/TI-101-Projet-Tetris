import os
import grid


def update_console(_grid):
    os.system("cls")

    content = grid.read_grid(_grid)
    grid.print_grid(content)

