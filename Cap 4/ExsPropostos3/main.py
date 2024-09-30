import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')
arr_aux = arr[1:]
arr_aux2 = arr[1:, 0]

#Ex 1
Num = len(np.unique(arr[1:, 0]))
success_count = np.sum(arr_aux == 'Success')
print((success_count / (Num - 1)) * 100)

#Ex 2
custo = arr_aux[:, 6].astype(float)

media_custo = np.mean(custo)

print(media_custo)

#Ex 3
usa_count = np.sum(np.char.count(arr_aux, 'USA'))
print(usa_count)

#Ex 4
space_rows = arr[arr[:, 1] == 'SpaceX']
max_cost = np.max(space_rows[:, 6].astype(float))
print(max_cost)

#Ex 5
empresas = arr[:, 1]

empresas_unique, counts = np.unique(empresas, return_counts=True)

for empresa, quantidade in zip(empresas_unique, counts):
    print(f"{empresa}: {quantidade} missões")
