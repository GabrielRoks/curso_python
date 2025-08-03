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
        apagar_str = input("Digite o índice que deseja apagar: ")
        try:
           apagar = int(apagar_str)
           del lista_de_compras[apagar]
        except ValueError:
            print("Por favor digite apenas um número inteiro")
        except IndexError:
            print("Esse indice não existe")
        except Exception:
            print("Erro desconhecido")
    elif escolha == "l":
        os.system("cls")
        if len(lista_de_compras) == 0:
            print("Nada para listar")
        for i, item in enumerate(lista_de_compras):
            print(i, item)
    else:
        print("Escreva somente a inicial")