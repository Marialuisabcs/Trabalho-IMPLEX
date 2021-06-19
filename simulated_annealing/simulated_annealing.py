import math
import random
from utils import Grafo


class SimulatedAnnealing:
    def __init__(self, grafo: Grafo, t_max: float, tx_resfria: float, t_min: float, max_iter: float):
        self.grafo = grafo
        self.t_atual = t_max
        self.t_max = t_max
        self.tx_resfria = tx_resfria
        self.t_min = t_min
        self.max_iter = max_iter
        self.i = 0

    def resfria(self):
        self.t_atual *= self.tx_resfria

    def prob_aceita(self, dist_vizinho):
        return math.exp(-abs((dist_vizinho - self.grafo.distancia_solucao_corrente) / self.t_atual))

    def run(self):
        self.grafo.gerar_solucao_aleatoria()
        self.grafo.calcula_distancia_solucao_corrente()

        vizinhos = self.grafo.vizinho_generator()
        while self.t_atual > self.t_min and self.i < self.max_iter:
            vizinho = next(vizinhos, None)
            if not vizinho:
                vizinhos = self.grafo.vizinho_generator()
                vizinho = next(vizinhos)

            distancia_vizinho = Grafo.calcula_distancia_total(vizinho)
            distancia_corrente = self.grafo.distancia_solucao_corrente

            if distancia_vizinho < distancia_corrente:
                self.grafo.solucao_corrente = vizinho
                self.grafo.distancia_solucao_corrente = distancia_vizinho
                vizinhos = self.grafo.vizinho_generator()

            elif random.random() < self.prob_aceita(distancia_vizinho):
                self.grafo.solucao_corrente = vizinho
                self.grafo.distancia_solucao_corrente = distancia_vizinho
                vizinhos = self.grafo.vizinho_generator()

            self.resfria()
            self.i += 1

        return self.grafo.solucao_corrente, self.grafo.distancia_solucao_corrente


if __name__ == '__main__':
    grafo = Grafo.gerar_grafo('../dados/att48.tsp.txt')
    sa = SimulatedAnnealing(grafo, 7, 0.995, 1e-8, 6000)
    solucao, distancia = sa.run()
    print(distancia)
