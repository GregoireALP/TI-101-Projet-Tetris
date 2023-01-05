def read_grid(path):
    """
    Permet de lire un fichier texte grille
    Et de retourner son equivalent en tableau 2D

    @:parameter:
        @:param path (string): Le chemin d'acces a la grille

    @:returns:
        @:return grid int[][] un tableau 2D representant la grille
    """

    grid = []

    # On ouvre le fichier indique en tant que variable txt
    with open("./src/" + path) as txt:

        # On parcours chaque ligne
        for l in txt:

            line = []  # On initialise une ligne vide

            '''
            Pour chaque caractere sur la ligne
            On insere dans notre ligne vide
            Son caractere sous forme d'int
            '''
            for e in l:
                if e == "1" or e == "0" or e == "2":
                    line.append(int(e))

            # On insere la ligne dans notre tableau
            grid.append(line)

    return grid


def save_grid(path, grid):
    """
    Permit d'enregistrer dans un fichier texte choisis
    Un tableau 2D sous la forme d'une grille text

    @:parameter:
        @:param string path le nom du fichier texte
        @:param grid int[][] le tableau 2D a convertir

    @:returns:
        @:return void
    """

    # On cree une chaine vide representant le fichier texte
    gridTxt = ""

    # Pour chaque tableau dans la variable grid
    for i in range(len(grid)):

        # On cree une ligne vide
        line = ""

        '''
        Pour chaque caractere dans le sous tableau
        On insere dans notre lignne texte vide
        Son caractere sous forme de char
        '''
        for y in range(len(grid[i])):
            line = line + str(grid[i][y]) + " "

        # On ajoute un saut de ligne a la fin
        line = line + "\n"

        # On ajoute la ligne a la grille
        gridTxt = gridTxt + line

    # On cree et ouvre un nouveau fichier a l'endroit indique
    with open(path, "w") as f:

        # On ecrit notre grille dans le fichier
        f.write(str(gridTxt))


def print_grid(grid):
    """
    Permet d'afficher un tableau 2D sous forme d'une grille decore

    @:parameter:
        @:param int[][] la tableau 2D a afficher

    @:returns:
        @:return void
    """

    # On cree des alphabets pour les coordonnees
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetCap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Afficher les coordonnees des abscices
    print("    ", end="")
    for i in range(len(grid[0])):
        print(alphabet[i], end=" ")
    print("\n  ╔", len(grid[0]) * "= " + "╗")

    '''
    On affiche le contenu du tableau 2D
    En verifiant chaque caractere pour afficher un bloc ou une case vide
    '''
    for i in range(len(grid)):
        print(alphabetCap[i] + " ║ ", end="")
        for y in range(len(grid[i])):
            if grid[i][y] == 0:
                print(" ", end=" ")
            if grid[i][y] == 1:
                print(".", end=" ")
            if grid[i][y] == 2:
                print("■", end=" ")
        print("║")

    print("  ╚", len(grid[0]) * "= " + "╝")


def valid_position(grid, bloc, x, y):
    """
    Permet de verifier si le bloc est placable a la poisition donnee

    @:parameter:
        @:param grid (list): La matrice de la graille
        @:param bloc (list): la matrice du bloc
        @:param x (int): coordonne x
        @:param y (int): coordonne x

    @:returns
        @:return: validPosition (bool): Si la position est valide
    """

    # Variable d'etat de la possibilite de placer le bloc
    validPosition = True

    # On parcours de la derniere ligne de la matrice a la premiere
    # x et y reprensentent le coin inferieur gauche de la matrice du bloc
    for i in range(len(bloc) - 1, -1, -1):

        # Pour chaque indice d'element de la ligne
        for j in range(len(bloc[i])):

            """
            On regarde si sur la matrice du bloc, sa position relative sur la grille correspond a une case vide
            Sinon la position n'est pas valide
            """
            if bloc[i][j] == 2 and (grid[x + (i - len(bloc) + 1)][y + j] == 2 or grid[x + (i - len(bloc) + 1)][y + j] == 0):

                # La position est fausse
                validPosition = False

    return validPosition


def emplace_bloc(grid, bloc, x, y):
    """
    Permet de placcer le bloc a la poisition donnee

    @:parameter:
        @:param grid (list): La matrice de la graille
        @:param bloc (list): la matrice du bloc
        @:param x (int): coordonne x
        @:param y (int): coordonne x

    @:returns
        @:return: void
    """

    # On parcours de la derniere ligne de la matrice a la premiere
    # x et y reprensentent le coin inferieur gauche de la matrice du bloc
    for i in range(len(bloc) - 1, -1, -1):

        # Pour chaque indice d'element de la ligne
        for j in range(len(bloc[i])):

            # Si l'element de la matrice est une case pleine
            if bloc[i][j] == 2:

                # Alors on place sur la grille avec la position relative une case pleine aussi
                grid[x + (i - len(bloc) + 1)][y + j] = 2


def clear_row(grid, i):
    """
    Permet vider une ligne donnee

    @:parameter:
        @:param grid (list): La matrice de la graille
        @:param i (int): indice de la ligne

    @:returns
        @:return: void
    """

    # Pour chaque indicec de la ligne donnee
    for y in range(len(grid[i])):

        # On remplace a l'indice y par un 1 (Case vide)
        grid[i][y] = 1


def clear_col(grid, i):
    """
    Permet vider une colonne donnee

    @:parameter:
        @:param grid (list): La matrice de la grille
        @:param i (int): indice de la colonne

    @:returns
        @:return: void
    """

    # Pour chaque indice de ligne dans la matrice
    for y in range(len(grid)):

        # On remplace a chaque ligne au meme indice par un 1 (case vide)
        grid[y][i] = 1


def grid_go_down(grid, line):
    """
    Permet de, en cas de ligne vide, faire descendre les blocs

    @:parameter:
        @:param grid (list): La matrice de la grille
        @:param line (int): indice de la ligne vide

    @:returns
        @:return: void
    """


