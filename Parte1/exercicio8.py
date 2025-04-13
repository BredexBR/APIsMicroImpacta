from dicionario import dic

# #8 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r8", 1996 in dic['linguagens'][0])
#False, pois 1996 não é uma **chave** do dicionário dic['linguagens'][0]
#Alias, dic['linguagens'][0] é  {"nome": "javascript", "criacao": 1996, 
#        "paradigma": ["eventos","funcional"]}