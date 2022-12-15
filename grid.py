"""
Permet de lire un fichier texte grille
Et de retourner son equivalent en tableau 2D
@:param string path: Le chemin d'acces a la grille
@:return int[][] un tableau 2D representant la grille
"""


def read_grid(path):
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


'''
Permit d'enregistrer dans un fichier texte choisis
Un tableau 2D sous la forme d'une grille text
@:param string path le nom du fichier texte
@:param grid int[][] le tableau 2D a convertir
@:return void
'''


def save_grid(path, grid):
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


'''
Permet d'afficher un tableau 2D sous forme d'une grille decore
@:param int[][] la tableau 2D a afficher
@:return void
'''


def print_grid(grid):
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
    if grid[x][y] != 1:
        return False
    elif grid[x][y] == 1:
        isValid = True
        for i in range(len(bloc) - 1, -1, -1):
            for j in range(len(bloc[i])):
                if grid[x - i][y + j] != 1:
                    if bloc[i][j] == 2:
                        isValid = False
        return isValid


def emplace_bloc(grid, bloc, x, y):
    for i in range(len(bloc) - 1, -1, -1):
        for j in range(len(bloc[i])):
            if bloc[i][j] == 2:
                grid[x + (i - len(bloc) + 1)][y + j] = 2