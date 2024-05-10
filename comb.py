import cv2
import numpy as np
import matplotlib.pyplot as plt

def combinar_imagenes(imagen_original, mascara_binaria, fondo_nuevo,titulo):
    # Verificar que las imágenes se hayan cargado correctamente
    if imagen_original is None or mascara_binaria is None or fondo_nuevo is None:
        print("No se pudieron cargar las imágenes.")
        return None

    # Aplicar la máscara binaria a la imagen original
    objeto_destacado = cv2.bitwise_and(imagen_original, imagen_original, mask=mascara_binaria)

    # Invertir la máscara binaria para obtener el fondo
    fondo = cv2.bitwise_not(mascara_binaria)

    # Aplicar la máscara inversa al fondo nuevo
    fondo_invertido = cv2.bitwise_and(fondo_nuevo, fondo_nuevo, mask=fondo)

    # Combinar el objeto destacado y el fondo
    imagen_combinada = cv2.add(objeto_destacado, fondo_invertido)

    if imagen_combinada is not None:
        imagen_combinada_rgb = cv2.cvtColor(imagen_combinada, cv2.COLOR_BGR2RGB)
        plt.imshow(imagen_combinada_rgb)
        plt.title(titulo)
        plt.axis('off')
        plt.show()


