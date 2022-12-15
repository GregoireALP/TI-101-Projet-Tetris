import random

blocs_liste_commun = [
    [
        [2, 1],
        [2, 2]
    ],
    [
        [1, 2],
        [2, 2]
    ],
    [
        [2, 1, 1],
        [2, 2, 2]
    ],
    [
        [2, 2],
        [1, 2],
        [1, 2]
    ],
    [
        [2, 1],
        [2, 2],
        [2, 1]
    ],
    [
        [1, 2, 1],
        [2, 2, 2]
    ],
    [
        [2, 2, 1],
        [1, 2, 2]
    ],
    [
        [2, 1],
        [2, 2],
        [1, 2]
    ],
    [
        [2],
        [2],
        [2],
        [2]
    ],
    [
        [2, 2],
        [2, 2]
    ],
    [
        [2, 2],
        [1, 2]
    ],
    [
        [2, 2],
        [2, 1]
    ],
    [
        [1, 1, 2],
        [2, 2, 2]
    ],
    [
        [2, 1],
        [2, 1],
        [2, 2]
    ],

    [
        [1, 2],
        [2, 2],
        [1, 2]
    ],
    [
        [2, 2, 2],
        [1, 2, 1]
    ],
    [
        [1, 2, 2],
        [2, 2, 1]
    ],
    [
        [1, 2],
        [2, 2],
        [2, 1]
    ],
    [
        [2, 2, 2, 2]
    ],
    [
        [2]
    ]
]

blocs_liste_cercle = [
    [
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2]
    ],
    [
        [1, 2, 2, 1],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [1, 2, 2, 1]
    ],
    [
        [2, 1, 1, 2],
        [2, 1, 1, 2],
        [2, 1, 1, 2],
        [2, 2, 2, 2]
    ],
    [
        [2, 2, 2, 2],
        [1, 1, 1, 2],
        [1, 1, 1, 2],
        [1, 1, 1, 2]
    ],
    [
        [2, 2, 2, 2],
        [2, 2, 2, 1]
    ],
    [
        [2, 2, 2],
        [1, 1, 2],
        [1, 1, 2],
        [2, 2, 2]
    ],
    [
        [2, 2],
        [2, 2],
        [2, 2],
        [2, 2]
    ],
    [
        [2, 2, 2, 2],
        [2, 2, 2, 2]
    ],
    [
        [2],
        [2],
        [2],
        [2],
        [2]
    ],
    [
        [2, 2, 2, 2, 2],
        [2, 1, 1, 1, 2]
    ],
    [
        [2, 2, 2, 2, 2]
    ],
    [
        [2, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 1, 1, 2],
        [2, 2, 2, 2]
    ]
]

blocs_liste_losange = [
    [
        [1, 1, 2, 2],
        [1, 2, 2, 1],
        [2, 2, 1, 1],
        [2, 1, 1, 1]
    ],
    [
        [2, 2, 1, 1],
        [1, 2, 2, 1],
        [1, 1, 2, 2],
        [1, 1, 1, 2]
    ],
    [
        [2, 2, 2, 2],
        [1, 2, 2, 1],
        [1, 2, 2, 1],
        [1, 2, 2, 1]
    ],
    [
        [2, 1, 1, 2],
        [1, 2, 2, 1],
        [1, 2, 2, 1],
        [2, 1, 1, 2]
    ],
    [
        [2, 2, 2, 2, 2],
        [1, 2, 2, 2, 1],
        [1, 1, 2, 1, 1]
    ],
    [
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2],
        [2, 2, 2, 2]
    ],
    [
        [2, 1, 1, 1],
        [2, 2, 1, 1],
        [1, 2, 2, 1],
        [1, 1, 2, 2]
    ],
    [
        [1, 1, 1, 2],
        [1, 1, 2, 2],
        [1, 2, 2, 1],
        [2, 2, 1, 1]
    ],
    [
        [2],
        [2],
        [2],
        [2],
        [2]
    ],
    [
        [1, 1, 1, 2],
        [2, 2, 2, 2],
        [1, 1, 1, 2]
    ],
    [
        [2, 2, 2, 2],
        [1, 1, 1, 2]
    ],
    [
        [2, 2],
        [1, 2],
        [1, 2],
        [1, 2]
    ],
    [
        [2, 1],
        [2, 1],
        [2, 1],
        [2, 2]
    ],
    [
        [2, 2, 2, 2, 2]
    ]

]

blocs_liste_triangle = [
    [
        [2, 1, 1],
        [2, 2, 2],
        [1, 1, 2]
    ],
    [
        [2, 2, 1],
        [1, 2, 1],
        [1, 2, 2]
    ],
    [
        [1, 1, 2],
        [2, 2, 2],
        [2, 1, 1]
    ],
    [
        [1, 2, 2],
        [1, 2, 1],
        [2, 2, 1]
    ],
    [
        [1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]
    ],
    [
        [2, 1, 1],
        [1, 2, 1],
        [1, 1, 2]
    ],
    [
        [2],
        [2],
        [2]
    ],
    [
        [2, 2, 2]
    ],
    [
        [2],
        [2]
    ],
    [
        [1, 2, 1],
        [2, 2, 2],
        [1, 2, 1]
    ],
    [
        [2, 2]
    ]
]

# On creer une grande liste regroupant tout les blocs disponibles dans le jeu
blocs_liste = blocs_liste_commun + blocs_liste_cercle + blocs_liste_losange + blocs_liste_triangle

# On initialise nos liste de blocs pour chaque grille en ajoutant leur indices
cercle_liste = blocs_liste_commun + blocs_liste_cercle
losange_liste = blocs_liste_commun + blocs_liste_losange
triangle_liste = blocs_liste_commun + blocs_liste_triangle


def display_bloc(bloc):
    for i in range(len(bloc)):
        for y in range(len(bloc[i])):
            if bloc[i][y] == 2:
                print("■", end=" ")
            else:
                print(" ", end=" ")
        print()
    print()


def print_bloc(grid):
    if grid == "cerlce.txt":
        for i in range(len(cercle_liste)):
            display_bloc(cercle_liste[i])

    if grid == "losange.txt":
        for i in range(len(losange_liste)):
            display_bloc(losange_liste[i])

    if grid == "triangle.txt":
        for i in range(len(triangle_liste)):
            display_bloc(triangle_liste[i])


def get_blocs(blocList):
    bs = []
    for _ in range(3):
        e = random.randint(0, len(blocList) - 1)
        bs.append(blocList[e])

    return bs


def select_blocs(grid):
    if grid == "cercle.txt":
        return get_blocs(cercle_liste)

    if grid == "losange.txt":
        return get_blocs(losange_liste)

    if grid == "triangle.txt":
        return get_blocs(triangle_liste)
