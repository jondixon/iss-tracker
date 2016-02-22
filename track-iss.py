#!/usr/local/bin/python3.5

#This is a simple program that is used to print the 
# current azimuth and altitude of any NORAD tracked
# object given either latitude and longitude, or 
# maybe even a zip code, idk we'll see what happens

import math
import time
from datetime import datetime
import ephem
import sys
import urllib.request

NORAD = urllib.request.urlopen('https://www.celestrak.com/NORAD/elements/stations.txt')
with open('norad.txt', 'w+b') as f:
    f.write(NORAD.read())

 
degrees_per_radian = 180.0 / math.pi
 
home = ephem.Observer()
home.lon = sys.argv[1]   # +E
home.lat = sys.argv[2]      # +N
home.elevation = int(sys.argv[3]) # meters
 
iss = ephem.readtle('ISS',
    '1 25544U 98067A   16053.61773880  .00007242  00000-0  11608-3 0  9999', 
    '2 25544  51.6425 274.3549 0004199 154.0845 254.2150 15.54236294987003'
)
 
while True:
    home.date = datetime.utcnow()
    iss.compute(home)
    print('iss: altitude %4.2f deg, azimuth %5.2f deg' % (iss.alt * degrees_per_radian, iss.az * degrees_per_radian))
    time.sleep(.5)
