# ListGeoData
Search a folder and subfolder for geo data

Using Esri ArcPy, search a folder and it's subfolders for Feature Clases, Datasets, Rasters and Tables.

Change line 4 to the folder to scan.
env.workspace = "f:/"  #folder to scan

If you want to skip a (one) subfolder, enter it on line 5
skipfolder = "v:/gis/temp" #folder to skip
