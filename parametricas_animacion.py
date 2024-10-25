import numpy as np
import cv2

def generar_punto_elipse(a, b, t, centro):
    x = int(a * np.cos(t) + centro[0])  
    y = int(b * np.sin(t) + centro[1])
    return (x, y)

# Dimensiones de la imagen
img_width, img_height = 600, 600

# Crear una imagen en blanco
imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)

# Parámetros del sol
a_sol = 50
b_sol = 50
centro_sol = (300, 300)

# Parámetros de los planetas
param_planetas = [
    {'a': 100, 'b': 50, 'color': (0, 255, 0)},  # Planeta 1
    {'a': 150, 'b': 70, 'color': (203, 33, 207)},  # Planeta 2
    {'a': 200, 'b': 90, 'color': (104, 231, 27)},  # Planeta 3
    {'a': 250, 'b': 110, 'color': (231, 209, 27)},  # Planeta 4
    {'a': 300, 'b': 130, 'color': (231, 27, 76)},  # Planeta 5
    {'a': 350, 'b': 150, 'color': (203, 33, 207)},  # Planeta 6
    {'a': 400, 'b': 170, 'color': (231, 27, 197)},  # Planeta 7
    {'a': 450, 'b': 190, 'color': (67, 27, 231)},  # Planeta 8
   
]

# Crear los valores del parámetro t para la animación
num_puntos = 1000
t_vals = np.linspace(0, 2 * np.pi, num_puntos)

# Bucle de animación
for t in t_vals:
    # Crear una nueva imagen en blanco en cada iteración
    imagen = np.zeros((img_height, img_width, 3), dtype=np.uint8)
    
    # Dibujar el sol en el centro
    cv2.circle(imagen, centro_sol, radius=15, color=(0, 247, 255), thickness=-1)
    
    # Dibujar órbitas de planetas (opcional)
    for param in param_planetas:
        for t_tray in t_vals:
            pt_tray = generar_punto_elipse(param['a'], param['b'], t_tray, centro_sol)
            cv2.circle(imagen, pt_tray, radius=1, color=(100, 100, 100), thickness=-1)
    
    # Dibujar planetas en órbita
    for idx, param in enumerate(param_planetas):
        punto_planeta = generar_punto_elipse(param['a'], param['b'], t, centro_sol)
        cv2.circle(imagen, punto_planeta, radius=5, color=param['color'], thickness=-1)
    
    # Mostrar la imagen con los planetas en movimiento
    cv2.imshow('Sistema Solar', imagen)
    
    # Controlar la velocidad de la animación (en milisegundos)
    cv2.waitKey(10)

# Cerrar la ventana después de la animación
cv2.destroyAllWindows()