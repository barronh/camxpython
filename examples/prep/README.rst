Get System Ready
----------------

The examples shared assume a file structure described below::

    .
    |-- examples
    |   |-- gridemiss/run_gridemiss_01_perturb.py
    |   |-- gridemiss/run_gridemiss_02_perturbbox.py
    |   |-- ptsrce/run_ptsrce_01_singlesource.py
    |   |-- ptsrce/run_ptsrce_02_editlonlatbox.py
    |   |-- mpe/run_mpe_01_no2.py
    |   |-- mpe/run_mpe_02_o3mda8.py
    |   |-- satellite/run_satellite_01_simpleomi.py
    |   |-- satellite/run_satellite_02_tropomiak.py
    |   `-- maps/run_maps_01_compare.py
    |
    |   # Standard CAMx.v7.32 test case downloaded from camx.com and expanded
    `-- camx
        |   # standard test-case inputs
        |-- emiss/camx_area.mobile.20160610.36km.nc
        |-- emiss/camx_area.mobile.20160610.12km.nc
        |-- ptsrce/point.camx.ptnonipm.20160610.nc
        |-- ptsrce/point.camx.ptnonipm.20160610.nc
        |   # standard camx test-case outputs
        |-- outputs/CAMx.v7.32.36.12.20160610.avrg.grd02.nc
        |-- outputs/CAMx.v7.32.36.12.20160611.avrg.grd02.nc
        |
        |   # outputs 3D were run using the standard test case with 3D set to .true.
        |   # and output species include NO2
        |-- outputs/CAMx.v7.32.36.12.20160610.3D.avrg.grd01.nc
        |-- outputs/CAMx.v7.32.36.12.20160610.3D.avrg.grd02.nc
        |-- outputs/CAMx.v7.32.36.12.20160611.3D.avrg.grd01.nc
        `-- outputs/CAMx.v7.32.36.12.20160611.3D.avrg.grd02.nc

Each python script (`*.py`) will be run using python3 from within its folder.
For example, `run_gridemiss_01_perturb.py` would be run from within
`examples/gridemiss` as:

.. code::

    python3 run_gridemiss_01_perturb.py


The python3 executable will be setup as described in the Preparing Python Environment.