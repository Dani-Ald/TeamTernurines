def frecuencia_acumulada(frecuencias):
    total_datos = sum(frecuencias)
    frec_acumulada = [sum(frecuencias[:i+1]) / total_datos * 100 for i in range(len(frecuencias))]
    return frec_acumulada