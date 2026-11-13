from varredura_completa import *
from indice_invertido import *

with open("texto.txt", "r", encoding="utf-8") as arquivo:
    texto = arquivo.read()

palavras = texto.split()
consultas = random.choices(palavras, k=1000)

#Varredura

inicio = time.perf_counter()

fim = time.perf_counter()
tempo_varredura = (fim - inicio) * 1000

#--------------------

#Construção do índice

inicio = time.perf_counter()

indice = construir_indice(texto)

fim = time.perf_counter()
tempo_construcao = (fim - inicio) * 1000

#----------------------

#Busca com índice
inicio = time.perf_counter()

for palavra in consultas:
    buscar(indice, palavra)

fim = time.perf_counter()
tempo_indice = (fim - inicio) * 1000

#------------------------

print(f"Tempo de construção do indice: {tempo_construcao:.2f} ms")
print(f"Tempo de busca com indice: {tempo_indice:.2f} ms")
print(f"Tempo de busca por varredura: {tempo_varredura:.2f} ms")

