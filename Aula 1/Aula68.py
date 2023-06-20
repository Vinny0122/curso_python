# Map Function
    # Muito utilizado em listas
    # Aplicar uma função a um Iterable, por item. (list, tuple, dicionary, etc)

lista1 = [1, 2, 3, 4]

def multi(x):
    return x * 2

print(multi(2))

lista2 = map(multi, lista1)

print(lista2)
print(list(lista2))
print('============================================================================')

lista2 = map(lambda x: x * 2, lista1)

print(list(lista2))

print(list(map(lambda x: x * 2, lista1)))