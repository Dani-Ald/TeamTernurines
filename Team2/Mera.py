def imprimir_tabla(clases_orden, fa_sorted, frecuencia_rel, frecuencia_rel_acum, lower_limit, upper_limit):
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