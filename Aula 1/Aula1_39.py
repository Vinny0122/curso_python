# Set (Listas)
    # Similar as Listas
    # Evita itens duplicados
    # Não utiliza index

lista1 = [10, 20, 30, 40, 50]
lista2 = [10, 20, 60, 70]

num1 = set(lista1)
num2 = set(lista2)

print(num1 | num2) # | = União
print(num1 - num2) # - = Diferença
print(num1 ^ num2) # ^ = Diferença Simétrica
print(num1 & num2) # & = E

print(len(num1))