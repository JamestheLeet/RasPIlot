from math import sqrt, acos, degrees

def dist(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
  return(dist)
  
def direction(a, b, c):
  ang = acos((a**2 + b**2 - c**2)/(2 * a * b))
  ang = degrees(ang)
  return(ang)

def heading(curpos, desired):
  north1, north2 = curpos
  north = (north1, 90)
  a = dist(curpos, north)
  b = dist(curpos, desired)
  c = dist(north, desired)
  heading = direction(a, b, c)
  heading = round(heading)
  return(heading)