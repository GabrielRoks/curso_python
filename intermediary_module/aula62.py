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