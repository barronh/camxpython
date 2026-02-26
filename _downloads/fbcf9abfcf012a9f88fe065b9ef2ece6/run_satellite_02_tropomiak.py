"""
Pair CAMx with TropOMI NO2
==========================

This example pairs CAMx 3D data with TropOMI NO2 columns using the CMAQ
Satellite Processors (cmaqsatproc). This includes (1) downloading TropOMI data
from NASA's Distribution and Active Archive Centers (DAAC), (2) regridding
TropOMI to the CAMx grid, (3) subseting CAMx to just overpass times, (4)
filtering CAMx to valid retrieval pixels/layers, and (5) applying the CAMx
a priori shape to the TropOMI retrieval.

*Reminder*: You must have already activated your python environment.
"""

# %%
# Configuration
# '''''''''''''

# General settings
satname = 'TropOMINO2'  # or TropOMIHCHO, VIIRS_AERDB, ...
date = '2019-06-10'  # Doing just one day... as a surrogate.
GDNAM = '36CAMX1'  # Using Lambert Conic Conformal 36-km grid
gdpath = '../../camx/GRIDDESC'  # Definition of a grid
figpath = f'outputs/CAMx_{satname}_{GDNAM}_{date}.png'

# %%
# Imports and Folders
# '''''''''''''''''''

import xarray as xr
import cmaqsatproc as csp
import matplotlib.pyplot as plt
import pycno
import os

os.makedirs('outputs', exist_ok=True)


# Define input paths
sdate = '2016' + date.replace('-', '')[4:]  # pair 2019 satellite with 2016 model...
cpath = f'../../camx/outputs/CAMx.v7.32.36.12.{sdate}.3D.avrg.grd01.nc'
mpath = f'../../camx/met/camx.3d.36km.{sdate}.nc'

# Define outputpaths
l3spath = f'outputs/{satname}_{date}_{GDNAM}.nc'
l3mpath = f'outputs/CAMx_{satname}_{date}_{GDNAM}.nc'

# %%
# Satellite to CMAQ/CAMx Grid
# '''''''''''''''''''''''''''

# Get a CMAQ/CAMx grid definition
cg = csp.open_griddesc(GDNAM, gdpath=gdpath)

# Get the Satellite Reader object
satreader = csp.reader_dict[satname]

# Download input files
dests = satreader.cmr_download(
    temporal=f'{date}T17:00:00Z/{date}T23:59:59Z',
    bbox=cg.csp.bbox(), verbose=1
)

# Use CMAQ grid definition and date to drive cmr query
l3 = satreader.paths_to_level3(
    dests, grid=cg.csp.geodf,
    bbox=cg.csp.bbox(), verbose=9
)
l3.to_netcdf(l3spath)


# %%
# CMAQ/CAMx to Satellite
# ''''''''''''''''''''''

# reopen satellite l3 file
l3 = xr.open_dataset(l3spath)

# Open a CMAQ 3D CONC file (NO2) and 3d met file (pressure, z, temperature, humiditiy)
cf = csp.open_ioapi(cpath)
mkeys = ['pressure', 'z', 'temperature', 'humidity']
mf = csp.open_ioapi(mpath)[mkeys].interp(TSTEP=cf.TSTEP)

# Reorganize like CMAQ for cmaqsatproc
qf = mf[mkeys]
qf['PRES'] = qf['pressure'] * 100.
qf['NO2'] = cf['NO2'].dims, cf['NO2'].data, cf['NO2'].attrs

# Create satellite according to CMAQ, and CMAQ according to satellite
overf = satreader.cmaq_process(qf, l3)
overf.to_netcdf(l3mpath)


# %%
# Make a Plot Comparison
# ''''''''''''''''''''''

mf = xr.open_dataset(l3mpath)
sf = xr.open_dataset(l3spath)

gskw = dict(left=0.033, right=0.967)
fig, axx = plt.subplots(1, 3, figsize=(16, 4), gridspec_kw=gskw)
ax = axx[2]
maxmf = mf.sel(ROW=39.5, COL=16.5)
ppml, = maxmf['NO2'].plot(y='LAY', label='NO2', marker='+', color='k', ax=ax)
swl, = maxmf['NO2_AK_CMAQ'].plot(y='LAY', marker='o', color='b', ax=ax.twiny())
ax.legend([ppml, swl], ['NO2 ppb', 'SW'])
ax.set(ylim=(1, 0), title='NO2 and Sensitivity')
Z = mf.eval('(VCDNO2_TOMI_CMAQ - VCDNO2_TOMI_CMAQ.mean()) / VCDNO2_TOMI_CMAQ.mean()')
qm = Z.plot(ax=axx[0], cmap='viridis')
Z = mf.eval('(VCDNO2_CMAQ - VCDNO2_CMAQ.mean()) / VCDNO2_CMAQ.std()')
Z.plot(ax=axx[1], norm=qm.norm, cmap=qm.cmap)
pycno.cno(mf.crs).drawstates(ax=axx[:2])
fig.savefig(figpath)
