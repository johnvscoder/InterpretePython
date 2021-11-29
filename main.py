from utilidades import tokenizar, sintaxis, ejecutar

ruta = input('Ingrese la ruta del archivo: ')
with open(ruta) as f:
    entrada = f.read()
    lista = tokenizar(entrada)
    sintaxis1 = sintaxis(lista)
    semantica = ejecutar(sintaxis1)