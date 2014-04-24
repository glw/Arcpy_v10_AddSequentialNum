# Name: sorted_seq_numb.py
# Description: updates a field [MAP_NO2] within a sorted shapefile with a sequential number.
# Author: Garret Wais garret.wais@cookcountyil.gov

import arcpy

arcpy.env.overwriteOutput=True

#sort variables
input = "Y:/Projects/2013/13-13_GIS_Requests/18-CentennialMaps/CentennialMaps/Map_Side/Data/Dist_Wide_POI.shp"
output = "Y:/Projects/2013/13-13_GIS_Requests/18-CentennialMaps/CentennialMaps/Map_Side/Data/poi_sorted.shp" 

numbr = 1

#order features first by zone (asc), then by labelname (asc)
sortfields = [["FPDzone", "ASCENDING"], ["LabelName", "ASCENDING"]]
#sort
arcpy.Sort_management(input, output, sortfields)

#input for field number update
rows = arcpy.UpdateCursor(output)
	
#add the sequential numbers according to the sorted fields
for row in rows:
	row.MAP_NO2 = numbr
	rows.updateRow(row)
	numbr += 1

# Delete cursor and row objects
del row	
del rows
