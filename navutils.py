from math import sqrt, acos, pow, degrees

def getdist(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  dist = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))
  return dist
  
def getdir(a, b, c):
  ang = acos((pow(a, 2) + pow(b, 2) - pow(c, 2))/(2 * a * b))
  retang = degrees(ang)
  return(retang)

def getheading(curpos, desired):
  north1, north2 = curpos
  north = (north1, 90)
  a = getdist(curpos, north)
  b = getdist(curpos, desired)
  c = getdist(north, desired)
  heading = getdir(a, b, c)
  return(heading)