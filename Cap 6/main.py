import pandas as pd
import matplotlib.pyplot as plt

space_df = pd.read_csv('space.csv', sep=';', encoding='utf-8')
paises_df = pd.read_csv('paises.csv', sep=';', encoding='utf-8')

# Exercício 1
usa_companys = space_df[space_df['Location'].str.contains('USA')]['Company Name'].unique()
china_companys = space_df[space_df['Location'].str.contains('China')]['Company Name'].unique()
num_usa = len(usa_companys)
num_china = len(china_companys)
country = ['USA', 'China']
num_companys = [num_usa, num_china]
plt.figure(figsize=(8, 6))
plt.bar(country, num_companys, color=['blue', 'red'])
plt.title('Número de Empresas Espaciais nos EUA e na China')
plt.ylabel('Número de Empresas')
plt.show()

# Exercício 2
df = paises_df[paises_df['Region'].str.strip().str.upper() == 'NORTHERN AMERICA']
natalidade = df['Birthrate']
mortalidade = df['Deathrate']
paises = df['Country']
plt.figure(figsize=(12, 8))
plt.plot(paises, natalidade, label='Taxa de Natalidade', marker='o')
plt.plot(paises, mortalidade, label='Taxa de Mortalidade', marker='o')
plt.title('Taxa de Natalidade e Mortalidade na América do Norte')
plt.xlabel('País')
plt.ylabel('Taxa')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
