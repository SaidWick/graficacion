import numpy as np
import cv2 as cv

# Definir los parámetros iniciales
width, height = 1000, 1000  # Ampliar la ventana para ver toda la figura
img = np.ones((height, width, 3), dtype=np.uint8)*255

# Parámetros de la espiral logarítmica
a, b = 1, 0.1  # Ajustar los valores de a y b para la espiral logarítmica
theta_increment = 0.05  # Incremento del ángulo
max_theta = 2 * np.pi  # Un ciclo completo

# Centro de la imagen
center_x, center_y = width // 2, height // 2

theta = 0  # Ángulo inicial

while True:  # Bucle infinito
    # Limpiar la imagen
    img = np.ones((width, height, 3), dtype=np.uint8) * 255
    
    # Dibujar la curva completa desde 0 hasta theta
    for t in np.arange(0, theta, theta_increment):
        # Calcular las coordenadas paramétricas (x, y) para la espiral logarítmica
        r = a * np.exp(b * t)  # Definir r correctamente
        x = int(center_x + r * np.cos(t))
        y = int(center_y + r * np.sin(t))
        
        # Dibujar un círculo en la posición calculada
        cv.circle(img, (x, y), 2, (0, 234, 0), 2)  # Color verde
        cv.circle(img, (x-2, y-2), 2, (0, 0, 0), 2)  # Borde negro

    # Mostrar la imagen
    cv.imshow("Parametric Animation", img)
    
    # Incrementar el ángulo
    theta += theta_increment
    
    # Pausar para ver la animación
    if cv.waitKey(1) & 0xFF == 27:  # Esperar 30ms, salir con 'ESC'
        break

# Cerrar la ventana al finalizar
cv.destroyAllWindows()