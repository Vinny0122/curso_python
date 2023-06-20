# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Vários Argumentos (xargs)
    
# Criar uma função que soma vários números.

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,3,4,7,4)
print(x)