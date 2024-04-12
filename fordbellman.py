def bellman_ford(graph, start, goal=None):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node

    if goal:
        path = []
        current_node = goal
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        path = path[::-1]
        return path, distances

    path = []
    for node in graph:
        current_node = node
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]
        path = path[::-1]

    return path, distances

# Exemplo de uso:
graph_complex = {
    'A': {'B': 7, 'C': 9, 'F': 14},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'A': 14, 'C': 2, 'E': 9}
}

start_node = 'A'
goal_node = 'E'  # Destino para o qual desejamos encontrar o caminho
path, distances = bellman_ford(graph_complex, start_node, goal_node)
print("Caminho encontrado:", path)
print("Distâncias mínimas a partir do nó inicial '{}': {}".format(start_node, distances))
