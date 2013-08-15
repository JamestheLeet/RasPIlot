from nav import dist, direction, heading
from vehicle  import trottle, steer
import gps
from multiprocessing import Process
from string import strip, split
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
loc, speed = 0
throttle = 0
changedistance = 0.000002
path = open('path', 'r')
limit = 16
minspeed = 15

def gpsread():
  while True:
    try:
    report = session.next()
    if report['class'] == 'TPV':
      if hasattr(report, 'lat'):
	lat = report.lat
      if hasattr(report, 'lon'):
	lon = report.lon
      if hasattr(report, 'track'):
	track = report.track
      if hasattr(report, 'speed'):
	speed = report.speed * gps.MPS_TO_KPH
      loc = lat, lon
  except KeyError:
    pass
  except KeyboardInterrupt:
    quit()
  except StopIteration:
    session = None
    print "GPSD has terminated"
    
def gotoloc(destination):
  while repeat:
    distto = dist(loc, destination)
    repeat = 1
    if (distto > changedistance)
      steer = heading(loc, destination)
      steer = steer - track
      if (steer > 30)
	steer = 30
      if (steer < -30)
	steer = -30
      steer(steer)
      if speed > limit
	throttle = throttle - 1
      if speed < minspeed
	throttle = throttle + 1
      throttle(throttle)
    else if (distto < changedistance)
      repeat = 0
      return('done: ' + destination);
     
    
while True:
  dest = path.readline()
  dest = strip(dest)
  dest = split(dest, ':')
  gotoloc(dest)
  
    
if __name__ == '__main__':
  gpsproc = Process(target=gpsread)
  gpsproc.start()
  gpsproc.join()