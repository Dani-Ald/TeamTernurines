# Frecuencia acumulada
def frecuencia_acumulada(frecuencias_relativas):
    frec_acumulada = []  # Inicializa una lista vacía para almacenar las frecuencias acumuladas
    acumulado = 0  # Inicializa una variable para llevar la suma acumulada

    for frecuencia in frecuencias_relativas:  # Itera sobre cada frecuencia relativa en la lista proporcionada
        acumulado += frecuencia  # Añade la frecuencia relativa actual al acumulado
        frec_acumulada.append(acumulado)  # Agrega el valor acumulado a la lista de frecuencias acumuladas

    return frec_acumulada  # Devuelve la lista de frecuencias acumuladas
