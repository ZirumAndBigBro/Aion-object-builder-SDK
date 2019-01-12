#Python 3.6.2
#script BigБро
#idea Zirum
#run this script with IDLE
# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#for npc: Lila Plate 831125

import math

# Item width
iw = 2.0
#insert here your platform midpoint
x0 = 1639.0
y0 = 1630.0
z0 = 284.0
h0 = 85
#0-1(radius) 90°(step)//2-3 45°/3-4 30°/4-5 22°/5-6 20°/6-7 4°/7-8 4°/8-10 3°/10-14 2°/ 14-25-50 1°
for u in range (5,6): #radius from, to
  for i in range (0, 360, 20):  #20° --> step (see table above)
    x = (u)* iw * math.cos(i/180*3.1459) + x0
    y = (u)* iw * math.sin(i/180*3.1459) + y0
    z = z0;   
    h = round(i/3)
    print ('<spot h="{:d}" x="{:.2f}" y="{:.2f}" z="{:.2f}"/>'.format(h, x, y, z))

