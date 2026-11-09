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
if "Maria" in alunos:
    print("Cadastrada");

# Percorra o dicionário e mostre o nome e a nota de cada aluno.

for nome, nota in alunos.items(): print(nome, nota);