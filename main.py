import cv2
import numpy as np
from mostrar import mostrar_imagenes
from comb import combinar_imagenes
# Cargar la imagen
imagen = cv2.imread('IMG/Piramide_Red.jpg', cv2.IMREAD_GRAYSCALE)

# Verificar que la imagen se cargó correctamente
if imagen is None:
    print("No se pudo cargar la imagen.")
else:
    # Definir la máscara de filtro de media de 11x11
    mascara_media = np.ones((11, 11), np.float32) / 121

    # Aplicar convolución con la máscara de filtro de media
    imagen_filtrada_media = cv2.filter2D(imagen, -1, mascara_media)

    # Definir la máscara de filtro de suavizado gaussiano de 11x11
    mascara_gaussiana = cv2.getGaussianKernel(11, 0)

    # Aplicar convolución con la máscara de filtro de suavizado gaussiano
    imagen_filtrada_gaussiana = cv2.filter2D(imagen, -1, mascara_gaussiana * mascara_gaussiana.T)

    # Guardar las imágenes procesadas
    cv2.imwrite('IMG/imagen_grises.jpg', imagen)
    cv2.imwrite('IMG/imagen_filtrada_media.jpg', imagen_filtrada_media)
    cv2.imwrite('IMG/imagen_filtrada_gaussiana.jpg', imagen_filtrada_gaussiana)

mostrar_imagenes([imagen, imagen_filtrada_media, imagen_filtrada_gaussiana],
                     ['Imagen Original', 'Filtro de Media', 'Suavizado Gaussiano'])
original = cv2.imread('IMG/objetoN.jpg')
mascara_binaria = cv2.imread('IMG/umbral.jpg', cv2.IMREAD_GRAYSCALE)
fondo_nuevo = cv2.imread('IMG/imagen_filtrada_media.jpg')
fondo_nuevo2 = cv2.imread('IMG/imagen_filtrada_gaussiana.jpg')
Imagen_comb_media = combinar_imagenes(original,mascara_binaria,fondo_nuevo)
Imagen_comb_gauss = combinar_imagenes(original,mascara_binaria,fondo_nuevo2)

mostrar_imagenes([Imagen_comb_media,Imagen_comb_gauss],['Imagen con filtro de media','Imagen con filtro gaussiano'])

