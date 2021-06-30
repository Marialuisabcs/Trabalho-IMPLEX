# TSP com metaheurísticas

### Descrição
TSP, o [problema do caixeiro viajante](https://pt.wikipedia.org/wiki/Problema_do_caixeiro-viajante) 
(do inglês, Travelling Salesman Problem), 
é um conhecido problema na área de computação. O problema em questão tem por objetivo 
ajudar a encontrar, dentre uma quantidade finita de locais, qual o menor caminho 
possível que se pode percorrer para que o caixeiro atinga todas as localidades 
retornando sempre ao seu ponto de origem. O problema é característico por 
ser um [NP-completo](https://pt.wikipedia.org/wiki/NP-completo). 
Com o objetivo de encontrar a solução mais próxima do ótimo global,
utilizamos as seguintes [metaheurísticas](https://pt.wikipedia.org/wiki/Meta-heur%C3%ADstica):
[Hill Climbing](https://en.wikipedia.org/wiki/Hill_climbing) e 
[Simulated Annealing](https://pt.wikipedia.org/wiki/Simulated_annealing).

### Vídeos explicativos
- [Hill Climbing](https://youtu.be/beTzgbgd1CM)
- [Simulated annealing](https://www.youtube.com/watch?v=onbOzOTqvOE)

### Instruções de execução
O trabalho foi feito utilizando a linguagem Python, na versão 3.9, portanto, 
é necessário instalar o interpretador Python.

Inicialmente, instale as dependências executando o seguinte comando no terminal:

```
pip install -r requirements.txt
```
São fornecidas 2 formas de execução:
- ### Através de uma aplicação web
  Instale a biblioteca _streamlit_ usando o comando:
  ```
  pip install streamlit
  ```
  Depos, abra o terminal no diretório raiz e execute o seguinte comando:
  ```
  streamlit run app.py
  ```
  No lado esquerdo, selecione a metaheurística e o caso de teste desejado.
  
  Ao selecionar uma metaheurística, os dados necessários serão solicitados.
 
  Após fornecer os dados, aperte 'Executar', e veja o resultado.
  

- ### Através do terminal
  Abra o terminal no diretório raiz e execute o seguinte comando:
  ```
  python run.py
  ```
  Depois disso, basta fornecer os dados conforme forem solicitados via linha de comando.
  

### Resultado do Simulated Annealing em um dos casos de teste
![Resultado 1](static-readme/simulated_annealing_result.png "Resultado 1")

### Resultado do Hill Climbing em um dos casos de teste
![Resultado 1](static-readme/hill_climbing_result.png "Resultado 1")

### Tabela com resultados obtidos
- Simulated Annealing

|instância|distância|melhor distância|diferença|
|---------|---------|----------------|---------|
|att48    |60581    |10628           |49953    |
|berlin52 |17558    |7542            |10016    |
|bier127  |416993   |118282          |298711   |
|eil101   |3178     |n.d             |n.d      |
|eil76    |2109     |538             |1571     |
|kroA100  |115444   |21282           |94162    |
|kroE100  |83547    |22068           |61479    |
|pr76     |256840   |108159          |148681   |
|rat99    |6749     |1211            |5538     |
|st70     |2928     |675             |2253     |

- Hill Climbing

|instância|distância|melhor distância|diferença|
|---------|---------|----------------|---------|
|att48    |41343    |10628           |30715    |
|berlin52 |9950     |7542            |2408     |
|bier127  |187708   |118282          |69426    |
|eil101   |1079     |n.d             |n.d      |
|eil76    |872      |538             |334      |
|kroA100  |41007    |21282           |19725    |
|kroE100  |48942    |22068           |26874    |
|pr76     |156365   |108159          |48206    |
|rat99    |2062     |1211            |851      |
|st70     |1069     |675             |394      |
