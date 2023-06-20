# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}

for x in aluno.keys():
    print(x)

print()
for x in aluno.values():
    print(x)

print()
for x in aluno.items():
    print(x)

print()
for chaves, valores in aluno.items():
    print(chaves, valores)