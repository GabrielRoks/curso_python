import os
lista_de_compras = []
# if len(escolha) > 1 and len(escolha) < 1:
#     print("Selecione apenas a primeira letra")
while True:
    escolha = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar: ").lower()
    if escolha == "i":
        os.system("cls")
        item = input("Digite o item que deseja inserir: ")
        lista_de_compras.append(item)
    elif escolha == "a":
        os.system("cls")
        indices = range(len(lista_de_compras))
        apagar = int(input("Digite o índice que deseja apagar: "))
        lista_de_compras.pop(apagar)
    elif escolha == "l":
        os.system("cls")
        if len(lista_de_compras) == 0:
            print("Nada para listar")
        for i, item in enumerate(lista_de_compras):
            print(i, item)
    else:
        print("Escreva somente a inicial")