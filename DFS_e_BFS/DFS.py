import cria_matriz as cm

# Função de Busca em Profundidade (DFS)
def dfs(matriz, inicio, visitado=None):
    if visitado is None:
        visitado = set()  # Conjunto para armazenar os nós visitados

    # Marca o nó atual como visitado
    print(f'Visitando nó {inicio}')
    visitado.add(inicio)

    # Explora todos os vizinhos do nó atual que ainda não foram visitados
    for vizinho, conectado in enumerate(matriz[inicio]):
        if conectado == 1 and vizinho not in visitado:
            dfs(matriz, vizinho, visitado)

no = 1
print(f"Fazendo uma busca em profundidade(DFS)|Início = {no}")
dfs(cm.matriz_adjacencia, no)

#Aluno= Rodrigo da Silva de Almeida
#Matrícula= 201911140006