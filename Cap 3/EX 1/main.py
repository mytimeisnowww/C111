# Lista dos 5 primeiros colocados do Campeonato Mundial de Futebol
colocacao = ["Real Madrid", "Bayern Munich", "Liverpool", "Manchester City", "Barcelona"]

# a) Apenas os 3 primeiros colocados
tres_primeiros = colocacao[:3]
print("Os 3 primeiros colocados:", tres_primeiros)

# b) Os últimos 2 colocados
dois_ultimos = colocacao[-2:]
print("Os últimos 2 colocados:", dois_ultimos)

# c) Times em ordem alfabética
ordem_alfabetica = sorted(colocacao)
print("Times em ordem alfabética:", ordem_alfabetica)

# d) Em que posição da tabela está o Barcelona
posicao_barcelona = colocacao.index("Barcelona") + 1
print("Posição do Barcelona:", posicao_barcelona)
