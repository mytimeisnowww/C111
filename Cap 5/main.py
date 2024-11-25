import pandas as pd

# Carregar o dataset
df = pd.read_csv('paises.csv', delimiter=';')

# 1. Mostrar países da OCEANIA e quantos são
# a) Quais são os países da OCEANIA
paises_oceania = df[df['Region'].str.contains('OCEANIA', case=False, na=False)]
print("Países da OCEANIA:")
print(paises_oceania['Country'])

# b) Quantos países são da OCEANIA
quantidade_oceania = paises_oceania.shape[0]
print(f"\nQuantidade de países da OCEANIA: {quantidade_oceania}")

# 2. Média da taxa de alfabetização (Literacy (%))
media_alfabetizacao = df['Literacy (%)'].mean()
print(f"\nMédia da taxa de alfabetização (Literacy (%)) do planeta: {media_alfabetizacao:.2f}")

# 3. Nome e região do país com maior população
pais_maior_populacao = df[df['Population'] == df['Population'].max()]
nome_pais_maior_populacao = pais_maior_populacao['Country'].values[0]
regiao_pais_maior_populacao = pais_maior_populacao['Region'].values[0]
print(f"\nPaís com maior população: {nome_pais_maior_populacao}")
print(f"Região do país com maior população: {regiao_pais_maior_populacao}")

# 4. Países que não possuem costa marítima e salvá-los em noCoast.csv
paises_sem_costa = df[df['Coastline (coast/area ratio)'] == 0]
paises_sem_costa.to_csv('noCoast.csv', index=False)
print("\nArquivo noCoast.csv com países que não possuem costa marítima foi salvo.")