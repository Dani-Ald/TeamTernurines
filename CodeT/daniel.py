def imprimir_tabla(clases_orden, fa_sorted, frecuencia_rel, frecuencia_rel_acum):
    # Imprimir encabezados
    print('Clases'.ljust(10), 'Fa'.ljust(8), 'Fr'.ljust(8), 'F acumulada'.ljust(12))
    print('------'.ljust(10), '---'.ljust(8), '---'.ljust(8), '-----------'.ljust(12))

    # Iterar sobre las clases y sus correspondientes datos
    for i in range(len(clases_orden)):
        print(f'Clase {clases_orden[i]}'.ljust(10), 
              str(fa_sorted[i]).ljust(8), 
              str(frecuencia_rel[i]).ljust(8), 
              str(frecuencia_rel_acum[i]).ljust(12))

# Ejemplo de uso:
# Suponiendo que tienes las listas correspondientes definidas antes de llamar la función:
# clases_orden = ['1', '2', '3', '4']
# fa_sorted = [6, 2, 11, 15]
# frecuencia_rel = [17.647058823529413, 5.88235294117647, 32.35294117647059, 44.11764705882353]
# frecuencia_rel_acum = [17.647058823529413, 23.529411764705884, 55.88235294117647, 100.0]

# Llamada a la función para imprimir la tabla
# imprimir_tabla(clases_orden, fa_sorted, frecuencia_rel, frecuencia_rel_acum)
