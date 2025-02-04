# Code Python3 pour implémenter la recherche binaire itérative.

# Il renvoie l'emplacement de a dans le tableau donné arr
def binarySearch(tab, min, max, a):
    while min <= max:
        mid = min + (max - min) // 2
        
        # Vérifier si a est présent à mi-parcours
        if tab[mid] == a:
            return mid
        
        # Si a est plus grand, ignorer la moitié gauche
        elif tab[mid] < a:
            min = mid + 1
        
       # Si x est plus petit, ignorer la moitié droite
        else:
            max = mid - 1
    
    # Si nous arrivons ici, c'est que l'élément n'était pas présent
    return -1

# main
if __name__ == '__main__':
    test_cases = [
        ([2, 3, 4, 10, 40], 10),
        ([1, 5, 8, 12, 20], 8),
        ([3, 6, 9, 15, 30], 7),
        ([0, 2, 4, 6, 8, 10], 6),
        ([10, 20, 30, 40, 50], 25)
    ]
    
    for i, (tab, a) in enumerate(test_cases):
        result = binarySearch(tab, 0, len(tab) - 1, a)
        if result != -1:
            print(f"Test {i+1}: Element {a} is present at index {result} in {tab}")
        else:
            print(f"Test {i+1}: Element {a} is not present in {tab}")
