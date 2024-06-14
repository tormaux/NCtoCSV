import xarray as xr
import numpy as np
import datetime as dt

netcdf_file = 'source.nc' 

xrds = xr.open_dataset(netcdf_file)
print(xrds)
# df = xrds.to_dataframe()
# df.to_csv('datafiles.csv')
# print('Conversion completed. CSV file saved as datafiles.csv')
