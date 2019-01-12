#Python 3.6.2
#script BigБро
#idea Zirum
#run this script with IDLE
# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\gather\New\location.xml

#for npc: giant Aquamarin 401103/ giant Rubin 401109/ giant Diamant 401110

import math

# Item width
iw = 1.0
#insert here your platform midpoint
x0 = 1639.0
y0 = 1630.0
z0 = 284.5
h0 = 85
# 5-6(radius) 15°(step)/6-7-8 12°/9-10 8°/10-11-12 7°/21-25 3°
for u in range (11,12): #radius from, to
  for i in range (0, 360, 7):  #7 --> step (see table above)
    x = (u)* iw * math.cos(i/180*3.1459) + x0
    y = (u)* iw * math.sin(i/180*3.1459) + y0
    z = z0; 		
    h = round(i/3)
    print ('<spot h="{:d}" x="{:.2f}" y="{:.2f}" z="{:.2f}"/>'.format(h, x, y, z))

