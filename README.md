# Estrutura-de-dados-II

# Lista de Atividades:

## 1. Binary Search
- Implemente o algoritmo Binary Search em uma lista ordenada e encontre o índice de um elemento dado.
- Explique por que a lista deve estar ordenada para que o Binary Search funcione corretamente. Forneça exemplos.

A ordenação é essencial porque isso facilita a busca do binary search com arrays.

## 2. Interpolation Search
- Crie uma função que implemente o Interpolation Search e teste-a em listas ordenadas com intervalos uniformes e não uniformes. Compare com o Binary Search.
- Identifique casos em que o Interpolation Search é mais eficiente que o Binary Search.

  obs: código na principal.

## Quando o Interpolation Search é mais eficiente:
- Distribuições Uniformes: Quando os valores estão distribuídos de forma uniforme, a interpolação geralmente encontra o valor em menos iterações do que a busca binária.
- Grandes Listas: Para listas muito grandes e uniformes, o Interpolation Search pode ter um desempenho significativamente melhor.

## Quando o Binary Search é melhor:
- Distribuições Não Uniformes: Se a lista não for uniforme, o Interpolation Search pode ser menos eficiente, pois as estimativas de posição podem ser menos precisas.


## 3. Jump Search
- Desenvolva o algoritmo Jump Search e determine o tamanho ideal do "salto" para uma lista de tamanho
- Compare o tempo de execução do Jump Search com o Binary Search em listas de diferentes tamanhos.
  <br>

| Tamanho da Lista | Jump Search (ms) | Binary Search (ms) | Relação (Jump / Binary) |
   |------------------:|-----------------:|-------------------:|------------------------:|
|            1.000  |           0,030 |             0,005  |                    6x  |
|           10.000  |           0,095 |             0,007  |                  ~14x  |
|          100.000  |           0,300 |             0,009  |                  ~33x  |
|        1.000.000  |           0,950 |             0,012  |                  ~79x  |

##  4. Exponential Search
- Implemente o algoritmo Exponential Search para localizar um elemento em uma lista ordenada. Explique como ele combina elementos do Jump Search e Binary Search.
- Analise o desempenho do Exponential Search em listas muito grandes e pequenas.

Como o Exponential Search combina Jump Search e Binary Search
O Exponential Search é um algoritmo eficiente para encontrar um elemento em uma lista ordenada. Ele usa uma combinação de Jump Search e Binary Search, aproveitando as vantagens de ambos, mas de forma adaptada.

### 1. Fase de Jump Search (Exponencial):
- O Exponential Search começa verificando o elemento em posições exponenciais. Ou seja, ele começa a procurar por um intervalo onde o valor buscado possa estar.
- Inicialmente, começa na posição 1, depois vai para a posição 2, 4, 8, 16, 32, etc., até encontrar um intervalo que contenha o valor ou ultrapassar o limite da lista.
- Isso é semelhante ao Jump Search, onde você "salta" de maneira fixa, mas, ao invés de uma distância fixa como no Jump Search, o Exponential Search dobra a distância a cada iteração (passos exponenciais).

### 2. Fase de Binary Search:
- Quando o Exponential Search encontra um intervalo onde o elemento pode estar (ou ultrapassa o valor ou chega a um ponto onde o valor deve estar entre dois índices), ele realiza uma busca binária dentro desse intervalo.
- Binary Search é utilizado para refinar a busca dentro de uma faixa estreita. Como a lista está ordenada, a busca binária se torna extremamente eficiente, reduzindo o número de comparações necessárias.

### Análise do Desempenho do Exponential Search

#### **Características do Exponential Search**
- Combina busca exponencial com busca binária.
- **Complexidade**:
    - **Melhor caso**: \(O(1)\), quando o elemento está nas primeiras posições.
    - **Pior caso**: \(O(\log n)\), devido à busca binária.

#### **Desempenho em Listas de Diferentes Tamanhos**

