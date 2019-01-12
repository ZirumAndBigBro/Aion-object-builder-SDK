#Python 3.6.2
#script BigБро
#idea Zirum
#run this script with IDLE
# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\gather\New\location.xml

#example npc: Aquamarin 400314 / Rubin 400317

import math

# Item size
iw = 0.5  #width
ih = 0.7  #height

#Wall height
wheight = 5.0

# example points
#xA = 1574.03
#yA = 1604.85
#zA = 121.00
#xB = 1640.68
#yB = 1675.37
#zB = 115.85
#h0 = 77

def wall(xA,yA,zA,xB,yB,zB,wheight,h0):
  LAB = math.sqrt((xB-xA)*(xB-xA) + (yB-yA)*(yB-yA) + (zB-zA)*(zB-zA))
  iCount = round(LAB / iw) + 1
  hCount = round(wheight / ih) + 1

  for h in range (0, hCount):
    for i in range (0, iCount):
       x = xA + (xB-xA)/iCount * i
       y = yA + (yB-yA)/iCount * i
       z = zA + (zB-zA)/iCount * i + ih*h
       print ('<spot h="{:d}" x="{:.1f}" y="{:.1f}" z="{:.1f}"/>'.format(h0, x, y, z))

#insert here your Start and End points
#wall(Start point x,y,z, End point x,y,z, wall height, direction)
#when many points, use many wall lines:
#wall...
#wall...
#wall...
wall(1574.03,1604.85,121.00,  1640.68,1675.37,115.85, wheight, 77)
