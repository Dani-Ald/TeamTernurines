# Función para calcular la frecuencia acumulada
def frecuencia_acumulada(frecuencias_relativas):
    frec_acumulada = []  # Inicializa una lista vacía para almacenar las frecuencias acumuladas
    acumulado = 0  # Inicializa una variable para llevar la suma acumulada

    for frecuencia in frecuencias_relativas:  # Itera sobre cada frecuencia relativa en la lista proporcionada
        acumulado += frecuencia  # Añade la frecuencia relativa actual al acumulado
        frec_acumulada.append(acumulado)  # Agrega el valor acumulado a la lista de frecuencias acumuladas

    return frec_acumulada  # Devuelve la lista de frecuencias acumuladas

# Función para calcular la frecuencia relativa
def frecuencia_relativa(frecuencia_absoluta):
    # Calcula el total de datos sumando todas las frecuencias absolutas
    tot_datos = sum(frecuencia_absoluta)
    
    frec_relativa = []

    # Calcula la frecuencia relativa para cada elemento en frecuencia_absoluta
    for i in range(len(frecuencia_absoluta)):
        frec_relativa.append((frecuencia_absoluta[i] / tot_datos) * 100)

    return frec_relativa

# Función para calcular la frecuencia acumulada
def frecuencia_acumulada(frecuencias_relativas):
    frec_acumulada = []  # Inicializa una lista vacía para almacenar las frecuencias acumuladas
    acumulado = 0  # Inicializa una variable para llevar la suma acumulada

    for frecuencia in frecuencias_relativas:  # Itera sobre cada frecuencia relativa en la lista proporcionada
        acumulado += frecuencia  # Añade la frecuencia relativa actual al acumulado
        frec_acumulada.append(acumulado)  # Agrega el valor acumulado a la lista de frecuencias acumuladas

    return frec_acumulada  # Devuelve la lista de frecuencias acumuladas
