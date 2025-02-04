# Implémentation récursive naive du problème du sac à dos 0-1

def knapSack(capacite, poids, valeurs, n):
    # Cas de base
    if n == 0 or capacite == 0:
        return 0
    
    # Si le poids du n-ième objet est supérieur à la capacité du sac
    if poids[n-1] > capacite:
        return knapSack(capacite, poids, valeurs, n-1)
    
    # Retourne le maximum entre les deux cas possibles :
    # (1) Inclure l'objet n
    # (2) Ne pas l'inclure
    else:
        return max(
            valeurs[n-1] + knapSack(capacite - poids[n-1], poids, valeurs, n-1),
            knapSack(capacite, poids, valeurs, n-1)
        )

# Tests avec différents exemples
tests = [
    {"valeurs": [60, 100, 120], "poids": [10, 20, 30], "capacite": 50},
    {"valeurs": [10, 40, 50, 70], "poids": [1, 3, 4, 5], "capacite": 7},
    {"valeurs": [15, 25, 35, 45], "poids": [5, 10, 15, 20], "capacite": 30},
    {"valeurs": [20, 30, 40], "poids": [3, 4, 5], "capacite": 8}
]

# Exécution des tests
for i, test in enumerate(tests):
    valeurs = test["valeurs"]
    poids = test["poids"]
    capacite = test["capacite"]
    n = len(valeurs)
    resultat = knapSack(capacite, poids, valeurs, n)
    print(f"Test {i+1} - Capacité: {capacite}, Valeur maximale: {resultat}")
