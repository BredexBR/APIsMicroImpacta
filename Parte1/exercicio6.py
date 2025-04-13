from dicionario import dic

# #6 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r6", dic["linguagens"][2] == "haskell")
# False
# dic["linguagens"][2] é o dicionário         {"nome": "haskell", "criacao": 1990, "paradigma": ["funcional"]}
# Esse dicionário não é a mesma coisa que a string "haskell"
