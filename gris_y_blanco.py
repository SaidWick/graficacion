
#+BEGIN_SRC python :results output

import cv2 as cv
img = cv.imread(r"C:\Users\wicki\OneDrive\Documentos\Trabajos Graficacion\phin.png",0)
cv.imshow('salida', img)
x, y =img.shape
for i in range(x):
    for j in range(y):
        if(img[i,j]>150):
            img[i,j]=255
        else:
            img[i,j]=0

cv.imshow('negativo',img) 
x, y =img.shape
for i in range(x):
    for j in range(y):
        if(img[i,j]<150):
            img[i,j]=255
        else:
            img[i,j]=0

cv.imshow('reverso',img)         
print(img.shape,x ,y)
cv.waitKey(0)
cv.destroyAllWindows()

#+END_SRC
#+RESULTS:
# (465,706) 465 706
