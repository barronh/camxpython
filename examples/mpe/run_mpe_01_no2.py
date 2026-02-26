"""
Compare Model to Hourly Observations
====================================

Evaluate CAMx by comparing to AirNow or AQS hourly observations.

The basic steps are:

1. Open CAMx file and identify space/time domain,
2. Download hourly observations for that domain to a CSV file.
3. Add CAMx hourly model data to the observations CSV file..
4. Plot a time series

*Reminder*: You must have already activated your python environment.
"""

# %%
# Configuration
# '''''''''''''

# Define Analysis
obssrc = 'airnow'  # or aqs
obsspc = 'no2'     # or ozone, co, pm25, ...
modsrc = 'CAMx'    # Or CMAQ
modspc = 'NO2'     # or O3, CO, PM25, ...

# Set input files
dates = ['20160610', '20160611']
avrgtmpl = '../../camx/outputs/CAMx.v7.32.36.12.{}.avrg.grd02.nc'  # placeholder {} for date

# Outputs
outstem = f'outputs/{obssrc}.{obsspc}_and_CAMx.v7.32.36.12.avrg.grd02'
pairedpath = outstem + '.csv'
statspath = outstem + '_stats.csv'
figpath = outstem + '_ts.png'

# %%
# Imports and Folders
# '''''''''''''''''''

import pandas as pd
import os
import pyrsig

os.makedirs('outputs', exist_ok=True)

# %%
# Query Observations for each model file
# ''''''''''''''''''''''''''''''''''''''

obskey = f'{obssrc}.{obsspc}'  # must exist in RSIG
modkey = f'{modsrc}{modspc}'
dfs = []
for datestr in dates:
    ds = pyrsig.open_ioapi(avrgtmpl.format(datestr))
    df = pyrsig.cmaq.pair_rsigcmaq(ds, modspc, obskey, prefix=modsrc, workdir='outputs')
    df[modkey] *= 1000
    df.rename(columns={obsspc: obskey}, inplace=True)
    dfs.append(df)

df = pd.concat(dfs)
df.to_csv(pairedpath)

# %%
# Calculate Statistics
# ''''''''''''''''''''

keys = [obskey, modkey]
statsdf = pyrsig.utils.quickstats(df[keys], obskey)
# Print them for the user to review.
print(statsdf)
# Save stats to disk
statsdf.to_csv(statspath)

# %%
# Make a Plot
# '''''''''''

gb = df.groupby('time')[keys]
ax = gb.median().plot(color=['k', 'r'], linewidth=2, zorder=2)
gb.quantile(.75).plot(ax=ax, color=['k', 'r'], linestyle='--', legend=False, zorder=1)
gb.quantile(.25).plot(ax=ax, color=['k', 'r'], linestyle='--', legend=False, zorder=1)
ax.figure.savefig(figpath)

# %%
# Extra Credit
# ''''''''''''
# 1. AirNow uses the "airnow" prefix and AQS uses "aqs". Can you change the script to evaluate no2 from AQS? Modify
# 2. Instead of no2, can you change the script to evaluate carbon monoxide?
