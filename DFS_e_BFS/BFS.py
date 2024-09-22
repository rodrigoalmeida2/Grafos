import cria_matriz as cm

# Função de Busca em Largura (BFS)
def bfs(matriz, inicio):
    visitado = set()  # Conjunto para armazenar os nós visitados
    fila = [inicio]  # Fila representada por uma lista simples
    visitado.add(inicio)

    while fila:
        # Remove o primeiro elemento da fila
        no_atual = fila.pop(0)
        print(f'Visitando nó {no_atual}')
        
        # Para cada vizinho conectado ao nó atual, se ainda não foi visitado, adiciona à fila
        for vizinho, conectado in enumerate(matriz[no_atual]):
            if conectado == 1 and vizinho not in visitado:
                visitado.add(vizinho)
                fila.append(vizinho)

no = 2
print(f"Fazendo uma busca em profundidade(DFS)|Início = {no}")
bfs(cm.matriz_adjacencia, no)

#Aluno= Rodrigo da Silva de Almeida
#Matrícula= 201911140006