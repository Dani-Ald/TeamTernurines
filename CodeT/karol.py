def frec_abs(datos_entrada):
    '''
    clases, fa_absoluta = frec_abs(datos_entrada)
    Regresa las clases y frecuencias absolutas 
    de cada clase dada una lista de datos
    
    Ejemplo:
    datos_entrada = [0, 1, 2, 0, 1, 3, 1, 3]
    clases, fa_absoluta = frec_abs(datos_entrada)
    >>> clases = [0, 1, 2, 3]
    >>> fa_absoluta = [2, 3, 1, 2]
    '''
    clases, fa_absoluta = [], []  # Inicializa dos listas vacías para almacenar las clases y sus frecuencias absolutas
    
    for elemento in datos_entrada:  # Itera sobre cada elemento en la lista datos_entrada
        if elemento not in clases:  # Si el elemento no está en la lista clases
            clases.append(elemento)  # Agrega el elemento a la lista clases
            fa_absoluta.append(1)    # Inicializa su frecuencia absoluta con 1
        else:                        # Si el elemento ya está en la lista clases
            idx = clases.index(elemento)  # Encuentra el índice del elemento en la lista clases
            fa_absoluta[idx] += 1         # Aumenta su frecuencia absoluta en 1

    return clases, fa_absoluta   # Devuelve las listas clases y fa_absoluta que contienen las clases y sus frecuencias absolutas respectivamente