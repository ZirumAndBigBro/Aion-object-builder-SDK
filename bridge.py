#Python 3.6.2
#run this script with IDLE
#script BigБро
#idea Zirum

# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#example npc 701025

import math

# Item size
iw = 1.0  #width
ih = 1.0  #height

#Wall height
wheight = 0.5

# example points
#xA = 1710.50
#yA = 1509.2
#zA = 70.5
#xB = 1631.0
#yB = 1641.27
#zB = 104.00
#h0 = 12

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
wall(1710.50,1509.2,70.5,  1631.0,1641.27,104.00, wheight, 12)
