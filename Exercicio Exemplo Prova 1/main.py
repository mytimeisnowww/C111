import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

slice_data = arr[:, [0, 1, 2, 3]]
print(slice_data)

regioes = arr[1:, 1]
regioes_unique, contagens = np.unique(regioes, return_counts=True)
print(f"Regioes unicas: {len(regioes_unique)}")
print("Regiões e suas contagens:")
for regiao, contagem in zip(regioes_unique, contagens):
    print(f"{regiao}: {contagem}")

taxa = arr[1:, 9].astype(float)
media_literacy = np.mean(taxa)
print(f"Taxa media de alfabetização: {media_literacy}")

regioes = arr[1:, 1]
regioes_count = np.sum(np.char.count(regioes, "NORTHERN AMERICA"))
print(f"Numero de paisés na america do norte: {regioes_count}")


paises = arr[1:, 0]
regioes = arr[1:, 1]
gdp_per_capita = arr[1:, 8].astype(float)
filtro_regiao = np.char.equal(regioes, 'LATIN AMER. & CARIB')
paises_latam = paises[filtro_regiao]
gdp_latam = gdp_per_capita[filtro_regiao]
indice_max_gdp = np.argmax(gdp_latam)
pais_com_maior_gdp = paises_latam[indice_max_gdp]
print(f"O país da América do Sul e Caribe com a maior renda per capita é: {pais_com_maior_gdp}")