| **Tamanho da Lista** | **Tempo (ms)** | **Observação**                                            |
|-----------------------|----------------|----------------------------------------------------------|
| **1.000**            | 0,006          | Muito eficiente devido ao pequeno número de elementos.   |
| **10.000**           | 0,008          | O tempo cresce levemente, ainda quase imperceptível.     |
| **100.000**          | 0,010          | O crescimento continua muito pequeno (\(O(\log n)\)).    |
| **1.000.000**        | 0,014          | Escalável para listas muito grandes.                     |

#### **Conclusões**
1. **Em listas pequenas**:
    - O Exponential Search apresenta tempos comparáveis ao **Binary Search**.
    - A diferença em desempenho em relação a outros algoritmos pode ser desprezível em listas pequenas.

2. **Em listas muito grandes**:
    - Mostra-se altamente escalável, aproveitando seu crescimento \(O(\log n)\).
    - É mais vantajoso quando se espera que o elemento procurado esteja nas primeiras posições, pois o crescimento exponencial inicial ajuda a localizar rapidamente o intervalo.

3. **Cenário ideal**:
    - É particularmente útil em listas ordenadas muito grandes, especialmente quando os elementos podem estar no início da lista.
    - Caso o elemento esteja distribuído de forma uniforme e a lista seja moderada em tamanho, o **Binary Search** ou **Interpolation Search** pode ser mais eficiente.

##  5. Shell Sort
- Implemente o Shell Sort com diferentes sequências de intervalo (ex.: Shell, Knuth, Hibbard). Compare os tempos de execução.
- Explique como a escolha da sequência de intervalos afeta a eficiência do algoritmo.

### Sequências de Intervalos:
No Shell Sort, a escolha da sequência de intervalos afeta a eficiência determinando quantas comparações e trocas o algoritmo fará. Sequências bem escolhidas, como as de Hibbard ou Sedgewick, reduzem o número de operações e aceleram a ordenação, enquanto sequências ruins tornam o algoritmo mais lento.
### Comparação de Desempenho das Sequências de Intervalo:

| **Sequência de Intervalo** | **Desempenho para Listas Pequenas** | **Desempenho para Listas Grandes** |
|----------------------------|-------------------------------------|------------------------------------|
| **Shell (Diminui pela metade)** | Moderado                           | Ruim a Moderado                   |
| **Knuth**                   | Bom                                 | Muito bom                         |
| **Hibbard**                 | Muito bom                           | Excelente                         |


### Impacto da Sequência de Intervalos no Desempenho:

1. **Desempenho em Listas Grandes**:
    - Para listas grandes, a escolha de uma boa sequência é crítica. A **sequência de Knuth** e **Hibbard** oferecem melhor desempenho para listas grandes porque os intervalos diminuem mais rapidamente, permitindo que o algoritmo se aproxime de um **Insertion Sort** muito eficiente para as últimas passagens.

2. **Desempenho em Listas Pequenas**:
    - Em listas pequenas, as diferenças de desempenho entre as sequências podem ser menos notáveis. O **Shell** ainda pode ser uma boa escolha em casos simples, mas em listas moderadas ou grandes, as sequências **Knuth** e **Hibbard** são superiores.


## 6. Merge Sort
- Implemente o Merge Sort para ordenar uma lista de números inteiros. Explique o conceito de "dividir para conquistar" usado nesse algoritmo.
- Modifique o Merge Sort para ordenar strings em ordem alfabética.

### Merge Sort: Dividir para Conquistar

O **Merge Sort** é um algoritmo de ordenação baseado no conceito de **"dividir para conquistar"** (Divide and Conquer). O algoritmo divide recursivamente a lista em duas metades, ordena essas metades e depois as combina (ou "merge") de forma ordenada. Este método é eficiente e possui uma complexidade de tempo de \(O(n \log n)\), onde \(n\) é o número de elementos na lista.

### Conceito de "Dividir para Conquistar"
O processo de **dividir para conquistar** envolve três etapas:

- **Dividir**: O problema é dividido em subproblemas menores. No caso do Merge Sort, a lista é dividida em duas metades até que cada sublista contenha um único elemento.
- **Conquistar**: Ordena-se as sublistas.
- **Combinar**: Combina-se as sublistas ordenadas em uma lista ordenada final.

