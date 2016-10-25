from geopy import Nominatim
import xlrd, sys

"""
    I mainly followed Javier De La Rosa's excellent tutorial on creating a Chrome WebGL Globe.
    All credit goes to him for the methods of retrieving a country's geocoordinates and converting it to JSON.
    You can find it here - http://versae.blogs.cultureplex.ca/2011/11/07/creating-a-globe-of-data/
"""

# take in excel file name, parse all entries in column 0: should be cities
xl = xlrd.open_workbook( sys.argv[1] ).sheet_by_index(0)

cities = open(sys.argv[1][:7] + "CityLonLat.txt", 'w')
g = Nominatim()

try:
    for row in range(xl.nrows):
    	# retrieve the city name, country name
    	c = str(xl.cell(row, 0).value)

    	# only want city name
    	commaIndex = c.find(",")
    	if commaIndex != -1:
    		c = c[:commaIndex]

    	# retrieve its latitude and longitude
    	loc = g.geocode(c)
    	if loc == None:
            # print out names that did not retrieve a geocode and fill with dummy text. Manually search their geocode and replace later
    		print c
    		cities.write( c + ", 0.0, 0.0\n" )
    	else:
    	   cities.write( c + ", " + str(loc.latitude) + ", " + str(loc.longitude) + "\n" )
        
finally:
    cities.close()
