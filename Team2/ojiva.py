import matplotlib.pyplot as plt

def crear_ojiva(marcas_clase, frecuencias, marcas_texto):
    # Ajustes necesarios para trazar la ojiva
    datos_x = [0] + marcas_clase 
    datos_y = [0] + frecuencias 

    plt.figure(figsize=(12, 6))  # Ancho, alto de la figura

    # Trazar la ojiva
    plt.plot(datos_x, datos_y, 
             linewidth=5, color="r", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="b")

    # Configuraciones adicionales del gráfico
    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Ojiva", fontsize=25)
    plt.grid(True)  # Activar la cuadrícula

    plt.show()  # Mostrar el gráfico

# Datos de ejemplo
marcas_clase = ['agua', 'arroz', 'cominos', 'gas', 'pollo', 'verduras']
frecuencias = [20.0, 33.33333333333333, 46.666666666666664, 60.0, 80.0, 100.0]
marcas_texto = ['Agua', 'Arroz', 'Cominos', 'Gas', 'Pollo', 'Verduras']

