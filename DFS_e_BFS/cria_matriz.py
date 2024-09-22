# Função para criar uma matriz de adjacência simples
def cria_matriz_adjacencia(n):
    # n é o número de vértices, a matriz começa com zeros (sem conexões)
    matriz = [[0 for _ in range(n)] for _ in range(n)]
    return matriz

# Adiciona aresta entre dois nós
def adicionar_aresta(matriz, u, v):
    matriz[u][v] = 1
    matriz[v][u] = 1

# Função para mostrar a matriz de adjacência
def mostrar_matriz(matriz):
    print("Matriz de Adjacência:")
    for linha in matriz:
        print(" ".join(map(str, linha)))
    print()

def mostrar_grafo(matriz):
    print("Grafo (vértices e arestas):")
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j] == 1:
                print(f"{i} -- {j}")
    print()

# Número de vértices
n = 5

# Criação da matriz de adjacência
matriz_adjacencia = cria_matriz_adjacencia(n)

# Adiciona arestas (conexões) entre os vértices
adicionar_aresta(matriz_adjacencia, 0, 1)
adicionar_aresta(matriz_adjacencia, 0, 3)
adicionar_aresta(matriz_adjacencia, 1, 2)
adicionar_aresta(matriz_adjacencia, 2, 3)
adicionar_aresta(matriz_adjacencia, 3, 4)

# Exibe a matriz de adjacência
mostrar_matriz(matriz_adjacencia)
mostrar_grafo(matriz_adjacencia)