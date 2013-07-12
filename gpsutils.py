 
import gps

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
  report = session.next()
  if report['class'] == 'TPV':
    if hasattr(report, 'lat'):
      lat = report.lat
    if hasattr(report, 'lon'):
      lon = report.lon
    if hasattr(report, 'track'):
      heading = report.track
      
def getloc():
  loc = (lat, lon)
  return loc
  
def gethead():
  return heading