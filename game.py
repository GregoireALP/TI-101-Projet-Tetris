import os

import blocs
import grid
import utils


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
    print("1- Afficher les regles du jeu")
    print("2- Commencer le jeu")
    print("3- Quiiter le jeu")

    print()
    print()
    result = int(input("Reponse: "))

    if result == 1:
        os.system("cls")
        regles()
        input()
        os.system("cls")
        start()
    elif result == 2:
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


def game_loop(_grid):
    isGameFinish = False

    while not isGameFinish:
        utils.update_console(_grid)