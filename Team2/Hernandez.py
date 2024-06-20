# Definición de la función generar_clase_y_FABS
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
    
    return clases, frecuencias

# Definición de la función clases_sorted
def clases_sorted(clases, frecuencias):
    # Ordenar los datos basados en las clases
    data = sorted(zip(clases, frecuencias))
    list_c, list_FA = zip(*data)
    return list_c, list_FA

# Ejemplo de uso
arreglo = ['agua', 'arroz', 'pollo', 'verduras', 'agua', 'verduras', 'arroz', 'pollo', 'gas', 'pollo', 'gas', 'cominos', 'verduras', 'agua', 'gas']

# Obtener clases y frecuencias
clases, frecuencias = generar_clase_y_FABS(arreglo)

# Ordenar y mostrar clases y frecuencias ordenadas
clases_ordenadas, frecuencias_ordenadas = clases_sorted(clases, frecuencias)
print("Clases ordenadas:", clases_ordenadas)
print("Frecuencias ordenadas:", frecuencias_ordenadas)