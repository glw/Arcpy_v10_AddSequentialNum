# Name: sorted_seq_numb.py
# Description: updates a field [MAP_NO2] within a sorted shapefile with a sequential number.
# Author: Garret Wais garret.wais@cookcountyil.gov

import arcpy

arcpy.env.overwriteOutput=True

#Variables
input = "path/to/file"
output = "path/to/file" 
numbr = 1

#Order features. You can use several levels to order features. Replace "FieldName1" & "FieldName2" with field names in your file.
sortfields = [["FieldName1", "ASCENDING"], ["FieldName2", "ASCENDING"]]

#Sort
arcpy.Sort_management(input, output, sortfields)

#input for field number update
rows = arcpy.UpdateCursor(output)
	
#add the sequential numbers according to the sorted fields. Replace "FIELD" with the field that should recieve the number value.
for row in rows:
	row.FIELD = numbr
	rows.updateRow(row)
	numbr += 1

# Delete cursor and row objects
del row	
del rows
