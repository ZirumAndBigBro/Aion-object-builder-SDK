#Python 3.6.2
#script BigБро
#idea Zirum
#run this script with IDLE
# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\Npcs\New\location.xml

#for npc middle box 701016

import math

# Item size
iw = 0.9  #width 
ih = 0.9  #height 

#Wall height
wheight = 5.0

# example points
#xA = 1716.47
#yA = 1691.47
#zA = 100.00
#xB = 1734.11
#yB = 1679.80
#zB = 100.00
#h0 = 108

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
wall(1716.47,1691.47,100.00,  1734.11,1679.80,100.00, wheight, 108)
