"""
Fonction de vérification d'un nombre premier

Ce code contient uen fonction isprime() afin de v"rifier si un nombre est premier ou non,
et d'une fonction main() qui la teste sur les 100 premiers nombres.
"""

from math import sqrt

#### Fonction secondaire
# si un nombre n'est pas premier, il a au moins
#un diviseur qui est inféroeur ou égal à sa racine carrée


def isprime(p):
    """
    Vérifie si un nombre p est premier.
    Retourne True s'il l'est, False si il ne l'est pas.
    """

    # votre code ici
    if p <= 1:
        return False
    # on teste la boucle jusqu'à la racine carrée de p
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale


def main():
    """
    Fonction main() qui teste la fonction isprime() sur les 100 premeirs nombres.
    """

    # vos appels à la fonction secondaire ici
    print("Liste des nombres premiers entre 0 et 99:")

    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
