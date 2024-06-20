# Frecuencia relativa
def frecuencia_relativa(frecuencia_absoluta):
    # Calcula el total de datos sumando todas las frecuencias absolutas
    tot_datos = sum(frecuencia_absoluta)
    
    frec_relativa = []

    # Calcula la frecuencia relativa para cada elemento en frecuencia_absoluta
    for i in range(len(frecuencia_absoluta)):
        frec_relativa.append((frecuencia_absoluta[i] / tot_datos) * 100)

    return frec_relativa