# Code Python pour fusionner les intervalles qui se chevauchent

def mergeOverlap(intervals):
    n = len(intervals)
    intervals.sort()
    merged = []

    # Vérification de tous les chevauchements possibles
    for i in range(n):
        start = intervals[i][0]
        end = intervals[i][1]

        # Ignorer les intervalles déjà fusionnés
        if merged and merged[-1][1] >= end:
            continue

        # Trouver la fin de l'intervalle fusionné
        for j in range(i + 1, n):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
        merged.append([start, end])
    
    return merged

if __name__ == "__main__":
    test_cases = [
        [[7, 8], [1, 5], [2, 4], [4, 6]],
        [[3, 7], [2, 6], [10, 15], [5, 9]],
        [[1, 3], [8, 10], [2, 6], [15, 18]],
        [[5, 12], [14, 20], [1, 4], [8, 10]]
    ]
    
    for i, intervals in enumerate(test_cases):
        print(f"Test {i+1}:")
        result = mergeOverlap(intervals)
        for interval in result:
            print(interval[0], interval[1])
        print()
