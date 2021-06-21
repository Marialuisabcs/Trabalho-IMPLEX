from typing import List, Iterator, Tuple

from utils import Grafo, Vertice


class HillClimbing:
    def __init__(self, grafo: Grafo, max_iter: int = 0):
        self.grafo = grafo
        self.max_iter = max_iter
        self.i = 0

    def achar_melhor_vizinho(self, vizinhos: Iterator[List[Vertice]]) -> Tuple[List[Vertice], float]:
        """
        Descobre o melhor vizinho da lista de vizinhos.
            :param vizinhos: lista com os vizinhos da solução corrente.
            :return: melhor vizinho encontrado e a sua distância percorrida.
        """
        melhor_vizinho = next(vizinhos)
        melhor_distancia = self.grafo.calcula_distancia_total(melhor_vizinho)

        for vizinho in vizinhos:
            distancia_vizinho = self.grafo.calcula_distancia_total(vizinho)

            if distancia_vizinho < melhor_distancia:
                melhor_vizinho = vizinho
                melhor_distancia = distancia_vizinho

        return melhor_vizinho, melhor_distancia

    def continua(self) -> bool:
        """
        Determina se o algoritmo continua a busca por soluções melhores dado o índice da iteração atual.
            :return: verdadeiro se não houver máximo de iterações ou o índice da iteração atual for menor que o máximo.
        """
        return self.i < self.max_iter if self.max_iter else True

    def run(self) -> Tuple[List[Vertice], float]:
        """
        Executa o algoritmo até achar a solução ótima local ou atingir o limite de iterações.
            :return: solução ótima local e a distância percorrida.
        """
        self.grafo.gerar_solucao_aleatoria()
        self.grafo.calcula_distancia_solucao_corrente()

        vizinhos = self.grafo.vizinho_generator()
        melhor_vizinho, melhor_distancia = self.achar_melhor_vizinho(vizinhos)

        while melhor_distancia < self.grafo.distancia_solucao_corrente and self.continua():
            vizinhos = self.grafo.troca_solucao_corrente(melhor_vizinho, melhor_distancia)

            melhor_vizinho, melhor_distancia = self.achar_melhor_vizinho(vizinhos)
            self.i += 1

        return self.grafo.solucao_corrente, self.grafo.distancia_solucao_corrente


def main():
    grafo = Grafo('../dados/att48.tsp.txt')
    grafo.ler_vertices()
    hc = HillClimbing(grafo)
    solucao, distancia = hc.run()
    print(distancia)


if __name__ == '__main__':
    main()
