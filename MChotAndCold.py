xT = None
yT = None
zT = None
found = None
Dx = None
Dy = None
Dz = None
TotalD = None


import random
import time
from blinkt import *
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.player.setPos(0, 15, 0)

x, y, z = mc.player.getPos()
xT = random.randint(-125,125)
yT = random.randint(-30,30)
zT = random.randint(-125,125)
mc.setBlock(xT, yT, zT, 57)
print(xT, yT, zT)
found = 0
while found == 0:
  x, y, z = mc.player.getPos()
  Dx = abs(xT-x)
  Dy = abs(yT-y)
  Dz = abs(zT-z)
  print(Dx, Dy, Dz)
  TotalD = Dx + Dy + Dz
  set_all(255 - TotalD, 0, TotalD)
  show()
  time.sleep(.2)
