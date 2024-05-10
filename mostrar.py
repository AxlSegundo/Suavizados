import matplotlib.pyplot as plt

def mostrar_imagenes(imagenes, titulos):
    """
    Muestra las imágenes en una sola fila con sus respectivos títulos.

    Args:
        imagenes (list): Lista de imágenes.
        titulos (list): Lista de títulos para cada imagen.
    """
    num_imagenes = len(imagenes)
    fig, axs = plt.subplots(1, num_imagenes, figsize=(5*num_imagenes, 5))

    for i in range(num_imagenes):
        axs[i].imshow(imagenes[i], cmap='gray')
        axs[i].set_title(titulos[i])
        axs[i].axis('off')

    plt.show()
