def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    for _ in range(len(graph) - 1):
        for u, v, weight in graph.edges():
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                
    for u, v, weight in graph.edges():
        if distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative-weight cycle")
            
    return distances