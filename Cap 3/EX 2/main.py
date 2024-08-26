# Conjuntos de smartphones disponíveis em cada loja
loja1 = {"iPhone 14", "Samsung Galaxy S23", "Xiaomi Mi 13", "iPhone 15 pro max", "Sansumg Galazy A54"}
loja2 = {"iPhone 14", "Samsung Galaxy S22", "Xiaomi Mi 13", "iPhone 15 pro max", "Motorola Razr 50 Ultra"}

# Modelos disponíveis no total
todos_modelos = loja1.union(loja2)
print("Todos os modelos disponiveis:", todos_modelos)

# Modelos disponíveis em ambas as lojas
modelos_em_comum = loja1.intersection(loja2)
print("Modelos disponíveis em ambas as lojas:", modelos_em_comum)
