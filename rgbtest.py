from blinkt import *
from time import sleep
from colorsys import *
set_brightness(.05)

p=0

while True:
    for i in range(0,255,5):
        r,g,b = hsv_to_rgb(i/255,1,1)
        set_pixel(p,r*255,g*255,b*255)
        show()
        print(r*255,g*255,b*255)
        sleep(.05)
        p = p+1
        if p>7:
            p=0
