def tokenizar(entrada):
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
    return lista