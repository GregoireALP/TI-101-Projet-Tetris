import os
import grid
import blocs

def update_console(_grid):
    os.system("cls")
    content = grid.read_grid(_grid)
    grid.print_grid(content)

    bs = blocs.select_blocs(_grid)
    for b in bs:
        print(b)

    input()
    return 0


