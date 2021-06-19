import math
import random
from typing import Tuple, List

from utils import Grafo, Vertice


class SimulatedAnnealing:
    def __init__(self, grafo: Grafo, t_max: float, tx_resfria: float, t_min: float, max_iter: int):
        self.grafo = grafo
        self.t_atual = t_max
        self.t_max = t_max
        self.tx_resfria = tx_resfria
        self.t_min = t_min
        self.max_iter = max_iter
        self.i = 0

    def resfria(self):
        """
        Reduz a temperatura atual dada a taxa de resfriamento.
        """
        self.t_atual *= self.tx_resfria

    def prob_aceita(self, dist_vizinho: float) -> float:
        """
        Calcula a probabilidade de aceitação de uma solução pior que a corrente.
            :param dist_vizinho: distância percorrida pelo vizinho.
            :return: valor da probabilidade.
        """
        return math.exp(-abs((dist_vizinho - self.grafo.distancia_solucao_corrente) / self.t_atual))

    def run(self) -> Tuple[List[Vertice], float]:
        """
        Executa o algoritmo até atingir a temperatura mínima ou o limite de iterações.
            :return: última solução encontrada e a distância percorrida.
        """
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
                vizinhos = self.grafo.troca_solucao_corrente(vizinho, distancia_vizinho)

            elif random.random() < self.prob_aceita(distancia_vizinho):
                vizinhos = self.grafo.troca_solucao_corrente(vizinho, distancia_vizinho)

            self.resfria()
            self.i += 1

        return self.grafo.solucao_corrente, self.grafo.distancia_solucao_corrente


def main():
    grafo = Grafo('../dados/att48.tsp.txt')
    grafo.ler_vertices()
    sa = SimulatedAnnealing(grafo, 7, 0.995, 1e-8, 6000)
    solucao, distancia = sa.run()
    print(distancia)


if __name__ == '__main__':
    main()
