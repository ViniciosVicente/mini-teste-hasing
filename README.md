# Índice Invertido em Python

<p><strong>Dupla:</strong> Marcos Vinicios Vicente dos Santos e João Pedro Santos Vieira</p>

## Sobre o projeto

Este projeto implementa um **índice invertido para busca textual**, utilizando estruturas de dados da linguagem Python, como dicionários (`dict`) e conjuntos (`set`).

O objetivo é permitir a localização de palavras em um texto, identificando as linhas em que aparecem e realizando consultas com operadores de interseção e união.

## Estrutura do projeto

```text
mini-teste/
│
├── __pycache__/
│
├── indice_invertido.py
├── README.md
├── teste.py
└── treino.py
```

### Organização dos arquivos

| Arquivo | Descrição |
|---|---|
| `indice_invertido.py` | Contém a implementação das funções principais do índice invertido. |
| `teste.py` | Arquivo destinado à execução de testes para verificar o funcionamento das funções implementadas. |
| `treino.py` | Ambiente de prática utilizado para exercícios, experimentações e aprendizado dos conceitos de Python aplicados à atividade. |
| `README.md` | Documentação e apresentação do projeto. |

## Funcionalidades implementadas

### Construção do índice

**Função:** `construir_indice(texto)`

Constrói um dicionário que associa cada palavra às linhas em que aparece.

- Numeração das linhas iniciada em 1.
- Conversão das palavras para letras minúsculas.
- Remoção de pontuação nas extremidades das palavras.
- Utilização de conjuntos para evitar duplicações.
- Preservação dos acentos.

### Busca por palavra

**Função:** `buscar(indice, palavra)`

Localiza uma palavra no índice e retorna uma lista ordenada com os números das linhas correspondentes.

### Busca com operador E

**Função:** `buscar_e(indice, palavras)`

Retorna as linhas que possuem todas as palavras pesquisadas, utilizando a operação de interseção (`&`) entre conjuntos.

### Busca com operador OU

**Função:** `buscar_ou(indice, palavras)`

Retorna as linhas que possuem pelo menos uma das palavras pesquisadas, utilizando a operação de união (`|`) entre conjuntos.

## Tecnologias e recursos utilizados

- **Python 3**
- Biblioteca padrão `string`
- Dicionários (`dict`)
- Conjuntos (`set`)
- Listas (`list`)

## Como executar

### 1. Pré-requisitos

Ter o Python 3 instalado na máquina.

### 2. Executar os testes

No terminal, dentro da pasta do projeto, execute:

```bash
python teste.py
```

### 3. Executar os exercícios de prática

Para executar o ambiente de treinamento:

```bash
python treino.py
```

### 4. Executar o experimento 'Tempo de Busca'

No terminal, dentro da pasta do projeto, execute:

```bash
py experimento_tempo_de_busca.py
```

### 5. Executar o experimento 'Vantagem de Indexação'

No terminal, dentro da pasta do projeto, execute:

```bash
py experimento_vantagem_de_indexacao.py
```

Altere o valor de 'k' em 'consultas = random.choices(palavras, k=1000)' para alternar entre os valores de consultas. Ex: k = 1 -> 1 Consulta | k = 10 -> 10 Consultas...

## Objetivo de aprendizagem

Além da implementação das funcionalidades, o projeto também foi utilizado para praticar conceitos fundamentais de Python, manipulação de textos e estruturas de dados.

A separação entre implementação, testes e exercícios permite validar o código sem misturar a solução principal com experimentações de aprendizado.

## Escopo

Esta documentação contempla a organização dos arquivos e as funcionalidades de construção e consulta do índice invertido. Outras etapas da atividade, como busca sequencial, experimentos de desempenho e análise comparativa, serão documentadas separadamente.
