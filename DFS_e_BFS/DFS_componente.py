import cria_matriz as cm

# Função de DFS adaptada para encontrar componentes conectados
def dfs(matriz, inicio, visitado, componente_atual):
    # Marca o nó atual como visitado e o adiciona ao componente atual
    visitado.add(inicio)
    componente_atual.append(inicio)
    
    # Explora todos os vizinhos do nó atual que ainda não foram visitados
    for vizinho, conectado in enumerate(matriz[inicio]):
        if conectado == 1 and vizinho not in visitado:
            dfs(matriz, vizinho, visitado, componente_atual)

# Função para encontrar e exibir todos os componentes conectados
def encontrar_componentes_conectados(matriz):
    visitado = set()  # Conjunto para armazenar os nós visitados
    componentes = []   # Lista para armazenar todos os componentes conectados
    
    # Itera sobre todos os vértices
    for vertice in range(len(matriz)):
        if vertice not in visitado:
            # Se o vértice ainda não foi visitado, iniciamos uma nova DFS
            componente_atual = []
            dfs(matriz, vertice, visitado, componente_atual)
            componentes.append(componente_atual)  # Adiciona o componente encontrado à lista

    # Exibe os componentes conectados
    for i, componente in enumerate(componentes):
        print(f"Componente {i + 1}: {componente}")

encontrar_componentes_conectados(cm.matriz_adjacencia)

#Rodrigo da silva Almeida
#201911140006