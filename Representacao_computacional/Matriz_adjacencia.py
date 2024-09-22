import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Matriz de adjacência ponderada
#     A  B  C  D  E  F
matriz_adjacencia = np.array([
    [0, 2, 0, 1, 0, 0],  # A
    [0, 0, 3, 0, 0, 0],  # B
    [0, 0, 0, 0, 4, 0],  # C
    [0, 0, 0, 0, 0, 5],  # D
    [0, 0, 0, 0, 0, 0],  # E
    [0, 1, 0, 0, 0, 0]   # F
])

# Criando um grafo direcionado
grafo = nx.DiGraph()

# Adicionando nós ao grafo
n = len(matriz_adjacencia)
grafo.add_nodes_from(range(n))

# Adicionando arestas ao grafo com pesos
for i in range(n):
    for j in range(n):
        if matriz_adjacencia[i][j] > 0:
            grafo.add_edge(i, j, weight=matriz_adjacencia[i][j])

# Renomeando os nós (opcional, se você quiser usar rótulos como A, B, C, etc.)
rotulos = {i: chr(65+i) for i in range(n)}
grafo = nx.relabel_nodes(grafo, rotulos)

# Desenhando o grafo com pesos nas arestas
pos = nx.spring_layout(grafo)  # Para uma disposição agradável dos nós
nx.draw(grafo, pos, with_labels=True, node_color='lightblue', font_weight='bold')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=nx.get_edge_attributes(grafo, 'weight'))
plt.show()
