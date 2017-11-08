from sense_hat import SenseHat
import time

sense = SenseHat()

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



def light_cols(num):
        if num == -1:
            i=0
            row = 7
            while row >=0:
                for col in range(8):
                    sense.set_pixel(row,col,colors[i])
                time.sleep(0.2)
                i += 1
                row -= 1
                sense.clear()
        else:
            i=0
            row = 0
            while row <= 7:
                for col in range(8):
                    sense.set_pixel(row,col,colors[i])
                time.sleep(0.2)
                i += 1
                row += 1
                sense.clear()

def light_rows(num):
        if num == -1:
            i=0
            row = 7
            while row >=0:
                for col in range(8):
                    sense.set_pixel(col,row,colors[i])
                time.sleep(0.2)
                i += 1
                row -= 1
                sense.clear()
        else:
            i=0
            row = 0
            while row <= 7:
                for col in range(8):
                    sense.set_pixel(col,row,colors[i])
                time.sleep(0.2)
                i += 1
                row += 1
                sense.clear()


while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        
        if x==0 and y==0:
            if z==1:
                sense.show_message("PI is up")
                sense.clear()
            else:
                print("The PI is upside-down")
        elif abs(x) >= abs(y):
            light_cols(x)
            sense.clear()
        elif abs(x) < abs(y):
            light_rows(y)
            sense.clear()






