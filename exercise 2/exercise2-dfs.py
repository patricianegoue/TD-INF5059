def dfs_rec(graph, visited, node):
    # Marquer le sommet actuel comme visité
    visited[node] = True

    # Afficher le sommet actuel
    print(node, end=" ")

    # Visiter récursivement tous les sommets adjacents non visités
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs_rec(graph, visited, neighbor)


def dfs(graph, start_node):
    visited = [False] * len(graph)
    # Appel de la fonction récursive DFS
    dfs_rec(graph, visited, start_node)

def add_edge(graph, node1, node2):
    # Ajouter une arête entre deux sommets
    graph[node1].append(node2)
    graph[node2].append(node1)
    
if __name__ == "__main__":
    num_nodes = 6

    # Création de la liste d'adjacence pour le graphe
    graph = [[] for _ in range(num_nodes)]

    # Définition des arêtes du graphe
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]

    # Ajout des arêtes au graphe
    for edge in edges:
        add_edge(graph, edge[0], edge[1])

    start_node = 0
    print("DFS à partir du sommet:", start_node)
    dfs(graph, start_node)
