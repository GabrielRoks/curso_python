# modulo intermediario
"""
Introdução às funções (def) em Python
funções são trechos de códigos usados para 
replicar determinada ação ao longo do seu código 
Elas podem receber valores para parâmetro (argumentos)
e retornar um valor específico.
Por padrão, funções em Python retornam None (nada)
"""

def saudacao(nome="Sem nome"): # usando o valor 'Sem nome' para caso o usuário não defina um argumento
    print(f'Olá, {nome}!')
saudacao("Gabriel")

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)
 
 
multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)