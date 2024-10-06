def cria_grafo():
    grafo = {
    0: [1],       # 0 -> 1
    1: [2, 3],    # 1 -> 2, 1 -> 3
    2: [3],       # 2 -> 3
    3: [],        # 3 não tem dependências
    4: [5, 0],       # 4 -> 5
    5: []         # 5 não tem dependências
    }
    return grafo

def tem_ciclo(grafo):
    def dfs(v):
        if visitado[v] == 1:  # Se está em processo, há um ciclo
            return True
        if visitado[v] == 2:  # Se já foi completamente visitado, não há ciclo por aqui
            return False
        
        visitado[v] = 1  # Marcar como em processo
        for vizinho in grafo[v]:
            if dfs(vizinho):  # Se algum vizinho leva a um ciclo, retornar True
                return True
        
        visitado[v] = 2  # Marcar como completamente visitado
        return False
    
    # Inicializando todos os nós como não visitados
    visitado = {node: 0 for node in grafo}  # 0: Não visitado, 1: Em processo, 2: Visitado

    # Executar DFS para cada nó
    for v in grafo:
        if visitado[v] == 0:  # Iniciar DFS apenas em nós não visitados
            if dfs(v):  # Se algum caminho contém um ciclo, retornamos True
                return True
    
    return False  # Se nenhum ciclo for encontrado, retornar False


if __name__=="__main__":
    grafo = cria_grafo()
    print(tem_ciclo(grafo))

# Rodrigo da Silva Almeida
# 201911140006