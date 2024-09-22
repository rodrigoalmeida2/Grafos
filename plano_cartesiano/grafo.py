class Grafo:
    def __init__(self):
        self.vertices = set()  # Conjunto de vértices
        self.arestas = {}      # Dicionário para arestas: {vértice: conjunto de adjacências}

    def adicionar_vertice(self, v):
        if v not in self.vertices:
            self.vertices.add(v)
            self.arestas[v] = set()

    def adicionar_aresta(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.arestas[u].add(v)
            self.arestas[v].add(u)  # Grafo não orientado

    def produto_cartesiano(self, outro_grafo):
        produto = Grafo()

        # Adiciona os vértices ao grafo produto
        for u in self.vertices:
            for v in outro_grafo.vertices:
                produto.adicionar_vertice((u, v))

        # Adiciona as arestas ao grafo produto
        for (u1, v1) in produto.vertices:
            for (u2, v2) in produto.vertices:
                if u1 == u2 and (v1 in outro_grafo.arestas[v2]):
                    produto.adicionar_aresta((u1, v1), (u2, v2))
                elif v1 == v2 and (u1 in self.arestas[u2]):
                    produto.adicionar_aresta((u1, v1), (u2, v2))

        return produto

    def __str__(self):
        return f"Vértices: {self.vertices}\nArestas: {[(u, v) for u in self.arestas for v in self.arestas[u]]}"

# Exemplo de uso
g1 = Grafo()
g1.adicionar_vertice(1)
g1.adicionar_vertice(2)
g1.adicionar_aresta(1, 2)

g2 = Grafo()
g2.adicionar_vertice('A')
g2.adicionar_vertice('B')
g2.adicionar_aresta('A', 'B')

produto = g1.produto_cartesiano(g2)
print(produto)
