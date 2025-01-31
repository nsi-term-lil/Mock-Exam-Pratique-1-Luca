#EXERCICE 1 (10 points)

#L’opérateur « ou exclusif » entre deux bits renvoie 0 si les deux bits sont égaux et 1 s’ils sont
#différents. Il est symbolisé par le symbole ⊕. Ainsi :
#• 0 ⊕ 0 = 0
#• 0 ⊕ 1 = 1
#• 1 ⊕ 0 = 1
#• 1 ⊕ 1 = 0
#Écrire une fonction ou_exclusif qui prend en paramètres deux tableaux de 0 ou de 1 de
#même longueur et qui renvoie un tableau où l’élément situé à position i est le résultat, par
#l’opérateur « ou exclusif », des éléments à la position i des tableaux passés en paramètres.
#Exemples :
#>>> ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0])
#[1, 1, 0, 1, 1, 0, 0, 1]
#>>> ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1])
#[1, 1, 1, 0]

def ou_exclusif(tab1, tab2):
    res = []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            res.append(0)
        else:
            res.append(1)
    return res

assert ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]) == [1, 1, 0, 1, 1, 0, 0, 1]
assert ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]) == [1, 1, 1, 0]