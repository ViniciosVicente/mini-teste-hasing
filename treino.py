# Treino de dicionários

estoque = {
    "arroz": 10,
    "feijao": 5,
    "macarrao": 8
}
# Como você faria para consultar a quantidade de arroz?
# print(estoque.get("arroz"));

# Como adicionaria "cafe" com quantidade 15?
# estoque["cafe"] = 15;
# print(estoque);

# Como verificaria se "leite" existe no dicionário?
# if "leite" in estoque:
#    print("Existe");
# else: 
#    print("não existe");

# Se você executar estoque["arroz"] = 20, o que acontece?
# R- A chave Arroz será atualiazada para o valor 20, pois arroz já existe no dicionário;

# --------------------

alunos = {
    "Marcos": 8,
    "Ana": 9,
    "Pedro": 7
}

# Atualize a nota de Pedro para 10.
# alunos["Pedro"] = 10;

# Adicione João com nota 6.
# alunos["Joao"] = 6;


# Verifique se Maria está cadastrada.
# if "Maria" in alunos:
#    print("Cadastrada");

# Percorra o dicionário e mostre o nome e a nota de cada aluno.

# for nome, nota in alunos.items(): print(nome, nota);

# ----------

# Aula 2 — Conjuntos em Python (set)

numeros = {10, 20, 30, 40}

# Adicione o número 50.
numeros.add(50);


# Adicione novamente o número 20. O que acontece?
# numeros.add(20);
# print(numeros); Não acontece nada! Como já existe o 20, ele não duplica


# Remova o número 30.
# numeros.remove(30);
# print(numeros)


# Tente remover o número 100 usando discard().
# numeros.discard(100);
# print(numeros);

# Mostre o conjunto completo com print().
# print(numeros);

# Aula 2 — Parte 2: União e interseção
javascript = {1, 2, 3, 7}
python = {2, 3, 4, 5}
java = {5, 6, 7}

# Qual será o resultado de javascript | python?

# resultado = javascript | python;
# print(resultado) Será {1,2,3,4,5,7}

# Qual será o resultado de javascript & python?
# resultado = javascript & python;
# print(resultado); será {2,3}

# Qual será o resultado de python | java?
# resultado = java | python; print(resultado);  SERÁ {2, 3, 4, 5, 6, 7}

# Qual será o resultado de javascript & java?
# resultado = java & javascript; print(resultado); será {7}

# Exercícios de splint e splintlines

texto = """Eu estudo Python.
Python é interessante.
Eu gosto de programação."""

# 1. Utilize .splitlines() para separar as linhas.
linhas = texto.splitlines();

# 2. Mostre as linhas utilizando print().
print(linhas);

# 3. Utilize um for para percorrer cada linha.
for percorre in linhas:
# 4. Dentro do for, utilize .split() para separar as palavras.
    separar = percorre.split();
    print(separar);
# 5. Mostre cada palavra individualmente.
    for palavra in percorre:
        print(palavra);