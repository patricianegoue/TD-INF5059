from collections import deque

def bfs_shortest_path(graph, start_location, end_location):
    if start_location == end_location:
        return [start_location]
    
    queue = deque([(start_location, [start_location])])
    visited = set()
    visited.add(start_location)
    
    while queue:
        current, path = queue.popleft()
        
        for neighbor in graph[current]:
            if neighbor == end_location:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # Aucun chemin trouvé

# Fonction pour ajouter une arête au graphe
def add_edge(graph, location1, location2):
    graph[location1].append(location2)
    graph[location2].append(location1)

# Exemple d'utilisation
if __name__ == "__main__":
    graph = {
        'Paris': ['Lyon', 'Marseille'],
        'Lyon': ['Paris', 'Bordeaux', 'Toulouse'],
        'Marseille': ['Paris', 'Nice'],
        'Bordeaux': ['Lyon'],
        'Toulouse': ['Lyon', 'Nice'],
        'Nice': ['Marseille', 'Toulouse']
    }
    
    start_location = 'Paris'
    end_location = 'Nice'
    path = bfs_shortest_path(graph, start_location, end_location)
    
    if path:
        print(f"Le chemin le plus court entre {start_location} et {end_location} est: {' -> '.join(path)}")
    else:
        print(f"Aucun chemin trouvé entre {start_location} et {end_location}")
