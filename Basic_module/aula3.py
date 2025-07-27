"""
Python = linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> String -> Texto
String são textos que estão dentro de aspas
A cada vírgula que separa o texto do print, precisa de aspas
"""

# Aspas simples
print('Gabriel Roks')

# Aspas duplas
print("Gabriel Roks")

# Escape
print("Gabriel \"Roks\"") 
"""A contrabarra é utilizada como escape para o interoretador
 não ler o prox caractere, que no caso é a aspas. É utilizado quando
 vai usar mais de duas aspas na mesma string por exemplo"""

# r
print(r"Gabriel \"Roks\"") 
"""r é utilizado antes da aspas para mostrar o caractere de escape"""

# Para facilitar
print(1, 'Gabriel "Roks"') 
""" Utilizar aspas duplas dentro de aspas simples.
Iniciar com aspas simples, colocar aspas dupla na palavra que quer (começo e final)
e fechar com aspas simples.
Caso queira que a palavra tenha aspas simples, é só inverter
"""
print(2, "Gabriel 'Roks'") 
