from dicionario import dic

# #7 O que o seguinte acesso imprime? Se ele dá erro, qual o erro? Se dá erro, como corrigir?
print("r7", dic["alimentos"]["pizzas"][2] == "mussarella")
# False
# dic["alimentos"]["pizzas"] é a lista ["margueritta", "mussarella",                    "frango com catupiry", "portuguesa"]
# A sua posição 0 é "margueritta"
# A sua posição 1 é "mussarella"
# A sua posição 2 é "frango com catupiry"