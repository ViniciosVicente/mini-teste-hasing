import time
import random

def varredura(texto, palavras):
    resultados = []

    if not palavras:
        return resultados

    for palavra in palavras:
     if palavra.lower() in texto.lower():
        resultados.append(palavra)

    return resultados