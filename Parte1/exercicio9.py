from dicionario import dic

# #9 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("ex9b", "pudim" in dic["sobremesas"]["doces"])
#KeyError: 'sobremesas', pois o dicionario dic só tem as chaves "alimentos" e "linguagens"