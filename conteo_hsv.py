import numpy as np
import cv2 

img = cv2.imread(r"C:\Users\wicki\OneDrive\Documentos\Trabajos Graficacion\salida.png")


imagen_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

color1_buscado = [108, 100, 100]

tolerancia = 5
bajo = np.array([color1_buscado[0] - tolerancia, color1_buscado[1] - tolerancia, color1_buscado[2] - tolerancia])
alto = np.array([color1_buscado[0] + tolerancia, color1_buscado[1] + tolerancia, color1_buscado[2] + tolerancia])
# Crear una máscara que identifique los píxeles dentro del rango del color buscado
mascara = cv2.inRange(imagen_hsv, bajo, alto)

# Contar los píxeles que coinciden con el color
numero_pixeles = cv2.countNonZero(mascara)

print(f"Número de píxeles con el color {color1_buscado}: {numero_pixeles}")