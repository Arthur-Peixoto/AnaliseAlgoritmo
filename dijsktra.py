import heapq

class Node:
    def __init__(self, state, parent=None, g=0):
        self.state = state
        self.parent = parent
        self.g = g  # custo acumulado do nó inicial até este nó

    def __lt__(self, other):
        return self.g < other.g

def dijkstra(graph, start, goal=None):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = predecessors[current_node]
            return path[::-1], distances

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    if goal:
        return None, None  # Se o objetivo não foi encontrado, retorna None

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
path, distances = dijkstra(graph_complex, start_node, goal_node)
print("Caminho encontrado:", path)
print("Distâncias mínimas a partir do nó inicial '{}': {}".format(start_node, distances))
