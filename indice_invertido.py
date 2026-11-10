def construir_indice(texto):
# Recebe um texto com várias linhas.
# Retorna um dicionário: palavra -> conjunto de linhas.
    infor = {}
    linhas = texto.splitlines();
    for numero, linhas_textos in enumerate(linhas, start = 1):
        
        splin_palavra = linhas_textos.split();
        for palavra in splin_palavra:
        
            if palavra not in infor:
                infor[palavra] = set();
            infor[palavra].add(numero);

    print(infor);
    return infor


def buscar(indice, palavra):
# Retorna uma lista ordenada com as linhas da palavra.
    
    pass

def buscar_e(indice, palavras):
# Retorna as linhas que contêm TODAS as palavras.
    
    pass

def buscar_ou(indice, palavras):

    pass

