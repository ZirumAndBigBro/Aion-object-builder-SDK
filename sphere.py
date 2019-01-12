#Python 3.6.2
#run this script with IDLE
#script BigБро
#idea Zirum

# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\gather\New\location.xml

#example npc: Aquamarin 400314 / Rubin 400317

import math
#insert here your sphere midpoint
radius = 9.0
x0 = 1566.0
y0 = 1599.0
z0 = 130.0
h0 = 85

for u in range (0,90,12): #12 --> step vertical
  for i in range (0, 360, 12): #12 --> step horizontal
    x = radius * math.sin(i/180*3.1459)*math.cos(u/180*3.1459) + x0
    y = radius * math.cos(i/180*3.1459)*math.cos(u/180*3.1459) + y0
    z = z0 + radius*math.sin(u/180*3.1459)
    z2= z0 - radius*math.sin(u/180*3.1459)
    h = round(i/3)
    print ('<spot h="{:d}" x="{:.4f}" y="{:.4f}" z="{:.4f}"/>'.format(h, x, y, z)) # upper half
    print ('<spot h="{:d}" x="{:.4f}" y="{:.4f}" z="{:.4f}"/>'.format(h, x, y, z2)) # bottom half
