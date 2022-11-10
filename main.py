import blocs

cercle_liste = [i for i in range(0, len(blocs.blocs_liste_commun) + len(blocs.blocs_liste_cercle))]
losange_liste = [i for i in range(0, 20)] +  [y for y in range(len(cercle_liste), len(cercle_liste) + 14)]
triangle_liste = [i for i in range(0, 20)] + [y for y in range(20 + len(blocs.blocs_liste_cercle) + len(blocs.blocs_liste_losange) ,len(blocs.blocs_liste_commun) + len(blocs.blocs_liste_cercle) + len(blocs.blocs_liste_losange) + len(blocs.blocs_liste_triangle))]

def afficher(bloc):
    for i in range(len(bloc)):
        for y in range(len(bloc[i])):
            if bloc[i][y] == 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

for i in range(len(triangle_liste)):
    afficher(blocs.blocs_liste[triangle_liste[i]])
    print()