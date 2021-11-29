from utilidades import tokenizar, sintaxis, ejecutar
with open('archivo.txt') as f:
    entrada = f.read()
    lista = tokenizar(entrada)
    sintaxis1 = sintaxis(lista)
    semantica = ejecutar(sintaxis1)