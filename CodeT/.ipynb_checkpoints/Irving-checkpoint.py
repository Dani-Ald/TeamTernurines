def ordenar_asc(arreglo):
    '''
    Regresa el arreglo ordenado de forma
    ascendente.
    
    Ejemplo:
    arreglo = [0, 5, 7, 6, 4, 2]
    arr_sorted = ordenar_asc(arreglo)
    >>> [0, 2, 4, 5, 6, 7]
    '''
    arr_len = len(arreglo)  # Obtiene la longitud del arreglo

    for i in range(arr_len):  # Itera a través de cada índice del arreglo
        min_idx = i  # Supone que el índice actual es el mínimo

        # Encuentra el índice del elemento mínimo en el resto del arreglo
        for j in range(i+1, arr_len):
            if arreglo[j] < arreglo[min_idx]:  # Si encuentra un elemento menor
                min_idx = j  # Actualiza el índice del mínimo

        # Intercambia el elemento actual con el mínimo encontrado
        arreglo[i], arreglo[min_idx] = arreglo[min_idx], arreglo[i]

    return arreglo  # Devuelve el arreglo ordenado de forma ascendente