import random
import networkx as nx
import matplotlib.pyplot as plt

def sparse_graph(num_nodes, edge_probability, weight_range=(1, 10)):
    graph = {}
    for node in range(num_nodes):
        graph[node] = {}
        for neighbor in range(num_nodes):
            if node != neighbor and random.random() < edge_probability:
                weight = random.randint(*weight_range)
                graph[node][neighbor] = weight
    return graph

def dense_graph(num_nodes, max_weight=10):
    graph = {}
    for node in range(num_nodes):
        graph[node] = {}
        for neighbor in range(num_nodes):
            if node != neighbor:
                weight = random.randint(1, max_weight)
                graph[node][neighbor] = weight
    return graph

def negative_cycle_graph(num_nodes, max_weight=10):
    graph = dense_graph(num_nodes, max_weight)
    # Adiciona um ciclo negativo
    for node in range(num_nodes):
        for neighbor in graph[node]:
            graph[neighbor][node] = -random.randint(1, max_weight)
    return graph

def negative_weight_graph(num_nodes, max_weight=10):
    graph = dense_graph(num_nodes, max_weight)
    # Adiciona algumas arestas com pesos negativos
    for node in range(num_nodes):
        for neighbor in graph[node]:
            if random.random() < 0.2:
                graph[node][neighbor] = -random.randint(1, max_weight)
    return graph

def unreachable_goal_graph(num_nodes):
    graph = sparse_graph(num_nodes, 0.1)
    # Adiciona um objetivo inacessível
    goal_node = num_nodes + 1
    for node in graph:
        graph[node][goal_node] = random.randint(1, 10)
    return graph

def nearby_vs_distant_goal_graph(num_nodes, distance_factor=0.1):
    graph = sparse_graph(num_nodes, 0.2)
    # Adiciona dois objetivos: um próximo e outro distante
    goal_node_nearby = num_nodes + 1
    goal_node_distant = num_nodes + 2
    for node in graph:
        graph[node][goal_node_nearby] = random.randint(1, 10)
        graph[node][goal_node_distant] = random.randint(1, 10) + int(num_nodes * distance_factor)
    return graph

# Exemplo de uso para gerar e visualizar um grafo
graph = dense_graph(10)
G = nx.Graph(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
