[2:02 p. m., 20/6/2024] +52 1 772 114 1865: # Find the lower and upper limits of the data
    lower_limit = min(frecuencias)
    upper_limit = max(frecuencias)
    
    return clases, frecuencias, lower_limit, upper_limit
[2:03 p. m., 20/6/2024] +52 1 772 114 1865: def generar_clase_y_FABS(arr):
    # Inicializar diccionario para contar frecuencias
    frecuencia_dict = {}
    
    # Contar frecuencias de cada elemento
    for item in arr:
        if item in frecuencia_dict:
            frecuencia_dict[item] += 1
        else:
            frecuencia_dict[item] = 1
            
    # Extraer clases y frecuencias en listas separadas
    clases = list(frecuencia_dict.keys())
    frecuencias = list(frecuencia_dict.values())
    
    # Find the lower and upper limits of the data
    lower_limit = min(frecuencias)
    upper_limit = max(frecuencias)
    
    return clases, frecuencias, lower_limit, upper_limit
[2:09 p. m., 20/6/2024] +52 1 772 114 1865: def imprimir_tabla(clases_orden, fa_sorted, frecuencia_rel, frecuencia_rel_acum, lower_limit, upper_limit):
    # Imprimir encabezados
    print('Clases'.ljust(10), 'Fa'.ljust(8), 'Fr'.ljust(8), 'F acumulada'.ljust(12), 'Lim inferior'.ljust(12), 'Lim superior'.ljust(12))
    print('------'.ljust(10), '---'.ljust(8), '---'.ljust(8), '-----------'.ljust(12), '------------'.ljust(12), '------------'.ljust(12))

    # Iterar sobre las clases y sus correspondientes datos
    for i in range(len(clases_orden)):
        print(f' {clases_orden[i]}'.ljust(10), 
              str(fa_sorted[i]).ljust(8), 
              str(frecuencia_rel[i]).ljust(8), 
              str(frecuencia_rel_acum[i]).ljust(12), 
              str(lower_limit).ljust(12), 
              str(upper_limit).ljust(12))

imprimir_tabla(clases_ordenadas, frecuencias_ordenadas, frecuencias_relativas, frecuencias_acumuladas, lower_limit, upper_limit)