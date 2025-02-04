# Programme Python pour trouver la somme maximale d'un sous-tableau en utilisant des boucles imbriquées

# Fonction pour trouver la somme maximale d'un sous-tableau
def maxSubarraySum(arr):
    res = arr[0]
  
    # Boucle externe pour le point de départ du sous-tableau
    for i in range(len(arr)):
        currSum = 0
      
        # Boucle interne pour le point de fin du sous-tableau
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
          
            # Mise à jour de res si currSum est supérieur à res
            res = max(res, currSum)
          
    return res

if __name__ == "__main__":
    test_cases = [
        [2, 3, -8, 7, -1, 2, 3],
        [-2, -3, 4, -1, -2, 1, 5, -3],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [10, -3, -2, 5, 7, -1, 2]
    ]
    
    for i, arr in enumerate(test_cases):
        print(f"Test {i+1}: Tableau {arr} -> Somme max: {maxSubarraySum(arr)}")
