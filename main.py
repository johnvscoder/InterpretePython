from utilidades import tokenizar, sintaxis
with open('archivo.txt') as f:
    entrada = f.read()
    lista = tokenizar(entrada)
    sintaxis1 = sintaxis(lista)
    print(sintaxis1)