# Separa una cadena de texto en tokens
def tokenizar(entrada):
    if entrada == None:
        print('Error. Argumento None')
        return None
    if entrada == '':
        print('Error. cadena vacía')
        return None

    # Guarda la lista de tokens
    lista =[]

    i = 0
    # Guarda la posición de inicio de un identificador
    pos = 0
    while i < len(entrada):
        # Se ignoran espacios, tabulaciones y saltos de línea
        if entrada[i] == ' ' or entrada[i] == '\t' or entrada[i] == '\n':
            i = i + 1
            continue
        # Si el caracter actual es el inicio de un identificador
        # se guarda su posición
        if entrada[i].isalnum() and (i == 0 or not(entrada[i - 1].isalnum())):
            pos = i
        # Si el caracter actual es el fin de un identificador
        # éste se agrega a la lista
        if entrada[i].isalnum() and (i == len(entrada) - 1 or not(entrada[i + 1].isalnum())):
            identificador = entrada[pos:i + 1]
            # Se valida el identificador
            if not(identificador.isdecimal()) and not(identificador[0].isalpha()):
                print('Error. identificador inválido')
                return None
            lista.append(identificador)

        # Si el caracter actual no es alfanumérico
        # se agrega a la lista
        if not(entrada[i].isalnum()):
            lista.append(entrada[i])
        i = i + 1
    
    if len(lista) == 0:
        print('Error. No hay tokens')
        return None
    return lista


# Separa los tokens en instrucciones y detecta
# de qué tipo es cada instrucción
def sintaxis(tokens):
    # Guarda las instrucciones
    lista = []
    # Guarada una instrucción
    instruccion = []

    # Este ciclo separa las instrucciones por ;
    # y las guarda en lista
    for token in tokens:
        if token == ';':
            lista.append(instruccion)
            instruccion = []
        else:
            instruccion.append(token)
    
    # Si el último token no es ;
    # la última instrucción pudo no haberse guardado
    # en el ciclo anterior, entonces se guarda aquí.
    if len(instruccion) != 0:
        lista.append(instruccion)
    return lista

# Dice a qué tipo pertenece una instrucción
def tipoInstruccion(tokens):
    # Si el primer token es número
    # no es identificador y eso es un error
    if tokens[0].isdecimal():
        print('Error. se esperaba un identificador y se obtuvo un número')
    
