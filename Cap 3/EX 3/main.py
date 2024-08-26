# Criação do dicionário aluno
aluno = {
    "nome": input("Digite o nome do aluno: "),
    "media": float(input("Digite a média do aluno: "))
}

# Determinação da situação do aluno
if aluno["media"] >= 60:
    aluno["situacao"] = "AP"  # Aprovado
else:
    aluno["situacao"] = "RP"  # Reprovado

# Exibição do conteúdo do dicionário
print("\nInformações do Aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")
