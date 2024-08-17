# from arquivo import classe
from Vertice import Vertice
import heapq

class Grafo:
    def __init__(self):
        self.Vertices = [] # Cria uma lista vazia de vértices
        
    def __str__(self):
        return f'Este grafo possui {len(self.Vertices)} vértices.'
    
    def Add_Vertice(self, label):
        # Testar se o vértice já existe
        if label not in self.Vertices:
            novoVertice = Vertice(label)
            self.Vertices.append(novoVertice)
        else:
            print("Erro: Vértice já cadastrado")
            
    def Show_Vertices(self):
        for vertice in self.Vertices:
            #print(vertice)
            vertice.Show_Adjacencias()
         
    def Add_Aresta(self, label_origem, label_destino, peso):
        # parâmetro label_origem será uma string com o label da cidade de origem
        # parâmetro label_destino será uma string com o label da cidade de destino
        # 1) Buscar o objeto "origem" na lista de vertices (origem)
        origem = None
        for vertice in self.Vertices:
            if vertice.Label == label_origem: # verifica se é o vértice com o label que estou procurando
                origem = vertice # salvo o objeto com o label que eu estava procurando
                break  # saio do loop
                
        # 2) Buscar o objeto "destino" na lista de vertices (destino)
        destino = None
        for vertice in self.Vertices:
            if vertice.Label == label_destino: # verifica se é o vértice com o label que estou procurando
                destino = vertice # salvo o objeto com o label que eu estava procurando
                break  # saio do loop
            
        # 3) Chamar o "Add_Adjacencia" do objeto (origem) e passar
        #    (destino) como parâmetro   
        if origem != None and destino != None:
            origem.Add_Adjacencia(destino, peso)
            destino.Add_Adjacencia(origem, peso)
        else:
            print('Informe origem e destino válido')

    def dijkstra(self, origem):

        distancias = {vertice.Label: float('inf') for vertice in self.Vertices}  # Usa o rótulo como chave
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            distancia_atual, label_atual = heapq.heappop(fila_prioridade)

            # Encontra o vértice com o rótulo atual
            vertice_atual = next((v for v in self.Vertices if v.Label == label_atual), None)
            if vertice_atual is None:
                continue  # Se o vértice não for encontrado, pula para a próxima iteração

            for adjacencia in vertice_atual.Adjacencias:
                vizinho = adjacencia.Destino.Label  # Obtém o rótulo do vizinho
                peso = adjacencia.Peso
                nova_distancia = distancia_atual + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        return distancias
        

