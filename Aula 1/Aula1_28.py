# Functions (Funções)
    # DRY - Don't repeat yourself.
    # Vários Argumentos (xargs) identificando o Parametro
    
# Criar uma função que armazena numeros e strings (dados)

def agencia(**carro):
    return carro

print (agencia(marca='Gol',cor='Banca',motor=1.0, placa=1234))
print (agencia(marca='Gol',cor='Azul',motor=1.0))
print (agencia(marca='Gol',cor='Preto',motor=1.0, placa=1444))