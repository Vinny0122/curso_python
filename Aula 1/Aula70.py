# List Comprenhension
    # Mais simples de se escrever
    # Utilizado quando você precisa criar uma nova lista a partit de uma exixtente
    # [expressão for iten in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
# frutas2 = []

# for iten in frutas1:
#     if 'b' in iten:
#         frutas2.append(iten)

frutas2 = [iten for iten in frutas1 if 'k' in iten]

print(frutas2)