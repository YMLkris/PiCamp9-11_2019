from time import sleep
from blinkt import *
from pythonosc import osc_message_builder
from pythonosc import udp_client

sender = udp_client.SimpleUDPClient('127.0.0.1', 4559)
set_all(255,0,0)
show()
while True:
    sender.send_message('/play_this', 60)
    sleep(.1)
    set_brightness(1)
    for i in range(5):
        set_brightness((.6-i/10))
        show()
        sleep(.1)
