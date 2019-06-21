# Write your code here :-)
from blinkt import set_pixel, show,set_brightness
from random import randint
from time import sleep
set_brightness(0.2)
while True:
    for pixel in range(8):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        set_pixel(pixel, r, g, b)
        show()
        sleep(0.1)