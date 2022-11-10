import blocs

cercle_liste = [i for i in range(0, len(blocs.blocs_liste_commun) + len(blocs.blocs_liste_cercle))]
losange_liste = [i for i in range(0, 20)] + [y for y in range(len(cercle_liste), len(cercle_liste) + 14)]
triangle_liste = [i for i in range(0, 20)] + [y for y in range(20 + len(blocs.blocs_liste_cercle) + len(blocs.blocs_liste_losange) ,len(blocs.blocs_liste_commun) + len(blocs.blocs_liste_cercle) + len(blocs.blocs_liste_losange) + len(blocs.blocs_liste_triangle))]

def read_grid(path):
    grid = []
    with open(path) as txt:
        for l in txt:
            line = []
            for e in l:
                if e == "1" or e == "0":
                    line.append(int(e))
            grid.append(line)

    return grid

def save_grid(path, grid):
    gridTxt = ""
    for i in range(len(grid)):
        line = ""
        for y in range(len(grid[i])):
            line = line + str(grid[i][y]) + " "
        line = line + "\n"
        gridTxt = gridTxt + line

    with open(path, "w") as f:
        f.write(str(gridTxt))

def print_grid(grid):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetCap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Afficher les coordonnees
    print("    ", end="")
    for i in range(len(grid[0])):
        print(alphabet[i], end=" ")
    print()
    print("  ╔ ", end="")
    for i in range(len(grid[0])):
        print("=", end=" ")
    print("╗", end="")
    print()

    # afficher le contenu
    for i in range(len(grid)):
        print(alphabetCap[i] + " ║ ", end="")
        for y in range(len(grid[i])):
            if grid[i][y] == 0:
                print(" ", end=" ")
            if grid[i][y] == 1:
                print(".", end=" ")
            if grid[i][y] == 2:
                print("■", end=" ")
        print("║", end="")
        print()

    print("  ", end="")
    for i in range(len(grid[0])):
        print("=", end=" ")
    print()

print_grid(read_grid("losange.txt"))

