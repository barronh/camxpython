"""
Create a Hypothetical Source
============================

This example averages all other sources to create a single hypothetical source.
It also reports all variables that are in the file, which makes direct modification easy.

The basic steps are:

1. Read in an existing point source file.
2. Average all points (points are COL dimension).
3. Save out result.
4. Visualize result.

*Reminder*: You must have already activated your python environment.
"""

# %%
# Configuration
# '''''''''''''

# what date are you processing?
date = '20160610'
# existing point source file to copy
oldpath = f'../../camx/ptsrce/point.camx.ptnonipm.{date}.nc'
# new point source file for 1 "average" source
newpath = f'outputs/point.camx.just1.{date}.nc'
# plot that demonstrates new file
figpath = 'outputs/example_ptsrce_newsinglesource.png'

# %%
# Imports
# '''''''

import PseudoNetCDF as pnc
import os

# %%
# Pepare Folders
# ''''''''''''''

os.makedirs('outputs', exist_ok=True)
if os.path.exists(newpath):
    os.remove(newpath)

# %%
# Create a Single Source File
# '''''''''''''''''''''''''''
# - Old file has N point sources.
# - Oddly, each point source is an element of the COL dimension.
# - Average the COL dimension to make an "average" point source.

oldfile = pnc.pncopen(oldpath)
newfile = oldfile.apply(COL='mean')
saved = newfile.save(newpath, format='NETCDF4_CLASSIC', outmode='ws')
saved.close()

# %%
# Visualize Source to confirm operational
# '''''''''''''''''''''''''''''''''''''''

import PseudoNetCDF as pnc
import matplotlib.pyplot as plt
import pycno

# open file and get coordinate information
newfile = pnc.pncopen(newpath, format='netcdf')
proj = newfile.getproj(projformat='proj4', withgrid=False, fromorigin=True)
t = newfile.getTimes()
x = newfile.variables['xcoord'][:]
y = newfile.variables['ycoord'][:]

# Create a plot with a primary axis for FPRM, a secondary axis for NOx,
# and an inset axis for spatial location.
gskw = dict(bottom=0.25, top=.9)
fig, ax = plt.subplots(gridspec_kw=gskw)
sax = ax.twinx()
mapax = fig.add_axes([.15, .65, .2, .2])

# Add outlines of countries to the map.
cno = pycno.cno(proj=proj, xlim=(-2.5e6, 2.5e6), ylim=(-2e6, 2e6))
cno.drawcountries(ax=mapax)
# add a point for the source
mapax.scatter(x=x, y=y, marker='+', color='r')
mapax.set(xticks=[], yticks=[])

# Add a time-series plot of FPRM to the primary axis
ax.plot(t, newfile.variables['FPRM'][:, 0], label='FPRM', color='k')
ax.set(ylabel='FPRM [g/h]')
# Add a time-series plot of NOx to the secondary axis
noxf = newfile.eval('NOx = NO[:] + NO2[:]')
sax.plot(t, noxf.variables['NOx'][:, 0], label='NOx', color='r')
sax.set(ylabel='NOx [mol/h]')

# Orient the date tick labels
plt.setp(ax.get_xticklabels(), rotation=90)
# Add a legend for both axes
ll = ax.lines + sax.lines
ax.legend(ll, [_l.get_label() for _l in ll], loc='lower right')
# Save the figure to disk
fig.savefig(figpath)

# %%
# Extra Credit
# ''''''''''''
# 1. Modify the script to set the xcoord and yxoord to a new location before saving out [LCC meters].
# 2. What other properties might you want to change?
