from utilidades import tokenizar, sintaxis
with open('archivo.txt') as f:
    entrada = f.read()
    lista = tokenizar('  \t\n ')
    print(lista)
