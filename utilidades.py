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
# probado
def sintaxis(tokens):
    if tokens == None:
        print('Error. método sintaxis recibió argumento None')
        return None
    # Guarda las instrucciones
    lista = []
    # Guarada una instrucción
    instruccion = []

    # Este ciclo separa las instrucciones por ;
    # y las guarda en lista
    for token in tokens:
        if token == ';':
            if not(esInstruccionValida(instruccion)):
                print('Error. Instrucción inválida')
                return None
            lista.append(instruccion)
            instruccion = []
        else:
            instruccion.append(token)
    
    # Si el último token no es ;
    # la última instrucción pudo no haberse guardado
    # en el ciclo anterior, entonces se guarda aquí.
    if len(instruccion) != 0:
        if not(esInstruccionValida(instruccion)):
            print('Error. Instrucción inválida')
            return None
        lista.append(instruccion)
    return lista

# Probado
def esInstruccionValida(tokens):
    return esLlamada(tokens) or esAsignacion(tokens) or esEcuacion(tokens)

# Probado
def esLlamada(tokens):
    if len(tokens) != 4:
        return False
    
    return esIdentificador(tokens[0]) and tokens[1] == '(' and (esIdentificador(tokens[2]) or tokens[2].isdecimal()) and tokens[3] == ')'

# Probado
def esAsignacion(tokens):
    # deben ser exactamente 3 tokens
    if len(tokens) != 3:
        return False
    # la primera condición es que el primer token sea identificador
    # la segunda condición es que el segundo token sea =
    # la tercera condición es que el tercer token sea un número
    return esIdentificador(tokens[0]) and tokens[1] == '=' and (esIdentificador(tokens[2]) or tokens[2].isdecimal())

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

