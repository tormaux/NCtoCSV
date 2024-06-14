import netCDF4 as nc
import numpy as np
import pandas as pd

def flatten_data(data):
    
    if len(data.shape) > 1:
        return data.flatten()
    else:
        return data

def convert_nc_to_csv(nc_file, csv_file):
    try:
        
        dataset = nc.Dataset(nc_file)
        
        
        variables = dataset.variables.keys()
        print(variables)
        
        data = {}
        
        
        for var_name in variables:
            var_data = dataset.variables[var_name][:]
            
            var_data = flatten_data(var_data)
            
            if len(var_data.shape) == 1:
                var_data = np.expand_dims(var_data, axis=1)
            data[var_name] = var_data
        
        
        df = pd.DataFrame(data)
        
        
        df.to_csv(csv_file, index=False)
        
        print(f"Conversion completed. CSV file saved as {csv_file}")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")


nc_file = 'source.nc'
csv_file = 'datafiles.csv'
convert_nc_to_csv(nc_file, csv_file)
