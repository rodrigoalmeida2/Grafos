from collections import defaultdict

class Grafo:
    def __init__(self, vertices):
        # Inicializa o grafo com um número de vértices
        self.V = vertices
        self.grafo = defaultdict(dict)
    
    def adicionar_aresta(self, u, v, capacidade):
        # Adiciona uma aresta ao grafo
        if u not in self.grafo:
            self.grafo[u] = {}
        if v not in self.grafo:
            self.grafo[v] = {}

        # Define a capacidade da aresta de u para v
        self.grafo[u][v] = capacidade

        # Certifica-se de que a aresta reversa existe com capacidade inicial 0
        if v not in self.grafo[u]:
            self.grafo[v][u] = 0
        if u not in self.grafo[v]:
            self.grafo[v][u] = 0  # Inicializa a capacidade reversa com 0, se não existir

    def _DFS(self, fonte, alvo, caminho, visitado):
        # Realiza a Busca em Profundidade (DFS) para encontrar um caminho aumentante
        visitado.add(fonte)
        if fonte == alvo:
            return caminho
        
        for vizinho, capacidade in self.grafo[fonte].items():
            if vizinho not in visitado and capacidade > 0:
                # Tenta encontrar um caminho aumentante
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
                if v not in self.grafo[u]:
                    self.grafo[u][v] = 0  # Inicializa se não existir
                if u not in self.grafo[v]:
                    self.grafo[v][u] = 0  # Inicializa se não existir
                self.grafo[v][u] += fluxo_aumentante
            
            # Incrementa o fluxo total
            fluxo_maximo += fluxo_aumentante
            print(f"Caminho aumentante encontrado: {caminho}, fluxo aumentado: {fluxo_aumentante}")
        
        return fluxo_maximo

# Exemplo de uso
grafo = Grafo(4)
grafo.adicionar_aresta('s', 'a', 15)
grafo.adicionar_aresta('s', 'b', 12)
grafo.adicionar_aresta('a', 'b', 15)
grafo.adicionar_aresta('a', 't', 15)
grafo.adicionar_aresta('b', 't', 15)

# Calcular o fluxo máximo de 's' para 't'
fluxo_maximo = grafo.calcular_fluxo_maximo('s', 't')
print(f"Fluxo máximo de 's' para 't': {fluxo_maximo}")
