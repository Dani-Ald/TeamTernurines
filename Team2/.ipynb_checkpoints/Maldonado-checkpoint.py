def clases_sorted(clases, frecuencias):
    # Ordenar los datos basados en las clases
    data = sorted(zip(clases, frecuencias))
    list_c, list_FA = zip(*data)
    return list_c, list_Fa