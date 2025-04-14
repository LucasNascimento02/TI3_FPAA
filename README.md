# Projeto Caminho Hamiltoniano

O **Caminho Hamiltoniano** é um projeto desenvolvido para encontrar um caminho hamiltoniano em um grafo orientado ou não orientado. Um caminho hamiltoniano é um caminho que visita cada vértice do grafo exatamente uma vez, sendo um problema fundamental em teoria dos grafos com aplicações em diversas áreas.

## O que é um Caminho Hamiltoniano?

Um **Caminho Hamiltoniano** é um conceito em teoria dos grafos que representa um caminho em um grafo que visita cada vértice exatamente uma vez. Este problema está intimamente relacionado com o Problema do Caixeiro Viajante (PCV), sendo uma versão simplificada do mesmo, onde não é necessário retornar ao vértice inicial.

### Características principais:
- Deve visitar cada vértice exatamente uma vez
- Pode ser aplicado em grafos direcionados ou não direcionados
- É um problema NP-Completo
- Tem aplicações práticas em logística, planejamento de rotas e design de circuitos

## Complexidade Computacional

### Classes de Complexidade

O problema do Caminho Hamiltoniano pertence às seguintes classes de complexidade:

1. **NP (Tempo Polinomial Não-determinístico)**:
   - O problema está em NP pois uma solução pode ser verificada em tempo polinomial
   - Dado um caminho, podemos verificar se ele é hamiltoniano checando se:
     - Todos os vértices são visitados exatamente uma vez
     - As arestas entre vértices consecutivos existem no grafo
     - A verificação é feita em O(n), onde n é o número de vértices

2. **NP-Completo**:
   - O problema é NP-Completo pois:
     - Está em NP (como demonstrado acima)
     - É redutível ao Problema do Caixeiro Viajante em tempo polinomial
     - Qualquer problema em NP pode ser reduzido ao problema do Caminho Hamiltoniano em tempo polinomial

3. **NP-Difícil**:
   - Por ser NP-Completo, é também NP-Difícil
   - Não existe algoritmo conhecido que resolva o problema em tempo polinomial
   - A melhor solução conhecida tem complexidade exponencial

### Análise da Complexidade Assintótica

#### Complexidade Temporal

O algoritmo implementado utiliza uma abordagem de backtracking e possui complexidade temporal de:
- **O(n!)** no pior caso
- Onde n é o número de vértices no grafo

Justificativa da análise:
1. Para o primeiro vértice, temos n escolhas
2. Para o segundo vértice, temos (n-1) escolhas
3. Para o terceiro vértice, temos (n-2) escolhas
4. E assim por diante...
5. Multiplicando todas as escolhas: n * (n-1) * (n-2) * ... * 1 = n!

#### Aplicação do Teorema Mestre

O Teorema Mestre não é aplicável a este algoritmo pelos seguintes motivos:
1. O algoritmo não segue o formato padrão de divisão e conquista T(n) = aT(n/b) + f(n)
2. A recursão não divide o problema em subproblemas de tamanho igual
3. O algoritmo utiliza backtracking com número variável de chamadas recursivas

#### Análise dos Casos de Complexidade

1. **Melhor Caso - O(n)**:
   - Ocorre quando o primeiro caminho tentado é um caminho hamiltoniano válido
   - Exemplo: Em um grafo completo, seguindo os vértices em ordem

2. **Caso Médio - O(n!)**:
   - Na prática, a complexidade média se aproxima do pior caso
   - Depende da estrutura do grafo e da distribuição das arestas

3. **Pior Caso - O(n!)**:
   - Ocorre quando é necessário explorar todas as permutações possíveis
   - Exemplo: Quando não existe caminho hamiltoniano ou ele é o último a ser encontrado

## Dependências

Para rodar este projeto, você precisará das seguintes bibliotecas:

```bash
pip install networkx matplotlib
```

## Ambiente Virtual

### Passo 1: Criar e ativar o ambiente virtual

1. Crie um ambiente virtual:
```bash
python3 -m venv .venv
```

2. Ative o ambiente virtual:
   - No macOS e Linux:
     ```bash
     source .venv/bin/activate
     ```
   - No Windows:
     ```bash
     .venv\Scripts\activate
     ```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Passo 2: Executar o programa

Após ativar o ambiente virtual, execute o programa principal:

```bash
python main.py
```

## Versão do Python

Este projeto foi desenvolvido na versão **3.13.0** do Python.

## Explicação do Código

### Arquivo: main.py

#### Classe `Graph`
- **Objetivo:** Representa um grafo e implementa o algoritmo de busca do Caminho Hamiltoniano
- **Atributos:**
  - `V`: Número de vértices
  - `graph`: Matriz de adjacência do grafo
- **Métodos principais:**

##### `__init__(self, vertices)`
- Inicializa o grafo com o número de vértices especificado
- Cria uma matriz de adjacência vazia

##### `add_edge(self, v1, v2)`
- Adiciona uma aresta entre os vértices v1 e v2
- Para grafos não direcionados, adiciona em ambas as direções

##### `hamiltonian_path_util(self, path, pos, visited)`
- Função auxiliar recursiva que implementa o backtracking
- **Parâmetros:**
  - `path`: Lista que armazena o caminho atual
  - `pos`: Posição atual no caminho
  - `visited`: Conjunto de vértices já visitados
- **Retorno:**
  - `True` se um caminho for encontrado
  - `False` caso contrário

##### `find_hamiltonian_path(self)`
- Função principal que inicia a busca por um caminho hamiltoniano
- Inicializa as estruturas necessárias e chama a função auxiliar
- Retorna o caminho encontrado ou None se não existir