def ejecutar(sintaxis):
    if sintaxis == None:
        print('Error. Valor none')
        return None
    
    variables = {}
    for instruccion in sintaxis:
        if esAsignacion(instruccion):
            # Comprobar que el valor que se asignará existe
            existeValor = True
            if not(instruccion[2].isdecimal()):
                existeValor = False
                for clave in variables:
                    if clave == instruccion[2]:
                        existeValor = True
            if not(existeValor):
                print('Error. Variable en asignación no existe')
                exit()
            
            # Se obtiene el valor que se asignará
            valorFinal = 0
            if instruccion[2].isdecimal():
                valorFinal = int(instruccion[2])
            else:
                valorFinal = int(variables[instruccion[2]])
            
            # Comprobar si la variable a la cual se asigna un valor existe
            existeVariable = False
            for clave in variables:
                    if clave == instruccion[0]:
                        existeVariable = True

            # Asignar el valor a la variable
            if existeVariable:
                variables[instruccion[0]] = valorFinal
            else:
                variables.setdefault(instruccion[0], valorFinal)
        elif esEcuacion(instruccion):
            # Comprobar que la variable de asignacion exista
            existeVariable = False
            for clave in variables:
                    if clave == instruccion[0]:
                        existeVariable = True

            # Se extrae la ecuación de la variable instruccion
            valorFinal = instruccion[3 : len(instruccion)]
            # Asignar el valor a la variable
            if existeVariable:
                variables[instruccion[0]] = valorFinal
            else:
                variables.setdefault(instruccion[0], valorFinal)
        elif esLlamada(instruccion):
            # Se verifica que la función sea válida
            if not(instruccion[0] == 'imprimir') and not(instruccion[0] == 'resolver'):
                print('Error. Invocación de función inválida')
                return None
            if instruccion[0] == 'imprimir':
                if instruccion[2].isdecimal():
                    print(int(instruccion[2]))
                else:
                    # Se verifica que la variable del argumento exista
                    existeVariable = False
                    for clave in variables:
                        if clave == instruccion[2]:
                            existeVariable = True
                    if not(existeVariable):
                        print('Error. Llamada a función con argumento que no existe')
                        return None

                    valor = variables[instruccion[2]]
                    if isinstance(valor, int) or isinstance(valor, float):
                        print(valor)
                    elif isinstance(valor, list):
                        ecuacion = ''
                        # Se concatenan los elementos de la ecuación en una cadena
                        for token in valor:
                            ecuacion = ecuacion + ' ' + token
                        # Se elimina el espacio inicial agregado en el ciclo
                        ecuacion = ecuacion[1: len(ecuacion)]
                        print(ecuacion)
            else: # En este caso la función es resolver
                # Validamos que el argumento no sea un número pues no tiene sentido
                # resolver un número
                if instruccion[2].isdecimal():
                    print('Error. Argumento inválido en llamada a la función resolver')
                    return None
                # Determinar si la variable del argumento existe
                # y, si existe, se comprueba si guarda una ecuacion (una lista en este caso)
                existeVariable = False
                # Guardará la ecuación
                valorVariable = None
                for clave in variables:
                    if clave == instruccion[2]:
                        existeVariable = True
                        # Guardamos la ecuación en la lista valorVariable
                        valorVariable = variables[instruccion[2]]
                        break
                if not(existeVariable):
                    print('Error. Argumento inválido en llamada a la función resolver')
                    return None
                # Verificamos que el valor de la variable no sea un entero
                # pues no tiene sentido resolver un entero
                if isinstance(valorVariable, int):
                    print('Error. Argumento no hace referencia a una ecuación en llamada a la función resolver')
                    return None
                
                # Verificamos cada variable y comprobamos que halla una sola incógnita
                # y que las demás variables sean conocidas
                # Además, calculamos los valores de cada término
                hayIncognita = False
                # En qué posición de la lista valorVariable está la incógnita
                indiceIncognita = 0

                # Los valores de cada término
                valor1 = None
                valor2 = None
                valor3 = None

                # Verificamos la primer variable
                existeVariable = False
                for clave in variables:
                    if clave == valorVariable[0]:
                        existeVariable = True
                if not(existeVariable):
                    hayIncognita = True
                else:
                    valor1 = variables[valorVariable[0]]
                
                # Verificamos la segunda variable
                if esIdentificador(valorVariable[2]):
                    existeVariable = False
                    for clave in variables:
                        if clave == valorVariable[2]:
                            existeVariable = True
                    if not(existeVariable):
                        if hayIncognita:
                            print('No se pudo resolver la ecuación', instruccion[2], 'porque tiene más de una incógnita')
                            continue
                        else:
                            hayIncognita = True
                            indiceIncognita = 2
                    else:
                        valor2 = variables[valorVariable[2]]
                else:
                    valor2 = int(valorVariable[2])
                
                # Verificamos la tercera variable
                # si existe
                if len(valorVariable) > 3:
                    if esIdentificador(valorVariable[4]):
                        existeVariable = False
                        for clave in variables:
                            if clave == valorVariable[4]:
                                existeVariable = True
                        if not(existeVariable):
                            if hayIncognita:
                                print('No se pudo resolver la ecuación', instruccion[2], 'porque tiene más de una incógnita')
                                continue
                            else:
                                hayIncognita = True
                                indiceIncognita = 4
                        else:
                            valor3 = variables[valorVariable[4]]
                    else:
                        valor3 = int(valorVariable[4])
                
                if not(hayIncognita):
                    print('No se pudo resolver la ecuación', instruccion[2], 'porque no tiene incógnitas')
                    continue
                    
                # Ahora se resuelve la ecuación
                # Primero cuando en el miembro derecho hay operador
                if len(valorVariable) > 3:
                    operador = valorVariable[3]

                    # Validamos que no haya divisón por cero
                    if operador == '/' and valor3 == 0:
                        print('No se pudo resolver la ecuación', instruccion[2], 'porque se halló una división por cero')
                        continue

                    if indiceIncognita == 0:
                        respuesta = 0
                        if operador == '+':
                            respuesta = valor2 + valor3
                        elif operador == '-':
                            respuesta = valor2 - valor3
                        elif operador == '*':
                            respuesta = valor2 * valor3
                        elif valor3 != 0:
                            respuesta = valor2 / valor3
                        else:
                            print('No se pudo resolver la ecuación', instruccion[2], 'porque se halló una división por cero')
                            continue
                        variables.setdefault(valorVariable[0], respuesta)
                    elif indiceIncognita == 2:
                        respuesta = 0
                        if operador == '+':
                            respuesta = valor1 - valor3
                        elif operador == '-':
                            respuesta = valor1 + valor3
                        elif operador == '*':
                            if valor3 != 0:
                                respuesta = valor1 / valor3
                            else:
                                print('No se pudo resolver la ecuación', instruccion[2], 'porque se halló una división por cero')
                                continue
                        elif operador == '/':
                            respuesta = valor1 * valor3
                        variables.setdefault(valorVariable[2], respuesta)
                    elif indiceIncognita == 4:
                        respuesta = 0
                        if operador == '+':
                            respuesta = valor1 - valor2
                        elif operador == '-':
                            respuesta = valor2 - valor1
                        elif operador == '*':
                            if valor2 != 0:
                                respuesta = valor1 / valor2
                            else:
                                print('No se pudo resolver la ecuación', instruccion[2], 'porque se halló una división por cero')
                                continue
                        elif valor1 != 0:
                            respuesta = valor2 / valor1
                        else:
                            print('No se pudo resolver la ecuación', instruccion[2], 'porque se halló una división por cero')
                            continue
                        variables.setdefault(valorVariable[4], respuesta)
                else: # En este caso no hay operador en el miembro derecho
                    if indiceIncognita == 0:
                        variables.setdefault(valorVariable[0], valor2)
                    else: # el indice es 2
                        variables.setdefault(valorVariable[2], valor1)
    return variables