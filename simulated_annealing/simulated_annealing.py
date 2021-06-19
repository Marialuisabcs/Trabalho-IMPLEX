import os
import math
import random
from typing import Union
from utils import Grafo


class SimulatedAnnealing:
    def __init__(self, arquivo: Union[str, bytes, os.PathLike]):
        self.grafo = Grafo.gerar_grafo(arquivo)
        self.temperatura_maxima: float = 0
        self.cooling_ratio: float = 0
        self.temperatura_minima: float = 0
        self.temperatura_atual: float = 0
        self.iter_atual: int = 0

    def step_1(self, t_max: float, r: float, t_min: float):
        self.temperatura_maxima = t_max
        self.cooling_ratio = r
        self.temperatura_minima = t_min
        self.temperatura_atual = t_max
        self.grafo.gerar_solucao_aleatoria()
        self.grafo.calcula_distancia_solucao_corrente()

    def step_2(self, qtd_iteracoes: int):
        vizinhos = self.grafo.vizinho_generator()
        continua = True
        vizinho = next(vizinhos, None)
        while self.iter_atual < qtd_iteracoes and vizinho:
            distancia_vizinho = self.grafo.calcula_distancia_total(vizinho)
            distancia_corrente = self.grafo.distancia_solucao_corrente

            if distancia_vizinho < distancia_corrente:
                self.grafo.solucao_corrente = vizinho
                self.grafo.distancia_solucao_corrente = distancia_vizinho

            elif random.random() < math.exp((distancia_corrente - distancia_vizinho) / self.temperatura_atual):
                self.grafo.solucao_corrente = vizinho
                self.grafo.distancia_solucao_corrente = distancia_vizinho

            vizinho = next(vizinhos, None)
            self.iter_atual += 1

        if self.iter_atual >= qtd_iteracoes:
            return self.grafo.solucao_corrente, self.grafo.distancia_solucao_corrente

        print(self.iter_atual, qtd_iteracoes)
        return None, None

    def run(self, t_max: float, r: float, t_min: float, qtd_iteracoes: int):
        self.step_1(t_max, r, t_min)
        self.step_2(qtd_iteracoes)

        print(self.temperatura_atual)
        self.temperatura_atual *= self.cooling_ratio
        print(self.temperatura_atual, self.temperatura_minima)
        if self.temperatura_atual >= self.temperatura_minima:
            solucao_corrente, distancia_solucao_corrente = self.step_2(qtd_iteracoes)
            if solucao_corrente and distancia_solucao_corrente:
                return solucao_corrente, distancia_solucao_corrente
        else:
            self.step_1(t_max, r, t_min)

    def proc(self, t_max: float, r: float, t_min: float, qtd_iteracoes: int):
        tries = 0
        while tries < qtd_iteracoes:
            self.grafo.gerar_solucao_aleatoria()
            self.grafo.calcula_distancia_solucao_corrente()



if __name__ == '__main__':
    sa = SimulatedAnnealing('../dados/teste.txt')
    sc, dsc = sa.run(1000, 0.8, 150, 3000)
    for v in sc:
        print(v)
    print(dsc)
