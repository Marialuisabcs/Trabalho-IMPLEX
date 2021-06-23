import math
import pandas as pd
import streamlit as st
from metaheuristicas import HillClimbing, SimulatedAnnealing
from metaheuristicas.utils import Grafo


def main():
    st.sidebar.title('TSP com metaheurísticas')

    options_heuristica = {
        'Hill Climbing': hill_climbing,
        'Simulated Annealing': simulated_annealing
    }

    heuristica = st.sidebar.selectbox('Metaheurística', tuple(options_heuristica.keys()))
    arquivos = ['att48.tsp.txt', 'berlin52.tsp.txt', 'bier127.tsp.txt', 'eil101.tsp.txt', 'eil76.tsp.txt',
                'kroA100.tsp.txt', 'kroE100.tsp.txt', 'pr76.tsp.txt', 'rat99.tsp.txt', 'st70.tsp.txt']
    entrada = st.sidebar.selectbox('Arquivo de entrada', arquivos)
    grafo = Grafo(f'dados/{entrada}')
    grafo.ler_vertices()
    options_heuristica[heuristica](grafo)


def mostra_infos(grafo):
    fig = grafo.desenhar_solucao('SA')
    st.pyplot(fig)
    df = pd.DataFrame(columns=['head', 'tail', 'distance'])
    i = 0
    while i < len(grafo.solucao_corrente) - 1:
        a, b = grafo.solucao_corrente[i], grafo.solucao_corrente[i + 1]
        row = {
            'head': a.label,
            'tail': b.label,
            'distance': Grafo.calcula_distancia(a, b)
        }
        df = df.append(row, ignore_index=True)
        i += 1

    st.table(df)


def hill_climbing(grafo):
    st.title('Hill Climbing')

    max_iter = st.number_input('Máximo de iterações', min_value=0,
                               help='Para executar até encontrar o ótimo local, use o valor 0.')

    if st.button('Executar'):
        hc = HillClimbing(grafo, max_iter=max_iter)
        hc.run()
        mostra_infos(hc.grafo)


def simulated_annealing(grafo):
    st.title('Simulated Annealing')

    max_iter = st.number_input('Máximo de iterações', min_value=1, value=5000)
    t_max = st.number_input('Temperatura máxima', min_value=1.0, value=math.sqrt(len(grafo.vertices)))
    tx_resfria = st.number_input('Taxa de resfriamento', min_value=0.01, max_value=1.0, value=0.995)
    t_min = st.number_input('Temperatura mínima', min_value=1e-15, value=1e-8, help='Valor padrão: 1e-8.')

    if st.button('Executar'):
        sa = SimulatedAnnealing(grafo, t_max=t_max, tx_resfria=tx_resfria, t_min=t_min, max_iter=max_iter)
        sa.run()
        mostra_infos(sa.grafo)


if __name__ == '__main__':
    main()
