# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Parametro --> Argumento
    # Default = Aquele que você define o valor no parametro
    # Non-Default = Aquele que você não define o valor no parametro

def boas_vindas(nome, quantidade=5):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

def boas_vindas1(quantidade, nome='Linda'):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque')

boas_vindas('Marcos')
boas_vindas1(6)