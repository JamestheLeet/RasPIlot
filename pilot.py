import gpsutils
from multiprocessing import Process

if __name__ == '__main__':
    p = Process(target=gpsread, args=())
    p.start()
    p.join()
    location = gpsutils.getloc()
    head = gpsutils.gethead()