# Erros 
    # Excelente para testes 
    # Não realiza o 'stop' no programa 
    # Mensagens customizadas quando encontra um erro 

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
    print(type(valor))
except ValueError:
    print('Favor digitar um valor em numeros')
print('Mais código abaixo...')