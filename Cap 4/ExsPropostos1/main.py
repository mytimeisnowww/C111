import numpy as np

# Ex1:
arr = np.linspace(0,1,21)
print(arr)

# Ex2:
arr1 = np.arange(0,51,2)
arr2 = np.arange(100,50,-2)
arr3 = np.concatenate((arr1,arr2))
print(arr3)

# Ex3:
arr4 = np.flip(np.sort(arr3))
print(arr4)

# Ex4:
arr5 = np.ones((3,4))
print(arr5)
arr6 = arr5.flatten()
print(arr6)

# Ex5:

matriz = np.random.randint(1, 10, size=(3, 4))
num_linhas = matriz.shape[0]
num_colunas = matriz.shape[1]

produto_linhas_colunas = num_linhas * num_colunas

print("Número de linhas:", num_linhas)
print("Número de colunas:", num_colunas)
print("Produto das linhas e colunas:", produto_linhas_colunas)
if produto_linhas_colunas % 2 == 0:
    print("O vetor resultante pode ter um número par de elementos.")
else:
    print("O vetor resultante pode ter um número ímpar de elementos.")