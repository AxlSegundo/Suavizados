**comb.py**<br>
Combina las imágenes con el mismo proceso que se utilizo en la práctica de combinación de imágenes
**main.py**<br>
La imagen a suavizar la transforma a escala de grises.<br>
Crea las máscaras para cada filtro y a cada uno aplica la convolución<br>
Guarda las imágenes<br>
LLama a una función de otro módulo para mostrar los resultados<br>
Abrimos las imágenes para cada combinación<br>
LLama a la función combinar_imagenes del módulo comb.py para hacer la combinación con cada filtro y muestra los cambios<br>
**mostrar.py**<br>
Se encarga de mostrar los resultados de cada filtro y que se puedan comparar con la imagen original<br>
Esto lo hace con matplotlib que los muestra como si fueran gráficas<br>
**operaciones.py**<br>
Solo se encarga de realizar la resta entre el modelo y el objeto y crear el umbral para facilitar el trabajo de la combinación<br>