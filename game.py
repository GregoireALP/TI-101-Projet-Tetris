import os
import blocs
import grid


def game_loop(_grid):
    """
=    Fonction principal qui execute en boucle la fonction d'instruction de jeu

        @:parameter:
            @:param _grid (str): Le nom du fichier de plateau

        @:returns :
            @:return void
    """

    isGameFinish = False  # Variable d'etat de la partie
    content = grid.read_grid(_grid)  # On recupere la matrice de la grille
    score = 0  # On creer la varible de score

    # Tant que la variable d'etat du jeu n'est pas vrai (jeu non fini) on execute la fonction
    while not isGameFinish:
        """
        La fonction update_console() renvoie un score, une nouvelle grille et un etat
        On reinsere ces elements dans la fonction en verifiant avant si la partie n'est pas finie
        """
        content, isGameFinish, score = update_console(content, isGameFinish, _grid, score)

    # On efface la console
    os.system("cls")

    # Affichage fin de partie
    print(" " * 10 + "╔══════════════════════════════════════════════════╗")
    print(" " * 10 + "║                                                  ║")
    print(" " * 10 + "║                   PARTIE TERMINE                 ║")
    print(" " * 10 + "║                                                  ║")
    print(" " * 10 + "╚══════════════════════════════════════════════════╝")
    print()
    print()
    print("╔═════════════" + "═" * len(str(score)) + "═╗")
    print("║ Score: ", score, "    ║")
    print("╚═════════" + "═" * len(str(score)) + "═════╝")


def regles():
    """
=    Affiche les regles du jeu

        @:parameter:

        @:returns :
            @:return void
    """

    # On affiche les regles du jeu issu de la consigne
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
    """
=    Fonction de demarage, affiche le menu du jeu

        @:parameter:

        @:returns :
            @:return void
    """

    # On efface la console
    os.system("cls")

    # On affiche le menu et les differents choix
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

    # On demande a l'utilisateur son choix
    result = int(input("Reponse: "))

    match result:

        # 2 = Afficher les regles
        case 2:

            # On efface le terminal
            os.system("cls")

            # On execute la fonction regle()
            regles()

            # On attend tant que l'utilisateur n'appuie pas sur une touche
            input()

            # On efface la console
            os.system("cls")

            # On re affiche le menu
            start()

        # 1 = Commencer le jeu
        case 1:

            # On affiche les grilles
            choisir_grid()

        case 3:

            # On retourne 0, le programme s'arrete
            return 0

        # Sinon on re affiche le menu
        case _:
            start()


def choisir_grid():
    """
=    Affiche les grilles disponibles et recupere le choix de l'utilisateur

        @:parameter:

        @:returns :
            @:return void
    """

    # On efface la console
    os.system("cls")

    # On affiche les differents choix
    print("╔═══════════════╗          ╔════════════════╗          ╔════════════════╗")
    print("║               ║          ║                ║          ║                ║")
    print("║       1       ║          ║        2       ║          ║        3       ║")
    print("║     Cercle    ║          ║     Losange    ║          ║     Triangle   ║")
    print("╚═══════════════╝          ╚════════════════╝          ╚════════════════╝")
    print()
    print()

    # On demande un choix a l'utilisateur
    result = int(input("Reponse: "))

    # On teste la reponse
    match result:

        # 1 = Cerlce
        case 1:
            game_loop("cercle.txt")

        # 2 = Losange
        case 2:
            game_loop("losange.txt")

        # 3 = Triangle
        case 3:
            game_loop("triangle.txt")

        # Sinon on refais choisir l'utilisateur
        case _:
            choisir_grid()


