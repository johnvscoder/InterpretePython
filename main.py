from utilidades import tokenizar
with open('archivo.txt') as f:
    entrada = f.read()
    lista = tokenizar(entrada)
    print(lista)