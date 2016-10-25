from geopy import Nominatim
import xlrd
import sys

# take in excel file name, parse all entries in column 0: should be cities
sh = xlrd.open_workbook( sys.argv[1] ).sheet_by_index(0)
#2016CoL
countries = open(sys.argv[1][:7] + "CountryLonLat.txt", 'w')
try:
    for row in range(sh.nrows):
        countries.write( str(sh.cell(row, 0).value)+"\n" )
finally:
    countries.close()
