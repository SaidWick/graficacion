import cv2
import numpy as np

# Cargar la imagen en escala de grises
img = cv2.imread(r"C:\Users\wicki\OneDrive\Documentos\Trabajos Graficacion\paisaje.jpg", cv2.IMREAD_GRAYSCALE)

# Obtener dimensiones de la imagen original
rows, cols = img.shape

# Crear una nueva imagen donde cada píxel esté rodeado de ceros
new_img = np.zeros((2 * rows - 1, 2 * cols - 1), dtype=img.dtype)
new_img[::2, ::2] = img

# Definir los vectores fila y columna
fila_kernel = np.array([-1, 0, 1])
columna_kernel = np.array([1, 2, 1])

# Aplicar convolución 1D en las filas (horizontal)
flt_img_filas = cv2.filter2D(new_img, ddepth=-1, kernel=fila_kernel.reshape(1, 3))

# Aplicar convolución 1D en las columnas (vertical)
flt_img_final = cv2.filter2D(flt_img_filas, ddepth=-1, kernel=columna_kernel.reshape(3, 1))

# Mostrar la imagen resultante
cv2.imshow('Imagen con convolución separable', flt_img_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
