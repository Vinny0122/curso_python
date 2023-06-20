
velocidade = 100

if velocidade > 100:
    print('Acima da velocidade permitida')
    print('Favor, reduzir a velocidade.')
else:
    print('Velocidade OK')

velocidade = 120

if velocidade > 100:
    print('Acima da velocidade permitida')
    print('Favor, reduzir a velocidade.')
else:
    print('Velocidade OK')

velocidade = 40

if velocidade > 100:
    print('Acima da velocidade permitida')
    print('Favor, reduzir a velocidade.')
elif velocidade < 60:
    print('Favor, dirigir acima de 80KM/h')
else:
    print('Velocidade OK')