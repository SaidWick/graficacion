#+BEGIN_SRC python
import cv2 as cv
import numpy as np

img =cv.imread(r"C:\Users\wicki\OneDrive\Documentos\Trabajos Graficacion\mona.jpeg",0)
x, y =img.shape
img2=np.zeros((x*2,y*2),dtype=np.uint8)
for i in range(x):
    for j in range(y):
        img2[int (i*0.1),int(j*0.1)]=img[i, j]

cv.imshow('img',img)        
cv.imshow('img2',img2) 

cv.waitKey()
cv.detroyAllWindows()

#+END_SRC