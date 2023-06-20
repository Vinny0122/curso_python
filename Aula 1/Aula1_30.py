# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador']
print(cidades)
print(cidades[0])
numeros = [2, 4, 6]
cidades[0] = 'Brasília'

cidades.append('Santa Catarina')
cidades.remove('Brasília')
cidades.insert(1, 'Santa Catarina')
cidades.pop(0)
cidades.sort()

print(cidades)
print(cidades[0])
print(cidades[-1])
print(numeros)