import random 
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
for i in range(1000):
    r=random.randrange(1,5)
    if r==1:
        mc.setBlocks(x,y,z,x+3,y,z,89)
        x=x+3
    elif r==2:
        mc.setBlocks(x,y,z,x-4,y,z,89)
        x=x-4
    elif r==3:
        mc.setBlocks(x,y,z,x,y,z+4,89)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-3,89)
        z=z-3
