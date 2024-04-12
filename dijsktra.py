import sys
class DijkstraAlgorithm:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    
    def minimum_distance(self, distances, visited):
        min_distance = sys.maxsize
        min_index = -1
        
        for v in range(self.V):
            if not visited[v] and distances[v] <= min_distance:
                min_distance = distances[v]
                min_index = v
                
        return min_index
    
    def print_path(self, distances, parent, source, destination):
        print(f"Caminho mínimo entre {source} e {destination}: ", end='')
        crawl = destination
        print(crawl, end='')
        
        while parent[crawl] != -1:
            print(f" <- {parent[crawl]}", end='')
            crawl = parent[crawl]
        
        print(f"\nCusto total: {distances[destination]}")
        
    def dijkstra(self, source, destination):
        distances = [sys.maxsize] * self.V
        visited = [False] * self.V
        parent = [-1] * self.V
        
        distances[source] = 0
        
        for count in range(self.V - 1):
            u = self.minimum_distance(distances, visited)
            visited[u] = True
            
            for v in range(self.V):
                if not visited[v] and self.graph[u][v] != 0 and distances[u] != sys.maxsize and distances[u] + self.graph[u][v] < distances[v]:
                  distances[v] = distances[u] + self.graph[u][v]
                  parent[v] = u
                  
        self.print_path(distances, parent, source, destination)# Programa principal para testar o algoritmo


if __name__ == "__main__":
    vertices = 5
    graph = [[0, 3, 2, 0, 0], [3, 0, 1, 5, 0], [2, 1, 0, 3, 6], [0, 5, 3, 0, 4], [0, 0, 6, 4, 0]]
    source = 0
    destination = 4
    
    dijkstra = DijkstraAlgorithm(vertices)
    dijkstra.graph = graph
    
    dijkstra.dijkstra(source, destination)