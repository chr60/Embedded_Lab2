from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

off = (0,0,0)
purple = (153,0,153)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
orange = (255,128,0)
pink = (255,102,178)
yellow = (255,255,0)
white = (255,255,255)
colors = [pink,yellow,blue,red,green,orange,purple,white]

while True:
    i = 0
    size = 7
    x = 0
    y = 0
    while x <= 7 and y <= 7:
        if x == 0 and y== 0:
            sense.set_pixel(x,y,colors[i])
        elif x != 0 and y != 0:
            j = 0
            k = 0
            while j <= x:
                while k <= y:
                    if j+k==x:
                        sense.set_pixel(j,k,colors[i])
                        sense.set_pixel(k,j,colors[i])
                    k += 1
                j += 1
                k = 0
                    
        time.sleep(0.2)
        x += 1
        y += 1
        i += 1
        sense.clear()
    i = 0
    while x <= 14 and y <= 14:
        if x != 0 and y != 0:
            j = 0
            k = 0
            while j <= 7:
                while k <= 7:
                    if j+k==x:
                        sense.set_pixel(j,k,colors[i])
                        sense.set_pixel(k,j,colors[i])
                    k += 1
                j += 1
                k = 0
            time.sleep(0.2)
            x += 1
            y += 1
            i += 1
            sense.clear()
