#+BEGIN_SRC python
import cv2 as cv
import numpy as np

img = np.ones((500,500,3),dtype=np.uint8)*255
cv.rectangle(img,(500,500),(0,0),(68,246,57),500)
cv.rectangle(img,(500,50),(0,200),(246,137,57),200)
cv.circle(img,(100,100), 50, (14,237,255), -1 )
cv.ellipse(img,(250, 350), (100, 150), 0, 0, 360, (244, 208, 245), -1)
cv.circle(img, (250, 200), 70, (253, 161, 255), -1)
cv.circle(img, (210, 130), 20, (253, 161, 255), -1)
cv.circle(img, (290, 130), 20, (253, 161, 255), -1)
cv.circle(img, (230, 190), 15, (243, 230, 243), -1)
cv.circle(img, (270, 190), 15, (233, 230, 243), -1) 
cv.circle(img, (230, 190), 5, (0, 0, 0), -1)  
cv.circle(img, (270, 190), 5, (0, 0, 0), -1)  
cv.ellipse(img, (250, 230), (30, 20), 0, 0, 360, (255, 105, 180), -1)
cv.circle(img, (240, 230), 5, (0, 0, 0), -1)
cv.circle(img, (260, 230), 5, (0, 0, 0), -1) 
cv.ellipse(img, (250, 250), (30, 20), 0, 20, 160, (0, 0, 0), 2)
cv.rectangle(img, (200, 450), (220, 400), (254, 184, 255), -1)
cv.rectangle(img, (280, 450), (300, 400), (254, 184, 255), -1)
 
cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()

#+END_SRC