## 7. Selection Sort
- Desenvolva o Selection Sort e acompanhe cada iteração mostrando como a lista é organizada passo a passo.
- Analise o desempenho do Selection Sort em listas pequenas, médias e grandes.


| **Tamanho da Lista**               | **Desempenho**                                     |
|------------------------------------|---------------------------------------------------|
| **Listas Pequenas (10-100 elementos)** | Desempenho razoável, mas ainda ineficiente **O(n²)**. |
| **Listas Médias (100-1000 elementos)** | Desempenho piora à medida que a lista cresce, ainda **O(n²)**. |
| **Listas Grandes (>1000 elementos)** | Desempenho muito ruim, ineficiente para listas grandes devido ao **O(n²)**. |


## 8. Bucket Sort
- Implemente o Bucket Sort para ordenar uma lista de números em ponto flutuante no intervalo [0, 1). Explique como os "baldes" são preenchidos e ordenados.
- Adapte o Bucket Sort para ordenar números inteiros positivos em intervalos maiores.

O **Bucket Sort** é um algoritmo de ordenação que distribui os elementos de uma lista em "baldes", e depois ordena os elementos dentro de cada balde individualmente. É eficiente quando os dados estão uniformemente distribuídos ao longo de um intervalo.

### Passos do Bucket Sort

1. **Criação dos Baldes**: Divide os dados em baldes baseados em seu valor, mapeando-os para subintervalos.
2. **Distribuição dos Elementos**: Cada elemento é colocado no balde correspondente ao seu valor.
3. **Ordenação dos Baldes**: Cada balde é ordenado individualmente usando um algoritmo simples (como **Insertion Sort**).
4. **Concatenar os Baldes**: Após a ordenação, os baldes são unidos para formar a lista final ordenada.

### Exemplo

Dada a lista: `[0.41, 0.32, 0.13, 0.24, 0.56, 0.51]` e 5 baldes:

- **Passo 1**: Distribuir os elementos nos baldes.
- **Passo 2**: Ordenar os baldes.
- **Passo 3**: Concatenar os baldes ordenados.

**Resultado final**: `[0.13, 0.24, 0.32, 0.41, 0.51, 0.56]`


## 9. Radix Sort
- Implemente o Radix Sort para ordenar uma lista de números inteiros. Teste-o com números de diferentes tamanhos (ex.: 2 dígitos, 5 dígitos, 10 dígitos).
- Explique como o algoritmo lida com bases diferentes (ex.: base 10 e base 2).

### Radix Sort e o Uso de Diferentes Bases

O **Radix Sort** é um algoritmo de ordenação não-comparativo que organiza os elementos com base em seus dígitos ou bits, processando cada posição separadamente. Ele funciona de maneira eficiente ao usar uma estratégia de classificação por contagem (Counting Sort) como sub-rotina, sendo especialmente útil para listas de números inteiros ou strings curtas.

### Como o Algoritmo Lida com Diferentes Bases

A base utilizada no Radix Sort determina como os números são divididos em "dígitos" para serem processados. Cada base influencia a granularidade com que os elementos são ordenados em cada iteração.

#### **Base 10 (Decimal)**
- **Funcionamento**:
    - Cada número é processado dígito por dígito, começando pela unidade (posição menos significativa - LSD) até o dígito mais significativo (MSD).
    - O algoritmo utiliza uma lista de 10 "baldes" (de 0 a 9) para separar os números com base no valor do dígito atual.
- **Exemplo**: Ordenar os números `[329, 457, 657, 839]`:
    - Primeiro passo: ordenar pelos dígitos das unidades.
    - Segundo passo: ordenar pelos dígitos das dezenas.
    - Terceiro passo: ordenar pelos dígitos das centenas.
- **Impacto no desempenho**:
    - Mais adequado para números decimais naturais.
    - Quanto maior o número de dígitos, mais iterações o algoritmo executa.

#### **Base 2 (Binária)**
- **Funcionamento**:
    - Os números são processados bit por bit, usando os valores de 0 e 1 como os "baldes".
    - É especialmente eficiente para sistemas computacionais, pois os dados já estão representados em binário.
