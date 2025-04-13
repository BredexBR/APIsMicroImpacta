from dicionario import dic

#10 Escreva uma função "mais velha" que 
# recebe um dicionário como dic e 
# retorna (isso é diferente de imprimir!) a linguagem de programação mais velha da nossa lista
def mais_velha(dic):
    lista_linguagens = dic['linguagens']
    ling_velha = lista_linguagens[0]
    for linguagem in lista_linguagens:
        if linguagem['criacao'] < ling_velha['criacao']:
            ling_velha = linguagem
    return ling_velha