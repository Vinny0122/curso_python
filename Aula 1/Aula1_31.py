# Listas
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']
itens = [['item1', 'item2'], ['item3', 'item4'],]

print(itens)
print(itens[0])
print(itens[1])
print(itens[1][1])

final = numeros * 2
print(final)

final = numeros + letras
print(final)

numeros.extend(letras)
print(numeros)