from indice_invertido import *
texto = (
"Python e dados\n"
"Dados e algoritmos\n"
"Python e algoritmos"
)
indice = construir_indice(texto)
print(indice);

busca = buscar(indice, "java");
print(busca);