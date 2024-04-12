import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  # custo acumulado do nó inicial até este nó
        self.h = h  # heurística - estimativa do custo deste nó até o objetivo

    def __lt__(self, other):
        return (self.g + self.h) < (other.g + other.h)

def astar(graph, start, goal, heuristic):
    open_set = []
    closed_set = set()

    start_node = Node(state=start, g=0, h=heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1], distances

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state].items():
            if neighbor in closed_set:
                continue

            g = current_node.g + cost
            h = heuristic(neighbor, goal)
            neighbor_node = Node(state=neighbor, parent=current_node, g=g, h=h)

            if g < distances[neighbor]:
                distances[neighbor] = g

            heapq.heappush(open_set, neighbor_node)

    return None, None

# Exemplo de uso:
def heuristic(state, goal):
    return 1  # Heurística simples, já que não temos informações adicionais sobre as coordenadas dos nós

# Representação do grafo como um dicionário de adjacências
graph_complex = {
    'A': {'B': 7, 'C': 9, 'F': 14},
    'B': {'A': 7, 'C': 10, 'D': 15},
    'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
    'D': {'B': 15, 'C': 11, 'E': 6},
    'E': {'D': 6, 'F': 9},
    'F': {'A': 14, 'C': 2, 'E': 9}
}

start_state = 'A'
goal_state = 'E'
path, distances = astar(graph_complex, start_state, goal_state, heuristic)

# Saída do caminho encontrado
print("Caminho encontrado:", path)

# Saída das distâncias mínimas a partir do nó inicial
print("Distâncias mínimas a partir do nó inicial '{}': {}".format(start_state, distances))
