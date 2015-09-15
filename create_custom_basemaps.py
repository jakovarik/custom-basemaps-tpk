# ---------------------------------------------------------------------------
# tilepackage.py
# Created by Jacqueline Kovarik, 2015
# Description: generates tile packages based on an input feature class, for use
# in Collector for ArcGIS and other mobile applications. Please read documentation
# for a comprehensive explanation of tool input requirements.
# ---------------------------------------------------------------------------

# Import modules
import os, arcpy, os.path
from arcpy import env

# Read the parameter values:
# 1: Input feature class
# 2: Field Name
# 3: Output location
# 4: Buffer Size
# 5: Buffer output location


fc_path = arcpy.GetParameterAsText(0)
field_name = arcpy.GetParameterAsText(1)
workspace = arcpy.GetParameterAsText(2)
buffer = arcpy.GetParameterAsText(3)

bufferOutput = workspace + "/buffer.shp"
arcpy.env.addOutputsToMap = False
mxd = arcpy.mapping.MapDocument("CURRENT")  #r'c:\temp\test.mxd")

# Set environment settings to local drive - overwrite existing
env.overwriteOutput = True
#mxdLoc = arcpy.mapping.MapDocument("CURRENT")


#buffer input fc
arcpy.Buffer_analysis(fc_path, bufferOutput, buffer, "FULL", "ROUND")
arcpy.AddMessage("Completed buffering the input feature class.")
arcpy.AddMessage("*****************************************")

#add buffered input layer to mxd
df = arcpy.mapping.ListDataFrames(mxd)[0]
addLayer = arcpy.mapping.Layer(bufferOutput)
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
arcpy.AddMessage("Added the buffered features to your current map document. (Under the imagery)")
arcpy.AddMessage("*****************************************")
# Open MXD and Get the Data Frame

for df in arcpy.mapping.ListDataFrames(mxd):
    print str(df.extent)

with arcpy.da.SearchCursor(bufferOutput, ["shape@", field_name]) as rows:
    for row in rows:
        geom = row[0]
        df.extent = geom.extent

        tpkName = row[1]
        if os.path.isfile(env.workspace + "/" + tpkName + '.tpk'):
            print "Skipping: " + workspace + "/" + tpkName + '.tpk'
            arcpy.AddMessage("Skipping: " + workspace + "/" + tpkName + ".tpk")
            continue

        print "Saving: " + workspace + "/" + tpkName + ".mxd"
        arcpy.AddMessage("Saving: " + workspace + "/" + tpkName + ".mxd")
        arcpy.AddMessage("*****************************************")
        arcpy.AddMessage("Generating tile packages. This may take a while...")
        arcpy.AddMessage("*****************************************")
        mxd.saveACopy(workspace + "/" + tpkName + ".mxd")
        arcpy.CreateMapTilePackage_management(workspace + "/" + tpkName + ".mxd", "ONLINE", workspace + "/" + tpkName + '.tpk', "MIXED", "20")

if arcpy.Exists(bufferOutput):
    arcpy.Delete_management(bufferOutput)
