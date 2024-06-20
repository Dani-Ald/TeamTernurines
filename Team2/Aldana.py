def generar_clase_y_FABS(arr):
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