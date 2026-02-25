"""
Getting CAMx Files
==================

* Option 1: Get and run the CAMx testcase
* Option 2: Get a small .tar.gz


Get and Run CAMx Testcase
'''''''''''''''''''''''''

1. Got to camx.com
2. Download the CAMx v7.3.2 test case inputs.
3. Unzip test case.
4. Compile CAMx and run test case.
5. Rerun test case with 3D outputs

   - Enable 3D output and append 3D to the output stem.
   - Run the same as before.


Quick Get
'''''''''

Or save time, by downloading the files directly. This path may not exist in the
future. In that case, you need to run the testcase.

.. code::

    cd ~
    wget --continue https://gaftp.epa.gov/Air/aqmg/bhenders/share/SESARM/camx.tar.gz
    gunzip camx.tar.gz

When you are done, run `tree -L 2 ~/camx` and you should get something like this:

.. code::

    camx
    |-- GRIDDESC
    |-- emiss
    |   |-- camx_area.mobile.20160610.12km.nc
    |   `-- camx_area.mobile.20160610.36km.nc
    |-- metss
    |   `-- camx.3d.36km.20160610.nc
    |-- outputs
    |   |-- CAMx.v7.32.36.12.20160610.3D.avrg.grd01.nc
    |   |-- CAMx.v7.32.36.12.20160610.3D.avrg.grd02.nc
    |   |-- CAMx.v7.32.36.12.20160610.3D_EDIT.avrg.grd01.nc
    |   |-- CAMx.v7.32.36.12.20160610.3D_EDIT.avrg.grd02.nc
    |   |-- CAMx.v7.32.36.12.20160610.avrg.grd01.nc
    |   |-- CAMx.v7.32.36.12.20160610.avrg.grd02.nc
    |   |-- CAMx.v7.32.36.12.20160611.3D.avrg.grd01.nc
    |   |-- CAMx.v7.32.36.12.20160611.3D.avrg.grd02.nc
    |   |-- CAMx.v7.32.36.12.20160611.avrg.grd01.nc
    |   `-- CAMx.v7.32.36.12.20160611.avrg.grd02.nc
    `-- ptsrce
        `-- point.camx.ptnonipm.20160610.nc
"""