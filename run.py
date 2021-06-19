from metaheuristicas import HillClimbing, SimulatedAnnealing
from utils import Grafo
import time
import os


def mostra_metaheuristicas():
    print('Metaheurísticas:')
    print('\t1. Simulated Annealing')
    print('\t2. Hill Climbing')
    print()


def mostra_arquivos():
    arquivos = os.listdir('dados')
    for idx, arquivo in enumerate(arquivos):
        if idx % 3 == 0 and idx != 0:
            print()
        if idx == 6:
            print(f'{idx}. {arquivo}', end='\t\t')
            continue

        print(f'{idx}. {arquivo}', end='\t\t\t')

    return arquivos


def simulated_annealing():
    print()
    print('\t\t\t\t  ===== Simulated Annealing =====')
    arquivos = mostra_arquivos()
    print('\n')
    arquivo = input('Digite o número correspondente ao arquivo desejado: ')
    if arquivo not in list(range(len(arquivos))):
        arquivo = input('Por favor, digite uma opção válida: ')


def hill_climbing():
    pass


def main():
    print('=== Trabalho final - Implementação algorítmica ===')
    mostra_metaheuristicas()
    option = input('Digite o número referente a metaheurística desejada: ')
    while option not in ('1', '2'):
        option = input('Por favor, digite uma opção válida: ')

    if option == '1':
        simulated_annealing()

    if option == '2':
        hill_climbing()


if __name__ == '__main__':
    main()
    '''
    grafo = Grafo('dados/berlin52.tsp.txt')
    grafo.ler_vertices()

    hc = HillClimbing(grafo, max_iter=1000)
    inicio = round(time.time() * 1000)
    _, distancia = hc.run()
    print(f'Tempo do Hill Climbing: {round(time.time() * 1000) - inicio}')
    print(distancia)
    hc.grafo.desenhar_solucao('HC', save=True)

    print('='*30)

    sa = SimulatedAnnealing(grafo, t_max=10**10, tx_resfria=0.995, t_min=1e-15, max_iter=10**10)
    inicio = round(time.time() * 1000)
    _, distancia = sa.run()
    print(f'Tempo do Simulated Annealing: {round(time.time() * 1000) - inicio}')
    print(distancia)
    sa.grafo.desenhar_solucao('SA', save=True)
    '''
