#Python 3.6.2
#script BigБро
#idea Zirum
#run this script with IDLE
# example result
# <spot h="85" z="119.1266" y="1546.7086" x="1613.4429"/>
#for \AC-Game\data\static_data\spawns\gather\New\location.xml

#example npc: giant Aquamarin 401103/ giant Rubin 401109/ giant Diamant 401110

import math

# Item size
iw = 1.5  #width
ih = 2		#height

#Wall height
wheight = 10.0

# example points
#xA = 1851.59
#yA = 1137.22
#zA = 444.00
#xB = 1897.32
#yB = 1133.2
#zB = 444.00
#h0 = 67

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
wall(1851.59,1137.22,444.00,  1897.32,1133.2,444.00, wheight, 67)
