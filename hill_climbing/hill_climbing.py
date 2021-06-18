import os
from typing import Union
from utils import Grafo


class HillClimbing:
    def __init__(self, arquivo: Union[str, bytes, os.PathLike]):
        self.grafo = Grafo.gerar_grafo(arquivo)

    def achar_melhor_vizinho(self, vizinho_generator):
        melhor_vizinho = next(vizinho_generator)
        melhor_distancia = self.grafo.calcula_distancia_total(melhor_vizinho)

        for vizinho in vizinho_generator:
            distancia_vizinho = self.grafo.calcula_distancia_total(vizinho)

            if distancia_vizinho < melhor_distancia:
                melhor_vizinho = vizinho
                melhor_distancia = distancia_vizinho

        return melhor_vizinho, melhor_distancia

    def run(self):
        self.grafo.gerar_solucao_aleatoria()
        self.grafo.calcula_distancia_solucao_corrente()

        vizinho_generator = self.grafo.vizinho_generator()
        melhor_vizinho, melhor_distancia = self.achar_melhor_vizinho(vizinho_generator)

        while melhor_distancia < self.grafo.distancia_solucao_corrente:
            self.grafo.solucao_corrente = melhor_vizinho
            self.grafo.distancia_solucao_corrente = melhor_distancia

            vizinho_generator = self.grafo.vizinho_generator()
            melhor_vizinho, melhor_distancia = self.achar_melhor_vizinho(vizinho_generator)

        return self.grafo.solucao_corrente, self.grafo.distancia_solucao_corrente


if __name__ == '__main__':
    hc = HillClimbing('../dados/att48.tsp.txt')
    sc, dsc = hc.run()
    for v in sc:
        print(v)

    print(dsc)
