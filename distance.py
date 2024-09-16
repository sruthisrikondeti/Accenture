'''Ques: The program is supposed to calculate the sum of  distance between three points from each other.

For
x1 = 1 y1 = 1
x2 = 2 y2 = 4
x3 = 3 y3 = 6

Distance is calculated as : sqrt(x2-x1)2 + (y2-y1)2'''
import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
x3=int(input())
y3=int(input())

def distance(x1,y1,x2,y2):
    dis=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return dis
dist_12 = distance(x1, y1, x2, y2)
dist_23 = distance(x2, y2, x3, y3)
dist_31 = distance(x3, y3, x1, y1)

print(round(dist_12+dist_23+dist_31))
