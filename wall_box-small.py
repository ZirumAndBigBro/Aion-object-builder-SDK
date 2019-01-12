#Python 3.6.2
#script BigБро
#idea Zirum
#run this script with IDLE
# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#for npc small box 700321

import math

# Item size
iw = 0.5  #width
ih = 0.5  #height

#Wall height
wheight = 4.0

# Ground points
#xA = 1747.0
#yA = 1631.0
#zA = 103.0
#xB = 1750.0
#yB = 1631.0
#zB = 103.00
#h0 = 0

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
wall(1747.0,1631.0,103.0,  1750.0,1631.0,103.00, wheight, 0)
wall(1746.5,1631.0,103.0,  1744.54,1631.0,103.00, wheight, 0)
wall(1747.0,1631.5,103.0,  1747.0,1634.0,103.00, wheight, 0)
wall(1747.0,1630.5,103.0,  1747.0,1628.0,103.00, wheight, 0)

