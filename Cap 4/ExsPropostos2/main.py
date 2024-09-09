import numpy as np

# EX 1
np.random.seed(5)
array_floats = np.random.uniform(-1, 1, 10)
array_mult = array_floats * 100
array_integers = np.floor(array_mult).astype(int)

# EX 2
np.random.seed(10)
matrix = np.random.randint(1, 51, (4, 4))

# EX 3
media_linhas = np.mean(matrix, axis=1)
media_colunas = np.mean(matrix, axis=0)
maior_media_linhas = np.max(media_linhas)
maior_media_colunas = np.max(media_colunas)

# EX 4
unique, counts = np.unique(matrix, return_counts=True)
aparicoes = dict(zip(unique, counts))
numeros_2x = [num for num, count in aparicoes.items() if count == 2]

print("EX 1. Array floats original:", array_floats)
print("   Array multiplicado e parte inteira:", array_integers)
print("\nEX 2. Matriz 4x4 aleatória:\n", matrix)
print("\nEX 3. Médias das linhas:", media_linhas)
print("   Médias das colunas:", media_colunas)
print("   Maior média das linhas:", maior_media_linhas)
print("   Maior média das colunas:", maior_media_colunas)
print("\nEX 4. Números que aparecem 2 vezes na matriz:", numeros_2x)