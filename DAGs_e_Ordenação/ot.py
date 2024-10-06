def cria_grafo():
    grafo = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2]
    }
    return grafo

def ordenacao_topologica(grafo):
    def dfs(v):
        visitado[v] = True
        for vizinho in grafo[v]:
            if not visitado[vizinho]:
                dfs(vizinho)
        order.append(v)  # Adiciona o vértice ao final da lista após explorar todos os vizinhos

    visitado = {node: False for node in grafo}  # Marcar todos os nós como não visitados
    order = []  # Lista que conterá a ordenação topológica

    # Executar DFS em cada nó não visitado
    for v in grafo:
        if not visitado[v]:
            dfs(v)

    # Reverter a lista para obter a ordenação correta
    order.reverse()
    return order

if __name__=="__main__":
    grafo = cria_grafo()
    print(ordenacao_topologica(grafo))

# Rodrigo da Silva Almeida
# 201911140006