def update_console(content, gameState, grid_name, score, error=0):
    """
    Fonction principal du jeu qui execute chaque instruction

    @:parameter:
        @:param conten (list): La matrice du plateau de jeu
        @:param gameState: (bool): L'etat de la partie
        @:param grid_name (str): Le nom de la grille
        @:param score (int): Le score du joueur
        @:param error: (int): Le nombre d'echec du joueur

    @:returns:
        @:return content (list): La nouvelle grille modifie
        @:return gameState (bool): L'etat de la partie
        @:return score (int): Le mouveau score actualise

    """

    # On creer 2 alphabets pour convertir les coordonne en nombre et inversement
    alphabet = "abcdefghijklmnopqrstuvwxy"
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Verification du nombre d'erreur du joueur
    if error >= 3:
        gameState = True
        return content, gameState, score

    # On efface le terminal
    os.system("cls")

    # Affichage du score, affichage modulable en fonction du score
    print("╔═════════════" + "═" * len(str(score)) + "═╗")
    print("║ Score: ", score, "    ║")
    print("╚═════════" + "═" * len(str(score)) + "═════╝")

    # Affichage de la grille
    grid.print_grid(content)

    # Récupération de 3 blocs aléatoire
    bs = blocs.select_bloc(grid_name)

    # On les affiches
    for i in range(len(bs)):
        print(i, ") ")  # On indique l'indice
        blocs.display_bloc(bs[i])

    # Demande du choix de l'utilisateur
    choice = int(input("Quelle block voulez-vous choisir ?"))
    while 0 > choice or choice > 2:
        print("Ce block n'existe pas !")
        choice = int(input("Quelle block voulez-vous choisir ?"))

    # Demande de la coordonnee x du bloc
    x = input("Sur quelle ligne voulez-vous poser le block")

    # Saisis securisé
    isXCorValid = False
    while not isXCorValid:
        if x in caps[:len(content)]:
            isXCorValid = True
        else:
            print("Ligne non disponible !")
            x = input("Sur quelle ligne voulez-vous poser le block")

    # On recupere la coordonne sous forme de nombre
    xcor = caps.index(x)

    # Demande de la coordonnee y du bloc
    y = input("Sur quelle colonne voulez-vous poser le block")

    # Saisis securisé
    isYCorValid = False
    while not isYCorValid:
        if y in alphabet[:len(content[0])]:
            isYCorValid = True
        else:
            print("Colonne non disponible !")
            y = input("Sur quelle colonne voulez-vous poser le block")

    # On recupere la coordonne sous forme de nombre
    ycor = alphabet.index(y)

    # On teste si la position demandé est valide
    isPositionValid = grid.valid_position(content, bs[choice], xcor, ycor)

    # Si la position est valide
    if isPositionValid:
        # On place le bloc sur la grille
        grid.emplace_bloc(content, bs[choice], xcor, ycor)

        # Pour chaque ligne dans la grille
        for line in range(len(content)):

            # On teste si elle est pleine
            isRowFull = row_state(content, line)

            # Si elle est pleine
            if isRowFull:

                # Pour chaque element sur cette ligne
                for e in content[line]:

                    # Si cette case est pleine (Toujours vraie car ligne pleine)
                    if e == 2:
                        # On ajoute 1 au score
                        score += 1

                # On efface la ligne
                grid.clear_row(content, line)

                # On fait descendre la grille
                # grid.grid_go_down(content, line)

        # Pour chaque indice d'element dans une ligne (Pour chaque colonne)
        for col in range(len(content[0])):

            # On teste si la colonne a cette indice est pleine
            isColFull = col_state(content, col)

            # Si elle est plein
            if isColFull:

                # Pour chaque ligne
                for e in content:

                    # Si l'element a cette indice de cette ligne est une case pleine (Toujours vraie car colonne pleine)
                    if e[col] == 2:
                        # On ajoute 1 au score
                        score += 1

                # On efface la colonne
                grid.clear_col(content, col)
    else:

        # Indiquation pour le joueur
        print("La position indiqué n'est pas valide !")
        input()

        # Si la position n'est pas valie on recommence la fonction en ajoutant l'echec 1
        return update_console(content, gameState, grid_name, score, error + 1)

    return content, gameState, score


def row_state(_grid, i):
    """
    Verifie si une ligne de la grille est pleine

        @:parameter:
            @:param _grid (list): Matrice du bloc choisis
            @:param i (int): inidice de la ligne a verifier

        @:returns :
            @:return isFull (bool): Vrai si ligne pleine
    """
    isFull = True

    # POur chaque element de la ligne i
    for e in _grid[i]:

        # Si la case est vide
        if e == 1:
            # La ligne n'est pas vide
            isFull = False

    return isFull


def col_state(_grid, i):
    """
    Verifie si une colonne de la grille est pleine

        @:parameter:
            @:param _grid (list): Matrice du bloc choisis
            @:param i (int): inidice de la colonne a verifier

        @:returns :
            @:return isFull (bool): Vrai si colonne pleine
    """

    isFull = True

    # Pour chasque ligne de la grille
    for y in range(len(_grid)):

        # Si la case est vide
        if _grid[y][i] == 1:
            # La colonne n'est pas vide
            isFull = False

    return isFull
