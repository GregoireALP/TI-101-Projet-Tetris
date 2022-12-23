import random

'''
Ici on creer la liste constitue de tout les blocs
qui sont commun a chaque plateaux
'''
blocs_liste_commun = [
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 2, 1, 1, 1],
     [2, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 2, 2, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [1, 2, 1, 1, 1],
     [1, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [2, 1, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 2, 1, 1, 1],
     [2, 2, 2, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [1, 2, 2, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [1, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 1, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [2, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [1, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [2, 1, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 2, 1, 1],
     [2, 2, 2, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 1, 1, 1, 1],
     [2, 2, 1, 1, 1]
     ],

    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 2, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [1, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 2, 1, 1],
     [1, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 2, 2, 1, 1],
     [2, 2, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 2, 1, 1, 1],
     [2, 2, 1, 1, 1],
     [2, 1, 1, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 2, 2, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 1, 1, 1, 1]
     ]
]

'''
Ici on creer la liste constitue de tout les blocs du plateau cercle
'''

blocs_liste_cercle = [
    [[1, 1, 1, 1, 1],
     [2, 2, 2, 2, 1],
     [2, 2, 2, 2, 1],
     [2, 2, 2, 2, 1],
     [2, 2, 2, 2, 1]
     ],
    [[1, 1, 1, 1, 1],
     [1, 2, 2, 1, 1],
     [2, 2, 2, 2, 1],
     [2, 2, 2, 2, 1],
     [1, 2, 2, 1, 1]
     ],
    [[1, 1, 1, 1, 1],
     [2, 1, 1, 2, 1],
     [2, 1, 1, 2, 1],
     [2, 1, 1, 2, 1],
     [2, 2, 2, 2, 1]
     ],
    [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1],
        [1, 1, 1, 2, 1],
        [1, 1, 1, 2, 1],
        [1, 1, 1, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1],
        [2, 2, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 2, 1, 1],
        [2, 2, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1],
        [2, 2, 1, 1, 1],
        [2, 2, 1, 1, 1],
        [2, 2, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1],
        [2, 2, 2, 2, 1]
    ],
    [
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1]
    ],
    [[1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [1, 1, 1, 1, 1],
     [2, 2, 2, 2, 2],
     [2, 1, 1, 1, 2]
     ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 2, 1],
        [2, 2, 2, 2, 1]
    ]
]

'''
Ici on creer la liste constitue de tout les blocs du plateau losange
'''

blocs_liste_losange = [
    [
        [1, 1, 1, 1, 1],
        [1, 1, 2, 2, 1],
        [1, 2, 2, 1, 1],
        [2, 2, 1, 1, 1],
        [2, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1],
        [1, 2, 2, 1, 1],
        [1, 1, 2, 2, 1],
        [1, 1, 1, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1],
        [1, 2, 2, 1, 1],
        [1, 2, 2, 1, 1],
        [1, 2, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 2, 1],
        [1, 2, 2, 1, 1],
        [1, 2, 2, 1, 1],
        [2, 1, 1, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1],
        [2, 2, 2, 2, 1],
        [2, 2, 2, 2, 1],
        [2, 2, 2, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 2, 1, 1, 1],
        [1, 2, 2, 1, 1],
        [1, 1, 2, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1],
        [1, 1, 2, 2, 1],
        [1, 2, 2, 1, 1],
        [2, 2, 1, 1, 1]
    ],
    [
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2, 1],
        [2, 2, 2, 2, 1],
        [1, 1, 1, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1],
        [1, 1, 1, 2, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 2, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 2, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2]
    ]

]

'''
Ici on creer la liste constitue de tout les blocs du plateau triangle
'''

blocs_liste_triangle = [
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 2, 2, 1, 1],
        [1, 1, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 2, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [2, 2, 2, 1, 1],
        [2, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 2, 2, 1, 1],
        [1, 2, 1, 1, 1],
        [2, 2, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 2, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [1, 1, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1],
        [2, 1, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 2, 1, 1, 1],
        [2, 2, 2, 1, 1],
        [1, 2, 1, 1, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [2, 2, 1, 1, 1]
    ]
]

# On creer une grande liste regroupant tout les blocs disponibles dans le jeu
blocs_liste = blocs_liste_commun + blocs_liste_cercle + blocs_liste_losange + blocs_liste_triangle

# On initialise nos liste de blocs pour chaque grille en ajoutant leur indices
cercle_liste = blocs_liste_commun + blocs_liste_cercle
losange_liste = blocs_liste_commun + blocs_liste_losange
triangle_liste = blocs_liste_commun + blocs_liste_triangle


def display_bloc(bloc):
    """
    Permet d'afficher sur la console un bloc choisis

        Parameters:
            bloc (list (list (int))): Matrice du bloc choisis

        Returns:
            void
    """
    for i in range(len(bloc)):

        for y in range(len(bloc[i])):

            # Un 2 represente un bloc alors q'un 1 est une case vide
            if bloc[i][y] == 2:
                print("■", end=" ")

            else:
                print(" ", end=" ")

        # On marque un saut de ligne a chaque fin de tableau
        print()

    # On saute une ligne pour indiquer un bloc suivant
    print()


def print_bloc(grid):
    """
    Permet d'afficher l'ensemble des blocs disponible
    pour un plateau choisis

        Parameters:
            grid (str): Nom du fichier plateau

        Returns:
            void
    """
    match grid:

        # Pour fichier disponible
        case "cercle.txt":

            # On parcours tous les blocs de la liste
            for i in range(len(cercle_liste)):
                # On affiche chaque blocs
                display_bloc(cercle_liste[i])

        case "losange.txt":
            for i in range(len(losange_liste)):
                display_bloc(losange_liste[i])

        case "triangle.txt":
            for i in range(len(triangle_liste)):
                display_bloc(triangle_liste[i])


def select_bloc(gridName):
    """
    Permet de recuperer 3 blocs selon le plateau choisis
        Parameters:
            gridName (list (list)): Nom du fichier du plateau

        Returns:
            bs: list (list): Les 3 blocs choisis
    """

    usedGrid = None

    match gridName:

        # On test le nom du  fichier
        case "cercle.txt":

            # On associe sa liste de blocs
            usedGrid = cercle_liste

        case "losange.txt":
            usedGrid = losange_liste
        case "triangle.txt":
            usedGrid = losange_liste

    # On creer une list de bloc vide
    bs = []

    # On execute 3 fois pour recpurer 3 blocs
    for _ in range(3):
        # Avec le module "random" on choisis un nombre aleatoire entre 0
        # et la taille de la liste correspondant a l'indice du bloc
        e = random.randint(0, len(usedGrid) - 1)

        bs.append(usedGrid[e])

    return bs
