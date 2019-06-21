x = None
y = None
z = None


import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 10
y = 20
z = 12
mc.player.setPos(x, y, z)

while True:
  x, y, z = mc.player.getPos()
  mc.setBlock(x, y, z, 35.1)
  time.sleep(.2)
