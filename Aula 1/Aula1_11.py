
# Logical Operators (Operadores Lógicos)

renda_acima_5mil = True
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento negado')

renda_acima_5mil = False
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento negado')