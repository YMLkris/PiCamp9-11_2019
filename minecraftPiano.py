from pythonosc import osc_message_builder
from pythonosc import udp_client
from time import sleep
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

sender = udp_client.SimpleUDPClient('127.0.0.1',4559)
def play_note(note):
    sender.send_message('/play_this', note)
    sleep(0.5)


while True:
    blockEvents = mc.events.pollBlockHits()
    for blockEvent in blockEvents:
        print(blockEvents)

    pos = mc.player.getPos()

    if int(pos.x) == 0 and int(pos.z) == 0 :
        play_note(60)

    if int(pos.x) == 1 and int(pos.z) == 0 :
        play_note(61)

    if int(pos.x) == 1 and int(pos.z) == -1 :
        play_note(62)

    if int(pos.x) == 2 and int(pos.z) == 0 :
        play_note(63)

    if int(pos.x) == 2 and int(pos.z) == -2 :
        play_note(64)

    sleep(1)