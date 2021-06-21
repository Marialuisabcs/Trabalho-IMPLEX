import math
import os
import random
from typing import List, Iterator, Union
import matplotlib.pyplot as plt


class Vertice:
    """Armazena informações de um vértice, sendo essas: rótulo, e coordenadas x, y no ponto cartesiano"""
    def __init__(self, label: str, x: float, y: float):
        self.label = label
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.label}: ({self.x}, {self.y})'


class Grafo:
    """Armazena e faz operações rotineiras no grafo"""
    def __init__(self, entrada: Union[str, bytes, os.PathLike]):
        self.vertices: List[Vertice] = []
        self.solucao_corrente: List[Vertice] = []
        self.distancia_solucao_corrente: float = 0
        self.entrada = entrada
        self.saida: str = f'{self.entrada[:-3]}out'

    def ler_vertices(self):
        """
        Define a lista de vértices atual a partir do arquivo de entrada.
        """
        vertices = []
        with open(self.entrada, 'r') as f:
            for line in f.readlines():
                line = line.split(' ')

                linha = []
                for item in line:
                    if item not in ('', '\n'):
                        linha.append(float(item))

                if linha:
                    label, x, y = linha

                v = Vertice(str(label), x, y)
                vertices.append(v)

        self.vertices = vertices

    def gerar_solucao_aleatoria(self) -> None:
        """
        Embaralha a ordem dos vértices e torna esta a solução corrente.
        """
        solucao = self.vertices.copy()
        random.shuffle(solucao)
        self.solucao_corrente = solucao

    def calcula_distancia_solucao_corrente(self) -> None:
        """
        Calcula a distância percorrida da solução corrente.
        """
        self.distancia_solucao_corrente = self.calcula_distancia_total(self.solucao_corrente)

    def troca_solucao_corrente(self, solucao: List[Vertice], dist_solucao: float) -> Iterator[List[Vertice]]:
        """
        Realiza a troca da atual solução corrente e gera seus vizinhos.
            :param solucao: nova solução corrente.
            :param dist_solucao: distância da nova solução corrente.
            :return: vizinhos da nova solução corrente.
        """
        self.solucao_corrente = solucao
        self.distancia_solucao_corrente = dist_solucao
        return self.vizinho_generator()

    def vizinho_generator(self) -> Iterator[List[Vertice]]:
        """
        Gera os vizinhos da solução corrente.
            :return: um iterador contendo as listas de vértices dos vizinhos, com um par de vértices trocados
                em relação à solução corrente.
        """
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
            :param a: vértice a.
            :param b: vértice b.
            :return: distância euclidiana.
        """

        radicando = ((a.x - b.x) ** 2) + ((a.y - b.y) ** 2)
        return math.sqrt(radicando)

    @staticmethod
    def calcula_distancia_total(solucao: List[Vertice]) -> float:
        """
        Calcula a distância total de uma determinada solução.
            :param solucao: solução cuja distância total deseja-se calcular.
            :return: distância total da solução.
        """

        distancia_total = 0
        i = 0
        while i < len(solucao) - 1:
            distancia_total += Grafo.calcula_distancia(solucao[i], solucao[i+1])
            i += 1
        distancia_total += Grafo.calcula_distancia(solucao[-1], solucao[0])

        return distancia_total

    def salvar(self):
        with open(self.saida, 'w') as f:
            linha = f'Distância percorrida: {self.distancia_solucao_corrente}\n'
            f.write(linha)

    def desenhar_solucao(self, name: str = 'Solução TSP', save: bool = False) -> plt.Figure:
        """"
        Desenha, em um plano cartesiano, o caminho que é percorrido pela solução corrente.
            :param name: nome dado ao arquivo onde o desenho será salvo.
            :param save: diz se o desenho deve ser salvo.
        """
        fig: plt.Figure = plt.figure(figsize=(15, 15), dpi=100)
        x, y = [], []
        for vertice in self.solucao_corrente:
            x.append(vertice.x)
            y.append(vertice.y)
            plt.plot([vertice.x], [vertice.y], marker='o', markersize=5, color="red")

        x.append(self.solucao_corrente[0].x)
        y.append(self.solucao_corrente[0].y)

        plt.plot(x, y)
        plt.title(f'{name} Distância percorrida: {round(self.distancia_solucao_corrente, 2)}')
        if save:
            plt.savefig(f'{name}.png')

        return fig
