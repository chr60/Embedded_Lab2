from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
temp_str = str(round(temp)) + " deg"

y = (255,255,0)
b = (0,0,0)

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

while True:
    for event in sense.stick.get_events():
        if event.direction == 'left' and event.action == 'pressed':
            sense.clear()
            sense.show_message(temp_str)
        elif event.direction == 'right' and event.action == 'pressed':
            sense.clear()
            sense.show_message("Hello")
        elif event.direction == 'up' and event.action == 'pressed':
            sense.clear()
            sense.clear((0,0,255))
            time.sleep(0.3)
            sense.clear((255,102,178))
            time.sleep(0.3)
        elif event.direction == 'down' and event.action == 'pressed':
            sense.clear()
            sense.show_letter("X", back_colour=[255,0,0])
            time.sleep(0.5)
        elif event.direction == 'middle' and event.action == 'pressed':
            sense.clear()
            sense.set_pixels(smile_face)
            time.sleep(0.5)

        sense.clear()
        
        
