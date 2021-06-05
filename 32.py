from mcpi.minecraft import Minecraft
from time import sleep
mc = Minecraft.create()
while True:
    mc.executeCommand("time add 78")

