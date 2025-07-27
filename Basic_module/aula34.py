"""
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

condicao = True

while condicao:
    nome = input('Qual é o seu nome: ')
    print(f'o seu nome é {nome}')
    if nome == 'sair':
        break
print("Acabou")