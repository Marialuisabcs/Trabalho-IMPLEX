import math
import random
from typing import List, Iterator


class Vertice:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.label}: ({self.x}, {self.y})'


class Grafo:
    def __init__(self):
        self.vertices = []
        self.solucao_corrente = None
        self.distancia_solucao_corrente = None
        self.filename_output = None

    @staticmethod
    def gerar_grafo(arquivo):
        g = Grafo()
        with open(arquivo, 'r') as f:
            for line in f.readlines():
                line = line.split(' ')

                linha = []
                for item in line:
                    if item != '':
                        linha.append(int(item))

                label, x, y = linha
                v = Vertice(label, x, y)
                g.vertices.append(v)

        g.filename_output = f'{arquivo[:-3]}out'
        return g

    def gerar_solucao_aleatoria(self) -> None:
        solucao = self.vertices.copy()
        random.shuffle(solucao)
        self.solucao_corrente = solucao

    def calcula_distancia_solucao_corrente(self) -> None:
        self.distancia_solucao_corrente = self.calcula_distancia_total(self.solucao_corrente)

    def troca_solucao_corrente(self, solucao, dist_solucao) -> Iterator[List[Vertice]]:
        self.solucao_corrente = solucao
        self.distancia_solucao_corrente = dist_solucao
        return self.vizinho_generator()

    def vizinho_generator(self) -> Iterator[List[Vertice]]:
        for i in range(len(self.solucao_corrente)):
            for j in range(i + 1, len(self.solucao_corrente)):
                vizinho = self.solucao_corrente.copy()
                vizinho[i] = self.solucao_corrente[j]
                vizinho[j] = self.solucao_corrente[i]
                yield vizinho

    @staticmethod
    def calcula_distancia(a: Vertice, b: Vertice) -> float:
        """
        Calcula a distância euclidiana dos vértices fornecidos.
            :param a: Vértice a
            :param b: Vértice b
            :return: distância euclidiana
        """

        radicando = ((a.x - b.x) ** 2) + ((a.y - b.y) ** 2)
        return math.sqrt(radicando)

    @staticmethod
    def calcula_distancia_total(solucao: List[Vertice]) -> float:
        """
        Calcula a distância total de uma determinada solução
            :param solucao: Solução cuja distância total deseja-se calcular.
            :return: Distância total da solução
        """

        distancia_total = 0
        i = 0
        while i < len(solucao) - 1:
            distancia_total += Grafo.calcula_distancia(solucao[i], solucao[i+1])
            i += 1
        distancia_total += Grafo.calcula_distancia(solucao[-1], solucao[0])

        return distancia_total

    def salvar(self):
        with open(self.filename_output, 'w') as f:
            linha = f'Distância percorrida: {self.distancia_solucao_corrente}\n'
            f.write(linha)
