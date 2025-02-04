from collections import deque

# Parcours BFS à partir du sommet donné start_node
def bfs(graph, start_node):
    
    # File pour BFS
    queue = deque()
    
    # Liste pour suivre les sommets visités
    visited = [False] * len(graph)

    # Marquer le sommet de départ comme visité et l'ajouter à la file
    visited[start_node] = True
    queue.append(start_node)

    # Parcours de la file
    while queue:
        
        # Retirer un sommet de la file et l'afficher
        current = queue.popleft()
        print(current, end=" ")

        # Ajouter tous les sommets adjacents non visités à la file
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

# Fonction pour ajouter une arête au graphe

def add_edge(graph, node1, node2):
    graph[node1].append(node2)
    graph[node2].append(node1)

# Exemple d'utilisation
if __name__ == "__main__":
    
    # Nombre de sommets du graphe
    num_nodes = 6

    # Représentation du graphe par liste d'adjacence
    graph = [[] for _ in range(num_nodes)]

    # Ajouter des arêtes au graphe
    add_edge(graph, 0, 1)
    add_edge(graph, 0, 2)
    add_edge(graph, 1, 3)
    add_edge(graph, 1, 4)
    add_edge(graph, 2, 5)
    add_edge(graph, 3, 5)

    # Effectuer un parcours BFS à partir du sommet 0
    print("Parcours BFS à partir du sommet 0:")
    bfs(graph, 0)