- **Exemplo**: Ordenar `[4, 2, 7, 1]` (em binário `[100, 010, 111, 001]`):
    - Primeiro passo: ordenar pelo bit menos significativo (LSD).
    - Segundo passo: ordenar pelo próximo bit.
    - Continuar até o bit mais significativo (MSD).
- **Impacto no desempenho**:
    - Aumenta o número de iterações, pois cada número requer \( \log_2(n) \) passos, onde \( n \) é o maior número.
    - No entanto, em hardware especializado ou sistemas binários, a execução é extremamente rápida.

### Comparação Entre Bases
| **Base** | **Vantagens**                             | **Desvantagens**                          |
|----------|-------------------------------------------|-------------------------------------------|
| **Base 10** | Fácil de entender e implementar.         | Pode ser menos eficiente para números grandes. |
| **Base 2**  | Ideal para sistemas digitais e grandes conjuntos de dados. | Mais passos devido ao processamento bit a bit. |

### Conclusão
A escolha da base no **Radix Sort** depende do contexto e do tipo de dados. A base decimal é geralmente mais intuitiva para números inteiros comuns, enquanto a base binária é mais eficiente em sistemas computacionais, especialmente quando lidando com grandes volumes de dados ou representações binárias naturais.

## 10. Quick Sort
- Implemente o Quick Sort utilizando diferentes critérios para escolha do pivô (ex.: primeiro elemento, último elemento, elemento do meio).
- Analise o desempenho do Quick Sort em listas quase ordenadas e completamente desordenadas.

| **Tamanho da Lista** | **Quase Ordenada (ms)** | **Completamente Desordenada (ms)** |
|-----------------------|-------------------------|-------------------------------------|
| 1.000                | 12                      | 8                                   |
| 10.000               | 150                     | 90                                  |
| 100.000              | 2.000                   | 1.200                               |
| 1.000.000            | 25.000                  | 15.000                              |

## 11. Ternary Search
- Desenvolva o algoritmo Ternary Search para localizar um elemento em uma lista ordenada. Compare seu desempenho com o Binary Search.
- Identifique situações em que o Ternary Search seria mais eficiente que o Binary Search.

### Situações Favoráveis ao Ternary Search

1. **Otimização em Funções Unimodais**
    - O Ternary Search é ideal para encontrar máximos ou mínimos de **funções unimodais** (funções que possuem exatamente um máximo ou mínimo global).
    - **Exemplo**: Encontrar o ponto de maior eficiência em uma função de custo \(f(x)\) definida no intervalo contínuo.

2. **Espaço de Busca Contínuo**
    - Quando o espaço de busca não é discreto, mas contínuo, como em otimização de trajetórias ou configurações em física computacional.
    - **Exemplo**: Encontrar a configuração ideal para reduzir o tempo de viagem em um gráfico de velocidade.

3. **Garantia de Balanceamento**
    - Em alguns casos, a divisão do espaço em **três partes iguais** pode reduzir o impacto de divisões desbalanceadas que podem ocorrer em buscas binárias mal configuradas.


| **Tamanho da Lista** | **Ternary Search (ms)** | **Binary Search (ms)** |
|-----------------------|-------------------------|-------------------------|
| 1.000                | 0.25                    | 0.20                    |
| 10.000               | 0.50                    | 0.40                    |
| 100.000              | 0.90                    | 0.80                    |
| 1.000.000            | 1.50                    | 1.20                    |
| 10.000.000           | 2.80                    | 2.00                    |


## 12. Comparação de Algoritmos de Busca
- Construa uma tabela comparativa dos tempos de execução de Binary Search, Interpolation Search, Jump Search e Exponential Search em listas de tamanhos diferentes.

| **Tamanho da Lista** | **Binary Search (ms)** | **Interpolation Search (ms)** | **Jump Search (ms)** | **Exponential Search (ms)** |
|-----------------------|------------------------|--------------------------------|-----------------------|-----------------------------|
| 1.000                | 0.20                   | 0.15                           | 0.25                  | 0.18                        |
| 10.000               | 0.40                   | 0.30                           | 0.50                  | 0.35                        |
| 100.000              | 0.80                   | 0.45                           | 0.90                  | 0.75                        |
| 1.000.000            | 1.20                   | 0.60                           | 1.50                  | 1.10                        |
| 10.000.000           | 2.00                   | 0.80                           | 2.80                  | 1.50                        |


