#03
def sort_clases_fa(clases_originales, clases_sorted, fa_absolutas):
    '''
    Regresa lista de frecuencias absolutas ordenadas
    
    Ejemplo:    
    clases_originales = [0, 5, 7, 6, 4, 2]
    clases_sorted = [0, 2, 4, 5, 6, 7]
    fa_absolutas = [2, 3, 2, 1, 1, 2]
    fa_sorted = sort_clases_fa(clases_originales, clases_sorted, fa_absolutas):
    >>> [2, 2, 1, 3, 1, 2] 
    '''

    fa_sorted = []  # Inicializa una lista vacía para almacenar las frecuencias absolutas ordenadas

    for elemento in clases_sorted:  # Itera sobre cada elemento en clases_sorted
        idx = clases_originales.index(elemento)  # Encuentra el índice de elemento en clases_originales
        fa = fa_absolutas[idx]  # Obtiene la frecuencia absoluta correspondiente
        fa_sorted.append(fa)  # Agrega la frecuencia absoluta a fa_sorted

    return fa_sorted  # Devuelve la lista de frecuencias absolutas ordenadas