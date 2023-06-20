# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Realizam uma tarefa
    # Calcula e retorna um valor

def cliente1(nome):
    print(f'Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)