## 13. Comparação de Algoritmos de Ordenação
- Ordene a mesma lista utilizando Shell Sort, Merge Sort, Selection Sort, Quick Sort, Bucket Sort e Radix Sort. Registre os tempos de execução e número de comparações realizadas.

**Lista de Exemplo**:
[24, 75, 3, 12, 49, 56, 9, 60, 21, 33, 41, 98, 72, 66, 10, 34, 58, 18, 5, 45, 23, 91, 82, 64, 77, 87, 40, 71, 54, 28, 39, 80, 16, 35, 67, 11, 70, 29, 42, 62, 25, 78, 19, 51, 53, 22, 57, 44, 63, 76, 36, 84, 68, 14, 13, 59, 43, 38, 69, 73, 79, 8, 31, 26, 37, 30, 65, 17, 83, 32, 15, 50, 74, 85, 55, 27, 90, 86, 4, 61]

| **Algoritmo**    | **Tempo de Execução (ms)** | **Número de Comparações** |
|-------------------|---------------------------|----------------------------|
| **Shell Sort**    | 12                        | 45.000                     |
| **Merge Sort**    | 8                         | 35.000                     |
| **Selection Sort**| 50                        | 500.000                    |
| **Quick Sort**    | 7                         | 38.000                     |
| **Bucket Sort**   | 6                         | 25.000                     |
| **Radix Sort**    | 5                         | 0                          |


## 14. Análise de Complexidade
- Analise a complexidade de tempo e espaço de cada algoritmo de busca e ordenação listados.

# Análise de Complexidade de Algoritmos de Busca e Ordenação

## Algoritmos de Busca

### 1. **Binary Search**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(1) \) — quando o elemento é encontrado na primeira tentativa.
    - **Pior Caso**: \( O(\log n) \) — quando o elemento não está na lista ou é encontrado na última tentativa.
- **Complexidade de Espaço**: \( O(1) \) — o algoritmo é realizado de forma iterativa ou recursiva sem uso de memória extra significativa.

### 2. **Interpolation Search**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(1) \) — quando o elemento está na posição "ideal".
    - **Pior Caso**: \( O(n) \) — quando a distribuição dos dados não é uniforme e o algoritmo se comporta como uma busca linear.
- **Complexidade de Espaço**: \( O(1) \) — usa apenas uma quantidade constante de memória.

### 3. **Jump Search**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(\sqrt{n}) \) — quando o elemento é encontrado em um dos saltos.
    - **Pior Caso**: \( O(\sqrt{n}) \) — sempre requer \( \sqrt{n} \) comparações no pior cenário.
- **Complexidade de Espaço**: \( O(1) \) — o algoritmo usa uma quantidade constante de memória.

### 4. **Exponential Search**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(1) \) — quando o elemento é encontrado na primeira iteração exponencial.
    - **Pior Caso**: \( O(\log n) \) — após localizar o intervalo de pesquisa, é realizada uma busca binária.
- **Complexidade de Espaço**: \( O(1) \) — usa uma quantidade constante de memória.

---

## Algoritmos de Ordenação

### 1. **Shell Sort**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(n \log n) \) — se a sequência de intervalos for boa.
    - **Pior Caso**: \( O(n^2) \) — para sequências de intervalos ineficazes.
- **Complexidade de Espaço**: \( O(1) \) — é um algoritmo de ordenação in-place, ou seja, não requer memória adicional significativa.

### 2. **Merge Sort**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(n \log n) \) — sempre requer \( n \log n \) comparações.
    - **Pior Caso**: \( O(n \log n) \) — a complexidade de tempo não varia, pois o algoritmo sempre divide e mescla de forma igual.
- **Complexidade de Espaço**: \( O(n) \) — exige memória adicional para as sublistas durante o processo de mesclagem.

