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
wheight = 1.0

# example points
#xA = 1627.8
#yA = 1627.0
#zA = 285.8
#xB = 1561.90
#yB = 1596.5
#zB = 306.20
#h0 = 8

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
wall(1627.8,1627.0,285.8,  1561.90,1596.5,306.20, wheight, 8)
wall(1561.90,1596.5,306.20,  1558.5,1594.9,307.0, wheight, 8)
