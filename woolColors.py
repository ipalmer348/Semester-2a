def getWoolState(color):
 """ Takes a color as a string and returns the wool block state for
 that color """
u if color == "pink":
 blockState = 6
woolColors.py
Functions Give You Superpowers 159
 elif color == "blue":
 blockState = 7
wooldColors.py

v colorString = input("Enter a block color: ")
state = getWoolState(colorString)
w pos = mc.player.getTilePos()
mc.setBlock(pos.x, pos,y, pos.z, 35, state)
