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
cercle_liste = [i for i in range(0, len(blocs_liste_commun) + len(blocs_liste_cercle))]
losange_liste = [i for i in range(0, 20)] + [y for y in range(len(cercle_liste), len(cercle_liste) + 14)]
triangle_liste = [i for i in range(0, 20)] + [y for y in
                                              range(20 + len(blocs_liste_cercle) + len(blocs_liste_losange),
                                                    len(blocs_liste_commun) + len(blocs_liste_cercle) + len(
                                                        blocs_liste_losange) + len(blocs_liste_triangle))]


def display_bloc(bloc):
    for i in range(len(bloc)):
        for y in range(len(bloc[i])):
            if bloc[i][y] == 2:
                print("■", end="")
            else:
                print(" ", end="")
        print()


def print_bloc(grid):
    if grid == "cerlce.txt":
        for i in range(len(cercle_liste)):
            display_bloc(blocs_liste[cercle_liste[i]])

    if grid == "losange.txt":
        for i in range(len(losange_liste)):
            display_bloc(blocs_liste[losange_liste[i]])

    if grid == "triangle.txt":
        for i in range(len(triangle_liste)):
            display_bloc(blocs_liste[triangle_liste[i]])


def select_blocs(grid):
    def get_blocs(blocList):
        liste = []
        for _ in range(3):
            e = random.randint(1, len(grid) + 1)
            liste.append(blocs_liste[blocList[e]])
        return liste

    if grid == "cerlce.txt":
        return get_blocs(cercle_liste)

    elif grid == "losange.txt":
        return get_blocs(losange_liste)

    elif grid == "triangle.txt":
        return get_blocs(triangle_liste)