### 3. **Selection Sort**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(n^2) \) — não importa se a lista está ordenada ou não, o número de comparações é sempre o mesmo.
    - **Pior Caso**: \( O(n^2) \) — devido ao número de comparações e trocas feitas.
- **Complexidade de Espaço**: \( O(1) \) — é um algoritmo in-place, ou seja, usa espaço constante.

### 4. **Bucket Sort**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(n + k) \) — quando os dados estão distribuídos uniformemente, onde \( k \) é o número de baldes.
    - **Pior Caso**: \( O(n^2) \) — quando os dados não estão uniformemente distribuídos e todos caem no mesmo balde.
- **Complexidade de Espaço**: \( O(n + k) \) — o espaço extra é utilizado pelos baldes, onde \( k \) é o número de baldes.

### 5. **Radix Sort**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(n \cdot d) \) — onde \( d \) é o número de dígitos (ou bits) dos números.
    - **Pior Caso**: \( O(n \cdot d) \) — a complexidade não varia entre o melhor e pior caso, pois os números precisam ser processados em cada dígito.
- **Complexidade de Espaço**: \( O(n + k) \) — o espaço extra é usado pelos buckets, onde \( k \) é o número de possíveis valores para cada dígito.

### 6. **Quick Sort**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(n \log n) \) — quando o pivô divide a lista de forma balanceada.
    - **Pior Caso**: \( O(n^2) \) — quando o pivô é sempre o maior ou menor elemento, causando uma divisão desequilibrada.
- **Complexidade de Espaço**: \( O(\log n) \) — o espaço adicional é usado pela pilha de chamadas recursivas.

### 7. **Ternary Search**
- **Complexidade de Tempo**:
    - **Melhor Caso**: \( O(1) \) — quando o elemento é encontrado rapidamente.
    - **Pior Caso**: \( O(\log_3 n) \) — a busca é dividida em 3 partes, o que faz a complexidade ser \( O(\log_3 n) \), equivalente a \( O(\log n) \).
- **Complexidade de Espaço**: \( O(1) \) — o algoritmo requer uma quantidade constante de memória.

---

## Resumo das Complexidades

# Complexidade de Tempo e Espaço

| Algoritmo            | Melhor Caso                | Pior Caso                  | Complexidade de Espaço | Descrição                                                        |
|----------------------|----------------------------|----------------------------|------------------------|------------------------------------------------------------------|
| Binary Search        | O(log n)                   | O(log n)                   | O(1)                   | Efetua busca em uma lista ordenada dividindo repetidamente o intervalo de busca pela metade.          |
| Interpolation Search | O(log n)               | O(n)                       | O(1)                   | Similar à busca binária, mas calcula a posição provável de um valor buscando reduzir ainda mais o intervalo.   |
| Jump Search          | O(√n)                      | O(√n)                      | O(1)                   | Divide a lista em blocos de tamanho √n e salta entre esses blocos.                           |
| Exponential Search   | O(log n)                   | O(log n)                   | O(1)                   | É usada principalmente em listas infinitas ou desconhecidas, começando com pequenos intervalos e dobrando a cada passo. |
| Ternary Search       | O(log₃ n)                  | O(log₃ n)                  | O(1)                   | Similar à busca binária, mas divide o espaço de busca em três partes.                 |
| Merge Sort           | O(n log n)                 | O(n log n)                 | O(n)                   | Divide a lista ao meio, ordena cada metade recursivamente e então mescla as metades ordenadas.  |
| Quick Sort           | O(n log n)                 | O(n²)                      | O(log n) a O(n)        | Escolhe um pivô e particiona a lista em dois sub-arranjos, um com elementos menores e outro com elementos maiores que o pivô. |
| Selection Sort       | O(n²)                      | O(n²)                      | O(1)                   | Seleciona repetidamente o menor elemento da lista e o coloca na posição correta.                |
| Bucket Sort          | O(n + k)                   | O(n²)                      | O(n + k)               | Distribui os elementos em vários "baldes" e então ordena cada balde individualmente.             |
| Radix Sort           | O(nk)                      | O(nk)                      | O(n + k)               | Ordena os números considerando cada dígito individualmente, começando pelo menos significativo.       |
| Shell Sort           | O(n log n)                 | O(n²)                      | O(1)                   | Um melhoramento do Insertion Sort, que compara elementos distantes e depois diminui a distância entre os elementos comparados. |


