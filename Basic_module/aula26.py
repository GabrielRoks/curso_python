"""
Formatação básica de strings
s - string
d - int
f- float
.<número de digitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: >10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')
