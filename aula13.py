nome = 'Gabriel Roks'
altura = 1.78
peso = 71
imc = peso / altura ** 2

# f-strings
linha_1 = f'{nome} Tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é {imc:.2f}'

print(linha_1)
print(linha_2)