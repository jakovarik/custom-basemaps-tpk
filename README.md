# custom-basemaps-tpk
Summary:

A Python tool to create customized basemaps (tile packages) based on an input feature class for mobile application (such as Collector for ArcGIS) consumption.
 
This tool was specifically designed to assist with an organizational workflow of generating customized tile package basemaps for use in Collector for ArcGIS. Individual output basemap(s) are generated based on the geography and attributes of input feature(s). This tool's output tile packages can be "side-loaded" onto mobile devices following Esri documentation (http://blogs.esri.com/esri/arcgis/2014/03/23/using-your-own-basemap-layers-with-collector-for-arcgis/).
In-tool help has been developed for your convenience.


Requirements: 

Run the tool from an MXD that contains file-based data only (no web services).

The MXD must have a description and tags in order for the tool to execute. To add description and tags, choose File Map Document Properties from the main menu and enter description and tags..



Steps for Using This Tool Properly:

1. If you haven't done so already, fill out your MXD's Map Document Properties, or tool won't run.
2. For Input Feature Class, navigate to the feature class you want to create individual tile packages for (this feature class can also be present in your MXD). 
3. Choose a field from the Field Name drop-down menu to be used as the output tile package titles. 
4. Specify an output location to save the tile packages to (be sure you have write access to this location).
5. Specify a Buffer Size and Units; this is to buffer your input features to generate an extent slightly larger than the feature(s) themselves for a suitable basemap extent. The buffered features are used to specify the extents of the tile package generated. 
6. Choose a maximum level of detail for your tile packages to be generated at.
7. Verify that your Map Document Properties are filled out and check the box to confirm.




Suggestions:

*Your input feature class should include a field that will be used to name your output tile packages. 
*The tile packages will be generated from the cartographic elements in your active MXD. If you have reference data or your input feature class on top of a basemap, these feature classes will appear in the output tile package. If you're looking to generate a basemap only (i.e. imagery, topo map, etc.), be sure to remove the additional feature classes from your MXD before running this tool. 
*3 things will greatly affect the time it takes this tool to run: the size of the buffer you specify (a larger buffer will result in a longer wait time as larger tile packages are being generated), the level of detail you choose (a higher level of detail means more tiles being generated which equals a longer tiling process) and the number of features in your input feature class (a greater number of features will result in a longer wait time since an individual tile package is created for each feature). 



Use limitations
This script has been developed and tested in ArcGIS 10.2.2.

