def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplica(1,3,5,6,3)
print(multiplicacao)

def parimpar(numero):
    multiplo_de_dois = numero % 2 == 0 
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'
print(parimpar(2))
print(parimpar(52345))
print(parimpar(5))
print(parimpar(6))