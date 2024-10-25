#+BEGIN_SRC python

import cv2 as cv
cap = cv.VideoCapture(0)
while(True):
    ret,img = cap.read()
    if ret:
        cv.imshow('video', img)
        img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        cv.imshow('video2',img2)
        cv.imshow('Gray',gray)

        k=cv.waitKey(1)& 0xFF
        if k == 27:
            break
    else:
         break

cap.release()
cv.destroyAllWindows()

#+END_SRC