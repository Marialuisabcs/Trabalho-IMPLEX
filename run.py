from metaheuristicas import HillClimbing, SimulatedAnnealing
from utils import Grafo
import time

if __name__ == '__main__':
    grafo = Grafo.gerar_grafo('dados/berlin52.tsp.txt')

    hc = HillClimbing(grafo, max_iter=1000)
    inicio = round(time.time() * 1000)
    _, distancia = hc.run()
    print(f'Tempo do Hill Climbing: {round(time.time() * 1000) - inicio}')
    print(distancia)
    hc.grafo.desenhar_solucao('HC')

    print('='*30)

    sa = SimulatedAnnealing(grafo, t_max=10**10, tx_resfria=0.995, t_min=1e-15, max_iter=10**10)
    inicio = round(time.time() * 1000)
    _, distancia = sa.run()
    print(f'Tempo do Simulated Annealing: {round(time.time() * 1000) - inicio}')
    print(distancia)
    sa.grafo.desenhar_solucao('SA')
