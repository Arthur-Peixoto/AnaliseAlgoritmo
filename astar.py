def astar(graph, start, end):
    open_set = PriorityQueue()
    open_set.put(start, 0)
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, end)
    
    while not open_set.empty():
        current = open_set.get()
        
        if current == end:
            return reconstruct_path(came_from, end)
        
        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + graph[current][neighbor]
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, end)
                open_set.put(neighbor, f_score[neighbor])
                
    return None
