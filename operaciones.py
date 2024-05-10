import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar las imágenes
imagen1 = cv2.imread('IMG/merged_imageF1.jpg', cv2.IMREAD_GRAYSCALE)
imagen2 = cv2.imread('IMG/objetoN.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar que las imágenes se cargaron correctamente
if imagen1 is None or imagen2 is None:
    print("No se pudieron cargar las imágenes.")
else:
    # Calcular la diferencia entre las imágenes
    diferencia = cv2.absdiff(imagen1, imagen2)

    # Aplicar un umbral para obtener una máscara binaria
    umbral, mascara = cv2.threshold(diferencia, 39, 255, cv2.THRESH_BINARY)
    cv2.imwrite('IMG/umbral.jpg', mascara)
