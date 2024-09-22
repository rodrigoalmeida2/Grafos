import networkx as nx
import matplotlib.pyplot as plt

# Lista de adjacência
# Cada chave do dicionário representa um nó, e cada valor é uma lista dos nós adjacentes.
lista_adjacencia = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Criando o grafo
grafo = nx.Graph()

# Adicionando as arestas ao grafo
for nodo, adjacentes in lista_adjacencia.items():
    for adj in adjacentes:
        grafo.add_edge(nodo, adj)

# Desenhando o grafo
nx.draw(grafo, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()
