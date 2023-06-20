# Tuples
    # Armazenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável
    # Não podem ser alterados (Imutable)

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
tres_listas = cores_tuple * 3

print(duas_listas)
print(tres_listas)
print(cores_tuple[1])