import csv, math

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

maxes = {}
maxes[0] = 147.95
maxes[1] = 163.55
maxes[2] = 157.47
maxes[3] = 189.23
maxes[4] = 188.91
maxes[5] = 149.26
maxes[6] = 169.2

mins = {}
mins[0] = 20.06
mins[1] = 20.81
mins[2] = 21.17
mins[3] = 28.35
mins[4] = 30.2
mins[5] = 28.48
mins[6] = 29.82



for x in range(7):
	for lat, lon, col, in lines[x]:
		year[x] += ( lat, lon, str( (float(col) - mins[x]) / (maxes[x] - mins[x]) ))
    

print """
[
["2016", [%s]],
["2015", [%s]],
["2014", [%s]],
["2013", [%s]],
["2012", [%s]],
["2011", [%s]],
["2010", [%s]]
]
""" % (",".join(year[0]),
       ",".join(year[1]),
       ",".join(year[2]),
       ",".join(year[3]),
       ",".join(year[4]),
       ",".join(year[5]),
       ",".join(year[6]))