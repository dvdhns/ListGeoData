import arcpy
from arcpy import env
import os
env.workspace = "f:/"  #folder to scan
skipfolder = "v:/gis/temp" #folder to skip

wslist = arcpy.ListWorkspaces()
fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    desc = arcpy.Describe(fc)
    print desc.datatype, desc.path, desc.file

folders = os.walk( env.workspace  )
for folder in folders:
    try:
        if not skipfolder in folder[0]:
            env.workspace = folder[0]
            desc = arcpy.Describe(env.workspace)
            if desc.datatype == 'Folder':
                
                dslist = arcpy.ListDatasets()
                for ds in dslist:
                    desc = arcpy.Describe(ds)
                    print desc.datatype + "," + desc.path + "," +  desc.file

                fclist = arcpy.ListFeatureClasses()
                for fc in fclist:
                    desc = arcpy.Describe(fc)
                    print desc.datatype + "," + desc.path + "," +  desc.file

                rslist = arcpy.ListRasters()
                for rs in rslist:
                    desc = arcpy.Describe(rs)
                    print desc.datatype + "," + desc.path + "," +  desc.file

                tblist = arcpy.ListTables()
                for tb in tblist:
                    desc = arcpy.Describe(tb)
                    print desc.datatype + "," + desc.path + "," +  desc.file
    except:
        print "error," + folder[0]
            

    
        
        