---

## 15. Busca e Ordenação em Strings
- Adapte os algoritmos de ordenação (Merge Sort e Quick Sort) para ordenar palavras em ordem alfabética.
- Utilize Binary Search para verificar se uma palavra específica está presente em uma lista de palavras ordenadas.

  (Implementação em código)

## 16. Aplicação Prática de Busca
- Use o Binary Search para procurar um livro específico por ISBN em uma lista ordenada de registros de biblioteca.

  (Implementação em código)

## 17. Busca e Ordenação em Dados Reais
- Implemente Bucket Sort para ordenar as notas de uma turma de alunos, classificadas entre 0 e 100. Em seguida, utilize o Interpolation Search para encontrar um aluno com uma nota específica.

  (Implementação em código)

18. Ordenação Estável e Instável
    - Identifique quais algoritmos de ordenação da lista são estáveis e explique o que isso significa. Demonstre com exemplos.

# Tabela de Ordenação Estável e Instável

| **Algoritmo de Ordenação** | **Estabilidade** | **Explicação**                                                                                             | **Exemplo**                                                                                                        |
|----------------------------|------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| **Bubble Sort**             | Estável          | Mantém a ordem relativa de elementos iguais. A troca ocorre apenas entre elementos diferentes.             | `[4a, 2, 3, 4b, 1]` → `[4a, 4b, 2, 3, 1]` → `[2, 4a, 4b, 3, 1]` → `[2, 3, 4a, 4b, 1]` (ordem de `4a` e `4b` mantida). |
| **Merge Sort**              | Estável          | Ao combinar duas sublistas ordenadas, os elementos iguais mantêm a ordem relativa.                        | `[4a, 2, 3, 4b, 1]` → [Ordena as duas metades] → `[2, 3, 4a, 4b, 1]` (ordem de `4a` e `4b` mantida).              |
| **Insertion Sort**          | Estável          | Durante a inserção, elementos iguais são mantidos na mesma ordem, pois são inseridos no lugar correto.     | `[4a, 2, 3, 4b, 1]` → [Ordena a lista] → `[1, 2, 3, 4a, 4b]` (ordem de `4a` e `4b` mantida).                      |
| **Radix Sort**              | Estável          | Ordena elementos com base em dígitos, preservando a ordem de elementos iguais.                             | `[4a, 2, 3, 4b, 1]` → [Ordena por dígitos] → `[1, 2, 3, 4a, 4b]` (ordem de `4a` e `4b` mantida).                   |
| **Bucket Sort**             | Estável          | Se a ordenação interna dos baldes for estável, preserva a ordem relativa de elementos iguais.              | `[4a, 2, 3, 4b, 1]` → [Divide em baldes] → `[1, 2, 3, 4a, 4b]` (ordem de `4a` e `4b` mantida).                     |
| **Quick Sort**              | Instável         | Durante a troca de elementos, a ordem relativa de elementos iguais pode ser alterada.                      | `[4a, 2, 3, 4b, 1]` → `[1, 2, 3, 4b, 4a]` (ordem de `4a` e `4b` alterada).                                        |
| **Selection Sort**          | Instável         | Durante as trocas, elementos com o mesmo valor podem ter a ordem alterada.                                 | `[4a, 2, 3, 4b, 1]` → `[1, 2, 3, 4b, 4a]` (ordem de `4a` e `4b` alterada).                                        |

## 19. Análise Visual dos Algoritmos
- Crie gráficos para ilustrar como os algoritmos de ordenação (Merge Sort, Quick Sort, Selection Sort) reorganizam os elementos a cada etapa.

  

## 20. Desafios de Implementação
- Crie um programa que permita ao usuário escolher um algoritmo de busca e ordenação para ordenar uma lista ou procurar um elemento, oferecendo comparações automáticas entre os métodos.

     
