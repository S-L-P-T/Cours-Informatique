# Créé par ridf, le 18/03/2021 en Python 3.7
liste1 = [1, 2, 3, 4, 5, 6, 4, -56, 45, 78, 90, 7, 65, 0, 13, 908]
liste2 = [11, 12, 13, 74, 15, 46, 17, 18, 19, 567, 89, 46, 78, -45]

def fusion(tab1, tab2) -> list:
    """
    Fusion de deux listes en une seule par récursivité
    """
    if tab1 == []: #cas de base
        return tab2
    if tab2 == []:
        return tab1
    if tab1[0] < tab2[0]:
        return [tab1[0]] + fusion(tab1[1:], tab2) #on prend le plus petit et on le range dans la liste que l'on va renvoyer et on rappel la fonction fusion
    else:
        return [tab2[0]] + fusion(tab2[1:], tab1) #tab2[1:] prend le paramètre de la nouvelle liste

def tri_fusion(tab) -> list:
    """
    Fonction de tri en utilisant la méthode de diviser pour régner
    """
    if len(tab) == 1 :
        return tab
    tab_gauche = [tab[x] for x in range(len(tab)//2)] #compréhension de liste
    tab_droite = [tab[x] for x in range(len(tab)//2, len(tab))]
    return fusion(tri_fusion(tab_gauche), tri_fusion(tab_droite))


"""
print(tri_fusion(fusion(liste1, liste2)))
liste1.sort()
print(liste1)
print(sorted(liste2))
print(liste2)
"""
