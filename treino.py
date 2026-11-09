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