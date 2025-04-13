from dicionario import dic

#11 Escreva uma função que retorna uma lista (sem repetições) de paradigmas de linguagens de programação
def todos_paradigmas(dic):
    lista_linguagens = dic['linguagens']
    paradigmas = []
    for linguagem in lista_linguagens:
        paradigmas_da_linguagem = linguagem['paradigma']
        for p in paradigmas_da_linguagem:
            if p not in paradigmas:
                paradigmas.append(p)
    return paradigmas 

print(todos_paradigmas(dic))