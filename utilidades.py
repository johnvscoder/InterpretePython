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
# def tipoInstruccion(tokens):
    
#     lon = len(tokens)
#     # Cada instrucción tiene al menos 3 tokens
#     if lon < 3:
#         print('Error. Instruccion inválida')
#         return None
#     # Si el primer token es número
#     # no es identificador y eso es un error
#     if tokens[0].isdecimal():
#         print('Error. Instruccion inválida')
#         return None
#     if tokens[1] == '=':
#         if not(tokens[2].isnum()):
#             print('Error. Instruccion inválida')
#             return None
#         else:
#             if lon > 3:
#                 print('Error. Instruccion inválida')
#                 return None
#             else:
#                 return 'asignacion'
#     elif tokens[1] == '-':
#         if tokens[2] == '>':
#             print('')


# Probado
def esAsignacion(tokens):
    # deben ser exactamente 3 tokens
    if len(tokens) != 3:
        return False
    # la primera condición es que el primer token sea identificador
    # la segunda condición es que el segundo token sea =
    # la tercera condición es que el tercer token sea un número
    return esIdentificador(tokens[0]) and tokens[1] == '=' and tokens[2].isdecimal()

# Probado
def esEcuacion(tokens):
    if len(tokens) != 6 and len(tokens) != 8:
        return False
    
    if len(tokens) == 6:
        return esIdentificador(tokens[0]) and tokens[1] == '-' and tokens[2] == '>' and esIdentificador(tokens[3]) and tokens[4] == '=' and (esIdentificador(tokens[5]) or tokens[5].isdecimal())
    if len(tokens) == 8:
        return esIdentificador(tokens[0]) and tokens[1] == '-' and tokens[2] == '>' and esIdentificador(tokens[3]) and tokens[4] == '=' and (esIdentificador(tokens[5]) or tokens[5].isdecimal()) and esOperador(tokens[6]) and (esIdentificador(tokens[7]) or tokens[7].isdecimal())
    
# Probado
def esIdentificador(token):
    if token == None or len(token) == 0:
        return False
    return token.isalnum() and token[0].isalpha()

# Probado
def esOperador(token):
    return token == '+' or token == '-' or token == '*' or token == '/'