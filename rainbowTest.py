from blinkt import *
from random import randint
from time import sleep
set_brightness(0.05)

p=0



def rainbow_cycle(wait):
    p=0
    for k in range(0,255,25):
        for j in range(0,255,25):
            for i in range(0,255,25):
                set_pixel(p,i,j,k)
                show()
                p = p+1
                if p>7:
                    p=0
                time.sleep(wait)


def rCycl(wait):
    lights = 8
    for j in range(lights):
        for i in range(lights):
            b = ((i+j)/8)*255
            set_pixel(i,b ,b+(255/3),b+2*(255/3))
        show()
        time.sleep(wait)
    show()
#rainbow_cycle(.001)
rCycl(1)