from indice_invertido import *
texto = (
"Python e dados\n"
"Dados e algoritmos\n"
"Python e algoritmos"
)
indice = construir_indice(texto)

busca = buscar(indice, "algoritmos");
print(busca);

busca_e = buscar_e(indice, ["python", "dados"])
print(busca_e)
busca_ou = buscar_ou(indice, ["python", "dados"]);
print(busca_ou);