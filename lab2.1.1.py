from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

y = (255,255,0)
b = (0,0,0)
p = (255,102,178)

smile_face = [
    y,y,y,y,y,y,y,y,
    y,b,b,y,y,b,b,y,
    y,b,b,y,y,b,b,y,
    y,y,y,y,y,y,y,y,
    y,b,y,y,y,y,b,y,
    y,b,y,y,y,y,b,y,
    y,y,b,b,b,b,y,y,
    y,y,y,y,y,y,y,y
    ]

wink_face = [
    y,y,y,y,y,y,y,y,
    y,b,b,y,y,y,y,y,
    y,b,b,y,y,b,b,y,
    y,y,y,y,y,y,y,y,
    y,b,y,y,y,y,b,y,
    y,b,y,y,y,y,b,y,
    y,y,b,b,b,p,p,y,
    y,y,y,y,y,p,p,y
    ]

def blinky():
    while True:
        sense.set_pixels(smile_face)
        time.sleep(0.5)
        sense.set_pixels(wink_face)
        time.sleep(0.5)

blinky()
