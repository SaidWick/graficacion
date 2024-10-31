import cv2
import numpy as np

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Vértices de la pirámide en coordenadas 3D
vertices = np.array([
    [-1, -1, -1],  # Vértice de la base (izquierda, atrás)
    [1, -1, -1],   # Vértice de la base (derecha, atrás)
    [1, -1, 1],    # Vértice de la base (derecha, adelante)
    [-1, -1, 1],   # Vértice de la base (izquierda, adelante)
    [0, 1, 0]      # Vértice superior (pico de la pirámide)
])

# Conexiones de los vértices para formar las aristas de la pirámide
edges = [
    (0, 1),(1, 2), (2, 3), (3, 0),  # Aristas de la base
    (0, 4), (1, 4), (2, 4), (3, 4)   # Aristas que conectan la base con el vértice superior
]

def project_isometric(vertex):
    """Función para proyectar un punto 3D a 2D con proyección isométrica"""
    x, y, z = vertex
    x2D = x - z
    y2D = (x + 2 * y + z) / 2
    return int(x2D * 100 + WIDTH / 2), int(-y2D * 100 + HEIGHT / 2)

# Crear ventana
cv2.namedWindow("Piramide Isométrica")

while True:
    # Crear imagen negra para el fondo
    frame = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    # Dibujar aristas de la pirámide
    for edge in edges:
        pt1 = project_isometric(vertices[edge[0]])
        pt2 = project_isometric(vertices[edge[1]])
        cv2.line(frame, pt1, pt2, (255, 255, 255), 2)

    # Mostrar imagen
    cv2.imshow("Piramide Isométrica", frame)

    # Salir si se presiona 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
