from blinkt import *
from random import randint
from time import sleep
from colorsys import *
set_brightness(.05)

p=0

while True:
    for i in range(0,255,int(255/8)):
        r,g,b = hsv_to_rgb(i/255,1,1)
        set_pixel(p,r*255,g*255,b*255)
        # print(r*255,g*255,b*255)
        p = p+1
        if p>7:
            p=0
            show()
            sleep(.1)


