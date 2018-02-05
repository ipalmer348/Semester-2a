from mcpi.minecraft import Minecraft
mc = minecraft.create()

import time

while True:
    Hits = mc.events.pollBlockHits()
    iflen(hits) > 0:
        hit = hits[0]
        hitX, hitY, hitZ = hit.pos.x, hit.pos.z
        block = mc.getBlock(hitX, hitY, hitZ)
        blocks.append(block)

        time.sleep(0.2)

raceTimes = {'Katy': 26, 'Alex': 30, 'Richard': 19}
person{'name': 'David', 'age' : 42, 'favoriteAnimal': 'Snake',
