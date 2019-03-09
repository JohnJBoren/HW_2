import random
import numpy

lat = [random.gauss(60, 10) for x in range(100)]
lon = [random.randrange(100)/10.0 - 150 for x in range(100)]

lat_mean = 0
lon_mean = 0

for x in lat:
    lat_mean += x

for y in lon:
    lon_mean += y

lat_mean = lat_mean/100
lon_mean = lon_mean/100

print "The mean latitude is %f" % lat_mean

print "The mean longitude is %f" % lon_mean