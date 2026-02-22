# SESARM February 2026 Training

---
    author: Barron H. Henderson
    last updated: 2026-02-06
---

This document provides notes on three exercises to be performed with CAMx at the SESARM CAMx Training. These examples were determined based on discussions with the meeting organizers to be most responsive to the community's needs.

Objectives:

* Prepare modified emissions files from existing model-ready emission files.
    * point sources, and
    * Gridded emissions
* Run CAMx with modifications
* Evaluate Model using Surface Monitors 
    * NO2 evaluation
    * Update to evaluate ozone
* Compare Model to Satellite Columns
    * Nitrogen dioxide quick comparison.
    * Accounting for the averaging kernel.
* Check CAMx updated runs.


# Annotated Directory Sturcture

```
.
|-- README.md
|-- requirements.txt  # python -m pip install -r requirements.txt
|-- requirements-docs.txt  # python -m pip install -r requirements-docs.txt
|-- camx
|   |   # Standard CAMx.v7.32 test case
|   |-- README
|   |-- src.v7.32  # source directory (built)
|   |-- runfiles   # edited to add 3D avrg output
|   |-- inputs
|   |-- icbc
|   |-- met
|   |-- emiss
|   |-- ptsrce  
|   |-- outputs
|   |   |-- ... # added 3D outputs for satellite analysis
|   |   |-- CAMx.v7.32.36.12.20160610.3D.avrg.grd01.nc
|   |   |-- CAMx.v7.32.36.12.20160610.3D.avrg.grd02.nc
|   |   |-- CAMx.v7.32.36.12.20160611.3D.avrg.grd01.nc
|   |   `-- CAMx.v7.32.36.12.20160611.3D.avrg.grd02.nc
|   |
|   |   # Standard CAMx.v7.32 test case tar files
|   `-- www.camx.com/getmedia/*.tgz
`-- training
    |-- scripts
    |   |-- gridemiss_compare.py
    |   |-- gridemiss_perturb.py
    |   |-- mpeno2_plot.py
    |   |-- ptsrce_singlesource.py
    |   |-- tropomi_plot.py
    |   `-- tropomi_process.py
    |-- inputs/GRIDDESC  # made by hand to match CAMx domains
    |-- figs  # outputs from *_plot.py
    |   |-- AirNow_NO2.png
    |   |-- cmaq_tropomi.png
    |   |-- example_single_source.png
    |   `-- scaled_emis.png
    |-- outputs
    |   |-- airnow.no2_2016-06-10T000000Z_2016-06-10T235959Z.csv.gz
    |   |-- airnow.no2_and_CAMx.v7.32.36.12.20160610.avrg.grd02.csv
    |   |-- AirNow_NO2_stats.csv
    |   |-- camx_area_2x.mobile.20160610.12km.nc
    |   |-- CAMx_TropOMINO2_2019-06-10_36CAMX1.nc
    |   |-- point.camx.just1.20160610.nc
    |   `-- TropOMINO2_2019-06-10_36CAMX1.nc
    |
    |   # downloaded by tropomi_process.py
    `-- data.gesdisc.earthdata.nasa.gov/data/S5P_TROPOMI_Level2
```
