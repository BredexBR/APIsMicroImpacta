from dicionario import dic

# #5. O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r5", dic["linguagens"]["javascript"]["criacao"])
# TypeError: list indices must be integers or slices, not str
# O erro ocorre porque dic["linguagens"] é uma lista
# O acesso correto seria dic["linguagens"][0] em vez de dic["linguagens"]["javascript"]
