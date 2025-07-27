"""
a função print usa o chamado argumento, e é utilizada para mostrar algo na tela, sempre 
começa com p minusculo
"""
# \r\n é a quebra de linha padrão do windows CRLF, ele não é visivel 
# \n é a quebra de linha do Mac e Linux LF, mas funcionou aqui tbm
print(12, 34, sep="-", end="##\n") 
"""esse comando sep= é utilizado para separar os argumentos não nomeados que estão dentro do print
argumentos não nomeados: 123... ou que não tenha um nome predefinido como o sep="""
print(56, 78, sep='-', end="\n")  # posso usar o Ctrl C e V para duplicar a linha
print(910, 1112, sep='-', end="\n")  # posso usar o Ctrl C e V para duplicar a linha
"""
Ctrl C e V para duplicar linha, não precisa selecionar a linha toda, somente uma parte
"""