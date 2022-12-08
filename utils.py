import os
import grid
import blocs

alphabet = "abcdefghijklmnopqrstuvwxy"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def update_console(_grid, gameState):
    os.system("cls")

    content = grid.read_grid(_grid)
    grid.print_grid(content)

    bs = blocs.select_blocs(_grid)
    for i in range(len(bs)):
        print(i, ") ")
        blocs.display_bloc(bs[i])

    choice = int(input("Quelle block voulez-vous choisir ?"))
    while 0 > choice or choice > 2:
        print("Ce block n'existe pas !")
        choice = int(input("Quelle block voulez-vous choisir ?"))

    x = input("Sur quelle ligne voulez-vous poser le block")
    xcor = caps.index(x)

    y = input("Sur quelle colonne voulez-vous poser le block")
    ycor = alphabet.index(y)

    res = grid.valid_position(content, bs[choice], xcor, ycor)

    print(res)

    input()
    return gameState
