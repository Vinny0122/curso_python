# Dicionários
    # Utiliza index no formato de keys e values
    # Aceita string, integer, float, boolean...

aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovação': True}
print(aluno)
print(aluno['nome'])
print(aluno['idade'])

aluno['nome'] = 'José'
print(aluno)

aluno.update({'nome': 'Vinícius', 'nota_final': 'B'})
print(aluno)

aluno.update({'endereco': 'Rua A'})
print(aluno)

print(aluno.get('tipo'))
print(aluno.get('tipo', 'Não existe'))

del aluno['idade']
print(aluno)