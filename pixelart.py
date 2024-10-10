import numpy as np
import cv2

width, height = 500, 340

pixel_matrix = np.zeros((height, width, 3), dtype=np.uint8)

for y in range(height):
    for x in range(width):
        # Fila 1
        if y >= 0 and y <= 10:
            if (x >= 0 and x <= 100) or (x >= 130 and x <= 260) or (x >= 290 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 130) or (x >= 280 and x <= 290):
                pixel_matrix[y, x] = [0, 0, 0]

        # Fila 2
        if y >= 10 and y <= 20:
            if (x >= 0 and x <= 90) or (x >= 140 and x <= 160) or (x >= 230 and x <= 250) or (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 130) or (x >= 260 and x <= 290):
                pixel_matrix[y, x] = [150, 150, 150]

        # Fila 3
        if y >= 20 and y <= 30:
            if (x >= 0 and x <= 90) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 140 and x <= 160) or (x >= 230 and x <= 250):
                pixel_matrix[y, x] = [0, 0, 0]
            if (x >= 100 and x <= 140) or(x >= 160 and x <= 230) or (x >= 250 and x <= 290):
                pixel_matrix[y, x] = [150, 150, 150]
        
        # Fila 4
        if y >= 30 and y <= 40:
            if (x >= 0 and x <= 90) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 130 and x <= 140) or (x >= 240 and x <= 250):
                pixel_matrix[y, x] = [0, 0, 0]
            if (x >= 100 and x <= 130) or(x >= 150 and x <= 240) or (x >= 260 and x <= 290):
                pixel_matrix[y, x] = [150, 150, 150]
        
        # Fila 5
        if y >= 40 and y <= 50:
            if (x >= 0 and x <= 90) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 130 and x <= 140) or (x >= 240 and x <= 250):
                pixel_matrix[y, x] = [0, 0, 0]
            if (x >= 100 and x <= 120) or(x >= 140 and x <= 250) or (x >= 270 and x <= 290):
                pixel_matrix[y, x] = [150, 150, 150]
        
        # Fila 6
        if y >= 50 and y <= 60:
            if (x >= 0 and x <= 90) or  (x >= 185 and x <= 195) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 120 and x <= 130) or (x >= 250 and x <= 260):
                pixel_matrix[y, x] = [0, 0, 0]
            if (x >= 100 and x <= 110) or(x >= 130 and x <= 185)or(x >= 195 and x <=260) or (x >= 280 and x <= 290):
                pixel_matrix[y, x] = [150, 150, 150]
        
        # Fila 7
        if y >= 60 and y <= 70:
            if (x >= 0 and x <= 90) or  (x >= 180 and x <= 200) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 90 and x <= 110) or (x >= 280 and x <= 300):
                pixel_matrix[y, x] = [0, 0, 0]
            if  (x >= 110 and x <= 180)or(x >= 200 and x <=280) :
                pixel_matrix[y, x] = [150, 150, 150]
        
        # Fila 8
        if y >= 70 and y <= 80:
            if (x >= 0 and x <= 90) or  (x >= 175 and x <= 205) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 90 and x <= 100) or (x >= 290 and x <= 300):
                pixel_matrix[y, x] = [0, 0, 0]
            if  (x >= 100 and x <= 175)or(x >= 205 and x <=290) :
                pixel_matrix[y, x] = [150, 150, 150]
        
        # Fila 9
        if y >= 80 and y <= 90:
            if (x >= 0 and x <= 90) or  (x >= 170 and x <= 210) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 90 and x <= 100) or (x >= 290 and x <= 300):
                pixel_matrix[y, x] = [0, 0, 0]
            if  (x >= 100 and x <= 170)or(x >= 210 and x <=290) :
                pixel_matrix[y, x] = [150, 150, 150]

        # Fila 10
        if y >= 90 and y <= 100:
            if (x >= 0 and x <= 80) or  (x >= 170 and x <= 210) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 80 and x <= 90) or (x >= 150 and x <= 170) or (x >= 220 and x <= 230) or (x >= 290 and x <= 300):
                pixel_matrix[y, x] = [0, 0, 0]
            if  (x >= 90 and x <= 150)or (x >= 210 and x <= 220) or(x >= 230 and x <=290) :
                pixel_matrix[y, x] = [150, 150, 150]
        # Fila 11
        if y >= 100 and y <= 110:
            if (x >= 0 and x <= 80)or  (x >= 160 and x <= 170) or  (x >= 180 and x <= 210) or  (x >= 220 and x <= 230) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 80 and x <= 90) or (x >= 150 and x <= 160) or (x >= 170 and x <= 180) or (x >= 210 and x <= 220) or (x >= 230 and x <= 240) or (x >= 290 and x <= 300):
                pixel_matrix[y, x] = [0, 0, 0]
            if  (x >= 90 and x <= 150) or(x >= 240 and x <=290) :
                pixel_matrix[y, x] = [150, 150, 150]
        # Fila 12
        if y >= 110 and y <= 120:
            if (x >= 0 and x <= 80) or(x >= 90 and x <= 150) or (x >= 180 and x <= 210) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 80 and x <= 90) or (x >= 150 and x <= 180) or  (x >= 210 and x <= 240) or  (x >= 290 and x <= 300):
                pixel_matrix[y, x] = [0, 0, 0]
            if (x >= 240 and x <=290) :
                pixel_matrix[y, x] = [150, 150, 150]
        
        # Fila 13
        if y >= 120 and y <= 130:
            if (x >= 0 and x <= 80) or(x >= 90 and x <= 150) or (x >= 180 and x <= 210) or  (x >= 240 and x <= 290) or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 80 and x <= 90) or (x >= 150 and x <= 180) or (x >= 190 and x <= 200) or  (x >= 210 and x <= 240) or  (x >= 290 and x <= 300) or (x >= 320 and x <= 340):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 14
        if y >= 130 and y <= 140:
            if (x >= 0 and x <= 90) or(x >= 100 and x <= 280) or (x >= 290 and x <= 310)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 90 and x <= 100)  or  (x >= 280 and x <= 290) or (x >= 310 and x <= 320) or (x >= 340 and x <= 350):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 15
        if y >= 140 and y <= 150:
            if (x >= 0 and x <= 100) or(x >= 110 and x <= 280) or (x >= 290 and x <= 310)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 110)  or  (x >= 280 and x <= 290) or (x >= 310 and x <= 320) or (x >= 350 and x <= 360):
                pixel_matrix[y, x] = [0, 0, 0]
        # Fila 16
        if y >= 150 and y <= 160:
            if (x >= 0 and x <= 110) or(x >= 130 and x <= 260) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 110 and x <= 130)  or  (x >= 260 and x <= 280) or (x >= 300 and x <= 310) or (x >= 340 and x <= 350):
                pixel_matrix[y, x] = [0, 0, 0]
        # Fila 17
        if y >= 160 and y <= 170:
            if (x >= 0 and x <= 130) or(x >= 260 and x <= 300) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 130 and x <= 260)  or (x >= 300 and x <= 310) or (x >= 330 and x <= 340):
                pixel_matrix[y, x] = [0, 0, 0]
        # Fila 18
        if y >= 170 and y <= 180:
            if (x >= 0 and x <= 140) or(x >= 150 and x <= 250) or(x >= 260 and x <= 310) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 140 and x <= 150) or (x >= 250 and x <= 260) or (x >= 310 and x <= 320) or (x >= 340 and x <= 350):
                pixel_matrix[y, x] = [0, 0, 0]
        # Fila 19
        if y >= 180 and y <= 190:
            if (x >= 0 and x <= 130) or(x >= 140 and x <= 260) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 130 and x <= 140) or (x >= 260 and x <= 270) or (x >= 320 and x <= 330) or (x >= 350 and x <= 360):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 20
        if y >= 190 and y <= 200:
            if (x >= 0 and x <= 130) or(x >= 140 and x <= 270) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 130 and x <= 140) or (x >= 270 and x <= 280) or (x >= 320 and x <= 330) or (x >= 350 and x <= 360):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 21
        if y >= 200 and y <= 210:
            if (x >= 0 and x <= 120) or(x >= 140 and x <= 280) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 120 and x <= 140) or (x >= 280 and x <= 290) or (x >= 320 and x <= 330) or (x >= 350 and x <= 360):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 22
        if y >= 210 and y <= 220:
            if (x >= 0 and x <= 110) or(x >= 130 and x <= 290) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 110 and x <= 130) or (x >= 290 and x <= 300) or (x >= 320 and x <= 330) or (x >= 350 and x <= 360):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 23
        if y >= 220 and y <= 230:
            if (x >= 0 and x <= 100) or(x >= 120 and x <= 260)or(x >= 270 and x <= 290) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 120) or (x >= 260 and x <= 270) or (x >= 290 and x <= 310) or (x >= 320 and x <= 330) or (x >= 350 and x <= 360):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 24
        if y >= 230 and y <= 240:
            if (x >= 0 and x <= 100) or(x >= 110 and x <= 250)or(x >= 260 and x <= 310) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 110) or (x >= 250 and x <= 260) or (x >= 310 and x <= 320)  or (x >= 350 and x <= 360):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 25
        if y >= 240 and y <= 250:
            if (x >= 0 and x <= 100) or(x >= 110 and x <= 240)or(x >= 250 and x <= 310) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 110) or (x >= 240 and x <= 250) or (x >= 310 and x <= 320)  or (x >= 340 and x <= 350):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 26
        if y >= 250 and y <= 260:
            if (x >= 0 and x <= 100) or(x >= 110 and x <= 150) or (x >= 160 and x <= 190) or(x >= 200 and x <= 240) or(x >= 250 and x <= 310) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 110) or (x >= 150 and x <= 160) or (x >= 190 and x <= 200) or (x >= 240 and x <= 250) or (x >= 310 and x <= 320)  or (x >= 330 and x <= 340):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 27
        if y >= 260 and y <= 270:
            if (x >= 0 and x <= 100) or(x >= 110 and x <= 150) or (x >= 160 and x <= 190) or(x >= 200 and x <= 240) or(x >= 250 and x <= 310) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 110) or (x >= 150 and x <= 160) or (x >= 190 and x <= 200) or (x >= 240 and x <= 250) or (x >= 310 and x <= 320)  or (x >= 320 and x <= 330):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 28
        if y >= 270 and y <= 280:
            if (x >= 0 and x <= 110) or(x >= 130 and x <= 150) or (x >= 160 and x <= 190) or(x >= 200 and x <= 250) or(x >= 270 and x <= 310) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 110 and x <= 130) or (x >= 150 and x <= 160) or (x >= 190 and x <= 200) or (x >= 250 and x <= 270) or (x >= 310 and x <= 320):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 29
        if y >= 280 and y <= 290:
            if (x >= 0 and x <= 100) or(x >= 110 and x <= 150) or (x >= 160 and x <= 190) or(x >= 200 and x <= 250) or(x >= 260 and x <= 300) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 110) or (x >= 150 and x <= 160) or (x >= 190 and x <= 200) or (x >= 250 and x <= 260) or (x >= 300 and x <= 310):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 30
        if y >= 290 and y <= 300:
            if (x >= 0 and x <= 100) or(x >= 110 and x <= 150) or (x >= 160 and x <= 190) or(x >= 200 and x <= 250) or(x >= 260 and x <= 300) or(x >= 270 and x <= 320) or (x >= 280 and x <= 300)  or  (x >= 310 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 100 and x <= 110) or (x >= 150 and x <= 160) or (x >= 190 and x <= 200) or (x >= 250 and x <= 260) or (x >= 300 and x <= 310):
                pixel_matrix[y, x] = [0, 0, 0]
        
        # Fila 31
        if y >= 300 and y <= 310:
            if (x >= 0 and x <= 110)   or  (x >= 300 and x <= 500):
                pixel_matrix[y, x] = [255, 255, 255]
            if (x >= 110 and x <= 300):
                pixel_matrix[y, x] = [0, 0, 0]
        # Fila 32 a 34
        if y >= 310 and y <= 340:
            if (x >= 0 and x <= 500):
                pixel_matrix[y, x] = [150, 150, 150]
            

            
            
        
cv2.imshow('Pixel Art', pixel_matrix)
cv2.waitKey(0)
cv2.destroyAllWindows()
        