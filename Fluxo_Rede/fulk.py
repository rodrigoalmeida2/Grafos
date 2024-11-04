from collections import defaultdict

class Grafo:
    def __init__(self, vertices):
        # Inicializa o grafo com um número de vértices
        self.V = vertices
        self.grafo = defaultdict(dict)
    
    def adicionar_aresta(self, u, v, capacidade):
        # Adiciona uma aresta ao grafo com capacidade dada
        if v not in self.grafo[u]:
            self.grafo[u][v] = capacidade
        else:
            self.grafo[u][v] += capacidade  # Caso a aresta já exista, soma a capacidade

        # Certifica-se de que a aresta reversa existe com capacidade inicial 0
        if u not in self.grafo[v]:
            self.grafo[v][u] = 0

    def _DFS(self, fonte, alvo, caminho, visitado):
        # Realiza a DFS para encontrar um caminho aumentante
        visitado.add(fonte)
        if fonte == alvo:
            return caminho
        
        for vizinho, capacidade in self.grafo[fonte].items():
            if vizinho not in visitado and capacidade > 0:
                resultado = self._DFS(vizinho, alvo, caminho + [(fonte, vizinho)], visitado)
                if resultado is not None:
                    return resultado
        return None
    
    def calcular_fluxo_maximo(self, fonte, alvo):
        fluxo_maximo = 0

        while True:
            # Encontra um caminho aumentante usando DFS
            caminho = self._DFS(fonte, alvo, [], set())
            if caminho is None:
                break  # Se não há caminho aumentante, paramos
            
            # Encontra o fluxo mínimo no caminho aumentante
            fluxo_aumentante = min(self.grafo[u][v] for u, v in caminho)
            
            # Atualiza as capacidades residuais das arestas e suas reversas
            for u, v in caminho:
                self.grafo[u][v] -= fluxo_aumentante
                self.grafo[v][u] += fluxo_aumentante  # Capacidade residual da reversa
            
            # Incrementa o fluxo total
            fluxo_maximo += fluxo_aumentante
            print(f"Caminho aumentante encontrado: {caminho}, fluxo aumentado: {fluxo_aumentante}")
        
        return fluxo_maximo

# Exemplo de uso
grafo = Grafo(4)
grafo.adicionar_aresta('s', 'a', 2)
grafo.adicionar_aresta('s', 'b', 2)
grafo.adicionar_aresta('a', 'b', 2)
grafo.adicionar_aresta('a', 't', 1)
grafo.adicionar_aresta('b', 't', 5)

# Calcular o fluxo máximo de 's' para 't'
fluxo_maximo = grafo.calcular_fluxo_maximo('s', 't')
print(f"Fluxo máximo de 's' para 't': {fluxo_maximo}")
