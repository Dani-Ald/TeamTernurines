import matplotlib.pyplot as plt
# Función para crear el histograma
def crear_histograma(marcas_clase, frecuencias):
    plt.figure(figsize=(12, 6))
    plt.bar(marcas_clase, frecuencias,
           width=1, edgecolor="k",
           color=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.show()

# Función para crear el diagrama de barras
def crear_diagrama_barras(marcas_clase, frecuencias, marcas_texto):
    plt.figure(figsize=(12, 6))
    
    plt.barh(marcas_clase, frecuencias,
             height=0.75, edgecolor="k",
             color=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"])
    
    plt.yticks(marcas_clase, marcas_texto, fontsize=15)
    plt.xlabel("Frecuencias", fontsize=20)
    plt.ylabel("Marcas de clase", fontsize=20)
    plt.title("Diagrama de barras", fontsize=25)
    plt.grid()
    plt.show()


def crear_poligono_frecuencias(marcas_clase, frecuencias, marcas_texto):
    # Ajustes necesarios para trazar el polígono
    datos_x = [0] + list(marcas_clase) + [7]
    datos_y = [0] + list(frecuencias) + [0]

    plt.figure(figsize=(12, 6))  # Ancho, alto de la figura

    # Trazar el polígono de frecuencias
    plt.plot(datos_x, datos_y, 
             linewidth=5, color="r", linestyle=":", 
             marker="v", markersize=15, markerfacecolor="y", markeredgecolor="b")

    # Configuraciones adicionales del gráfico
    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencias", fontsize=20)
    plt.title("Polígono de frecuencias", fontsize=25)
    plt.grid(True)  # Activar la cuadrícula


# Función para crear gráfico de pastel
import matplotlib.pyplot as plt
def crear_grafico_pastel(datos, marcas_texto):
    separaciones = [0] * len(datos)  # Lista de ceros del mismo tamaño que datos
    plt.figure(figsize=(8, 8))
    plt.pie(datos, 
            explode=separaciones,  
            counterclock=False, 
            startangle=90, 
            autopct="%0.1f%%", 
            pctdistance=0.8, 
            colors=["#EF90F1", "#90E7F1", "#D8B4EF", "#C7EFB4", "#EFB4C7", "#EFE4B4"], 
            labels=marcas_texto)
    plt.title("Grafico de pastel", fontsize=20)
    plt.show()




