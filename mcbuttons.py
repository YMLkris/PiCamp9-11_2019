import time
import explorerhat as eh
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
current_state = 0
block = 0
#define state change
def changeState(channel, event):
    global current_state
    print(channel,event)
    if event == "press":
        if channel > 3:
            return(newState)
        else:
            current_state = channel
#main loop
while True:
    eh.touch.pressed(changeState)
    if (current_state == 1):
        block = 38
    elif (current_state == 2):
        block = 1
    else:
        block = 0
    print(current_state, block)
    pos = mc.player.getPos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x,y,z, block)
    time.sleep(.2)