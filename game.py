import os

import blocs
import grid

alphabet = "abcdefghijklmnopqrstuvwxy"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def game_loop(_grid):
    isGameFinish = False
    content = grid.read_grid(_grid)
    score = 0

    while not isGameFinish:
        content, isGameFinish, score = update_console(content, isGameFinish, _grid, score)


def regles():
    print(" " * 10 + "╔═════════════════════════════════════════════════════════╗")
    print(" " * 10 + "║                                                         ║")
    print(" " * 10 + "║                   Les Regles du Tetris                  ║")
    print(" " * 10 + "║                                                         ║")
    print(" " * 10 + "╚═════════════════════════════════════════════════════════╝")
    print()
    print()
    print(
        "● Le Tetris est un jeu qui se présente sous forme d’une matrice où des blocs de différentes formes doivent "
        "être posés de sorte que le plateau soit gardé le plus longtemps possible non plein.")
    print(
        "● L’idée est de placer chaque bloc à l’emplacement qui permet d’éliminer un maximum de lignes et/ou de "
        "colonnes.")
    print("● Ces dernières sont supprimées automatiquement lorsqu’elles sont pleines")
    print()
    print(
        "● Pour insérer un bloc sur le plateau, l’utilisateur dispose de trois tentatives pour saisir des coordonnées "
        "valides.")
    print(
        "● Si à l’issue de 3 tentatives successives, les positions choisies sont à chaque fois invalides, "
        "alors le jeu s’arrête.")
    print("● A la fin de la partie, un message doit s’afficher à l’écran rappelant le score obtenu.")


def start():
    os.system("cls")
    print(" " * 10 + "╔═════════════════════════════════════════════════════════╗")
    print(" " * 10 + "║                                                         ║")
    print(" " * 10 + "║                   Bienvenue sur TETRIS                  ║")
    print(" " * 10 + "║                                                         ║")
    print(" " * 10 + "╚═════════════════════════════════════════════════════════╝")

    print()
    print("1- Commencer le jeu")
    print("2- Afficher les regles du jeu")
    print("3- Quitter le jeu")

    print()
    print()
    result = int(input("Reponse: "))

    if result == 2:
        os.system("cls")
        regles()
        input()
        os.system("cls")
        start()
    elif result == 1:
        choisir_grid()
    elif result == 3:
        return 0
    else:
        start()


def choisir_grid():
    os.system("cls")
    print("╔═══════════════╗          ╔════════════════╗          ╔════════════════╗")
    print("║               ║          ║                ║          ║                ║")
    print("║       1       ║          ║        2       ║          ║        3       ║")
    print("║     Cercle    ║          ║     Losange    ║          ║     Triangle   ║")
    print("╚═══════════════╝          ╚════════════════╝          ╚════════════════╝")
    print()
    print()
    result = int(input("Reponse: "))

    if result == 1:
        game_loop("cercle.txt")
    elif result == 2:
        game_loop("losange.txt")
    elif result == 3:
        game_loop("triangle.txt")
    else:
        choisir_grid()


def update_console(content, gameState, grid_name, score):
    os.system("cls")

    print("Score:", score)

    grid.print_grid(content)

    bs = blocs.select_blocs(grid_name)
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
    if res:
        grid.emplace_bloc(content, bs[choice], xcor, ycor)

    for line in range(len(content)):
        res = row_state(content, line)
        if res:
            for e in content[line]:
                if e == 2:
                    score += 1

            grid.clear_row(content, line)

    for col in range(len(content[0])):
        res = col_state(content, col)
        if res:
            for e in content:
                if e[col] == 2:
                    score += 1

            grid.clear_col(content, col)

    return content, gameState, score


def row_state(_grid, i):
    isFull = True
    for e in _grid[i]:
        if e == 1 or e == 0:
            isFull = False
    return isFull


def col_state(_grid, i):
    isFull = True
    for y in range(len(_grid)):
        if _grid[y][i] == 1 or _grid[y][i] == 0:
            isFull = False
    return isFull
