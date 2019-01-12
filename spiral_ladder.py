#Python 3.6.2
#script BigБро
#idea Zirum
#run this script with IDLE
# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#for npc 701025

import math

# Item size
iw = 4.0 #width
k = 5 #slope
#insert here your spiral midpoint
x0 = 1566.0
y0 = 1599.0
z0 = 125.0
h0 = 85
#0-1 (radius) 45°(step)/1-2 20°/2-3 12°/3-4 8°/4-5 6°/5-6 5°/6-7 4°/7-8 4°/8-10 3°/10-14 2°/ 14-25-50 1°
for u in range (1,2): #radius from, to
  for i in range (0, 360, 20):  #20° --> step (see table above)
    x = (u)* iw * math.cos(i/180*3.1459) + x0
    y = (u)* iw * math.sin(i/180*3.1459) + y0
    z = (z0-k)+(u+i/360)*k #spiral	
    h = round(i/3)
    print ('<spot h="{:d}" x="{:.2f}" y="{:.2f}" z="{:.2f}"/>'.format(h, x, y, z))

