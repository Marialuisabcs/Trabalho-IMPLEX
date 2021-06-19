from utils import Grafo


class HillClimbing:
    def __init__(self, grafo: Grafo, max_iter: int = 0):
        self.grafo = grafo
        self.max_iter = max_iter
        self.i = 0

    def achar_melhor_vizinho(self, vizinho_generator):
        melhor_vizinho = next(vizinho_generator)
        melhor_distancia = self.grafo.calcula_distancia_total(melhor_vizinho)

        for vizinho in vizinho_generator:
            distancia_vizinho = self.grafo.calcula_distancia_total(vizinho)

            if distancia_vizinho < melhor_distancia:
                melhor_vizinho = vizinho
                melhor_distancia = distancia_vizinho

        return melhor_vizinho, melhor_distancia

    def continua(self):
        return self.i < self.max_iter if self.max_iter else True

    def run(self):
        self.grafo.gerar_solucao_aleatoria()
        self.grafo.calcula_distancia_solucao_corrente()

        vizinho_generator = self.grafo.vizinho_generator()
        melhor_vizinho, melhor_distancia = self.achar_melhor_vizinho(vizinho_generator)

        while melhor_distancia < self.grafo.distancia_solucao_corrente and self.continua():
            self.grafo.solucao_corrente = melhor_vizinho
            self.grafo.distancia_solucao_corrente = melhor_distancia

            vizinho_generator = self.grafo.vizinho_generator()
            melhor_vizinho, melhor_distancia = self.achar_melhor_vizinho(vizinho_generator)
            self.i += 1

        return self.grafo.solucao_corrente, self.grafo.distancia_solucao_corrente


if __name__ == '__main__':
    grafo = Grafo.gerar_grafo('../dados/att48.tsp.txt')
    hc = HillClimbing(grafo)
    solucao, distancia = hc.run()
    print(distancia)
