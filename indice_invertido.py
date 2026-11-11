import string

def construir_indice(texto):

    infor = {}
    linhas = texto.splitlines();
    for numero, linhas_textos in enumerate(linhas, start = 1):
        
        splin_palavra = linhas_textos.split();
        
        for palavra in splin_palavra:
            palavra = palavra.lower();
            palavra = palavra.strip(string.punctuation);

            if not palavra:
                continue
            
            if palavra not in infor:
                infor[palavra] = set();
            infor[palavra].add(numero);

    return infor

def buscar(indice, palavra):
    palavra = palavra.lower();
    palavra = palavra.strip(string.punctuation);

    if palavra not in indice:
        return [];

    resultado = sorted(indice[palavra]);

    return resultado

def buscar_e(indice, palavras):
# Retorna as linhas que contêm TODAS as palavras.
    
    pass

def buscar_ou(indice, palavras):

    pass

