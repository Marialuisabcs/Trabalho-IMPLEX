from metaheuristicas import HillClimbing, SimulatedAnnealing, Grafo


def escreve_saida(metaheuristica, algoritmo, melhores_solucoes, instancia):
    distancia = round(algoritmo.grafo.distancia_solucao_corrente)
    melhor_dist = melhores_solucoes[instancia]
    diferenca = distancia - melhor_dist

    line = f'{metaheuristica} : {instancia} : {distancia} : {melhor_dist} : {diferenca}\n'
    print(line)
    with open('dados/solucoes.txt', 'a') as out:
        out.write(line)


def gera_resultados_hc(dados, melhores_solucoes):
    for dado in dados:
        instancia = dado[:-8]
        grafo = Grafo(f'dados/{dado}')
        grafo.ler_vertices()
        hc = HillClimbing(grafo)
        hc.run()

        escreve_saida('hill climbing', hc, melhores_solucoes, instancia)


def gera_resultados_sa(dados, melhores_solucoes):
    for dado in dados:
        instancia = dado[:-8]
        grafo = Grafo(f'dados/{dado}')
        grafo.ler_vertices()
        sa = SimulatedAnnealing(grafo, len(grafo.vertices) ** (1 / 2), 0.99999, 1e-8, 10000)
        sa.run()

        escreve_saida('simulated annealing', sa, melhores_solucoes, instancia)


def main():
    dados = ['att48.tsp.txt', 'berlin52.tsp.txt', 'bier127.tsp.txt', 'eil101.tsp.txt', 'eil76.tsp.txt',
             'kroA100.tsp.txt', 'kroE100.tsp.txt', 'pr76.tsp.txt', 'rat99.tsp.txt', 'st70.tsp.txt']

    melhores_solucoes = {
        'att48': 10628,
        'berlin52': 7542,
        'bier127': 118282,
        'eil76': 538,
        'eil101': -1,
        'kroA100': 21282,
        'kroE100': 22068,
        'pr76': 108159,
        'rat99': 1211,
        'st70': 675,
    }

    gera_resultados_sa(dados, melhores_solucoes)
    gera_resultados_hc(dados, melhores_solucoes)


if __name__ == '__main__':
    main()
