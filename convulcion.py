import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread(r"C:\Users\wicki\OneDrive\Documentos\Trabajos Graficacion\paisaje.jpg", cv2.IMREAD_GRAYSCALE)

# Obtener dimensiones de la imagen original
rows, cols = img.shape

# Crear una nueva imagen donde cada píxel esté rodeado de ceros
# La nueva imagen tendrá dimensiones mayores, por lo que multiplicamos por 2 y sumamos 1
new_img = np.zeros((2 * rows - 1, 2 * cols - 1), dtype=img.dtype)

# Rellenar la nueva imagen con los píxeles originales
new_img[::2, ::2] = img

# Ahora puedes aplicar cualquier filtro o procesamiento sobre la nueva imagen

# Mostrar la imagen resultante
cv2.imshow('Imagen con ceros', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
