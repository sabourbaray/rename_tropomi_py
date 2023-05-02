import xarray as xr
import os
import sys
import numpy as np
import datetime as datetime
import pandas as pd

tropomi_cache = "$TROPOMIDIR/ncin"


tropomi_files = [f for f in os.listdir(tropomi_cache) if ".nc" in f]
tropomi_paths = [os.path.join(tropomi_cache, f) for f in tropomi_files]
gotdate=[]
newpath=[]

for f in range(len(tropomi_paths)):
    finddate={}
    tropomi_data = xr.open_dataset(tropomi_paths[f], group="instrument")
    finddate['yyyy'] = int(xr.DataArray(tropomi_data["time"]).where(tropomi_data["time"]>=0,drop="True").values[0,0])
    finddate['mm'] = int(xr.DataArray(tropomi_data["time"]).where(tropomi_data["time"]>=0,drop="True").values[0,1])
    finddate['dd'] = int(xr.DataArray(tropomi_data["time"]).where(tropomi_data["time"]>=0,drop="True").values[0,2])
    gotdate.append(str(finddate['yyyy']) + str(finddate['mm']).zfill(2) + str(finddate['dd']).zfill(2))
    newpath.append(tropomi_paths[f].split(".nc")[0] + "____" + gotdate[f] + ".nc")
    newpath[f] = newpath[f].replace("ncin","ncout")
    tropomi_data.close()
    os.rename(tropomi_paths[f],newpath[f])
