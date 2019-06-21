from blinkt import *
from random import randint
from time import sleep
from colorsys import *

set_brightness(.05)

# an even cleaner version
smoothing = 32 # try 8 or 16
delay = 100
while True:
    for i in range(0,255,int(255/smoothing)): # for each color value
        for j in range(0,8): # for each pixel
            r,g,b = hsv_to_rgb(i/255 + j*(255/8),1,1)
            set_pixel(j,r*255,g*255,b*255)
            # print(r*255,g*255,b*255)
        show()
        time.sleep(1/delay)