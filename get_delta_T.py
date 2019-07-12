import numpy as np
import Nio
import sys
import geog_funcs

rcplist = ['45', '85']
delta_T_2100 = np.zeros(2)
delta_T_2300 = np.zeros(2)
anomaly_forcing_files = ['af.tas.ccsm4.rcp45.2006-2300.nc','af.tas.ccsm4.rcp85.2006-2300.nc']
for rcp_i, rcp in enumerate(rcplist):
    file_forcing = Nio.open_file(anomaly_forcing_files[rcp_i])
    tas = file_forcing.variables['tas'][:]
    lats_forcing = file_forcing.variables['LATIXY'][:,0]
    lons_forcing = file_forcing.variables['LONGXY'][0,:]
    file_forcing.close()
    forcingfile_ntim_to_average = 120
    forcingfile_2100 = (2090-2006)*12
    delta_T_2100[rcp_i] = geog_funcs.area_average(tas[forcingfile_2100:forcingfile_2100+forcingfile_ntim_to_average,:,:].mean(axis=0), lats_forcing, lons_forcing)
    forcingfile_2300 = (2290-2006)*12
    delta_T_2300[rcp_i] = geog_funcs.area_average(tas[forcingfile_2300:forcingfile_2300+forcingfile_ntim_to_average,:,:].mean(axis=0), lats_forcing, lons_forcing)

print('global T anomalies, at 2100, for RCP4.5 and RCP8.5 are:')
print(delta_T_2100)
print('global T anomalies, at 2300, for RCP4.5 and RCP8.5 are:')
print(delta_T_2300)
