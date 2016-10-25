import csv

"""
    I mainly followed Javier De La Rosa's excellent tutorial on creating a Chrome WebGL Globe.
    All credit goes to him for the methods of retrieving a country's geocoordinates and converting it to JSON.
    You can find it here - http://versae.blogs.cultureplex.ca/2011/11/07/creating-a-globe-of-data/
"""

lines = {}
lines[0] = csv.reader(open("2016LatLonCoL.csv", "rb"))
lines[1] = csv.reader(open("2015LatLonCoL.csv", "rb"))
lines[2] = csv.reader(open("2014LatLonCoL.csv", "rb"))
lines[3] = csv.reader(open("2013LatLonCoL.csv", "rb"))
lines[4] = csv.reader(open("2012LatLonCoL.csv", "rb"))
lines[5] = csv.reader(open("2011LatLonCoL.csv", "rb"))
lines[6] = csv.reader(open("2010LatLonCoL.csv", "rb"))

year = {}
year[0] = []
year[1] = []
year[2] = []
year[3] = []
year[4] = []
year[5] = []
year[6] = []

sums = {}
sums[0] = 35373.59
sums[1] = 31152.66
sums[2] = 34881.52
sums[3] = 27839.66
sums[4] = 20608.45
sums[5] = 8842.88
sums[6] = 16171.04



for x in range(7):
	for lat, lon, col, in lines[x]:
		year[x] += (lat, lon, str( float(col) / sums[x] ))
    

print """
[
["2016", [%s]],
["2015", [%s]],
["2014", [%s]],
["2013", [%s]],
["2012", [%s]],
["2011", [%s]],
["2010", [%s]]
""" % (",".join(year[0]),
       ",".join(year[1]),
       ",".join(year[2]),
       ",".join(year[3]),
       ",".join(year[4]),
       ",".join(year[5]),
       ",".join(year[6]))