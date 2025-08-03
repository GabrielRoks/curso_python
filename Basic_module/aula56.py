'''
split e join com list e str
split - divide uma string
join - une uma string
'''
frase = "Hoje foi um dia bacana"
lista_de_palavras = frase.split() #Vai criar uma lista, quebrando em cada espaço, pois o split está vazio
frase_2 = "Hoje foi um dia bacana, não concorda?"
lista_de_frases = frase_2.split(",") # Agora vai quebrar na vírgula
print(lista_de_palavras)
print(lista_de_frases)


frase3 = '   Olha só que   , coisa interessante          '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase3 in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# print(lista_frases_cruas)
# print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)