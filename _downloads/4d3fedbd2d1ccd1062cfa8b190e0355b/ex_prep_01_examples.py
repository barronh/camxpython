"""
Get Examples Folder
===================

The section describes how to get all the examples as python files.

Steps:

1. Go to the bottom of the `Examples page <https://barronh.github.io/camxpython/auto_examples/index.html>`_.
2. Download the zip file "Download all examples in Python source code: auto_examples_python.zip".
3. Unzip the `auto_examples_python.zip` into `~/examples`.

This can be done by right clicking on the zip link, choosing copy link, and
using the link in the code below:

.. code::

    # you must edit the line below, or it will not work
    # something like:
    #  url="https://barronh.github.io/camxpython/_downloads/07fcc19ba03226cd3d83d4e40ec44385/auto_examples_python.zip"
    url="<LINK-GOES-HERE>"
    wget -N ${url}
    unzip -d ~/examples auto_examples_python.zip


When you're done, run `tree -L 2 ~/examples`. You should get something like:

.. code::

    examples/
    |-- gridemiss
    |   |-- run_gridemiss_01.py
    |   `-- run_gridemiss_02.py
    |-- maps
    |   `-- run_maps_01_compare.py
    |-- mpe
    |   |-- run_mpe_01.py
    |   `-- run_mpe_02.py
    |-- prep
    |   |-- ex_prep_01_examples.py
    |   |-- ex_prep_02_setup.py
    |   |-- ex_prep_03_mamba.py
    |   `-- ex_prep_04_downloadcamx.py
    |-- ptsrce
    |   |-- run_ptsrce_01.py
    |   `-- run_ptsrce_02.py
    `-- satellite
        |-- data.gesdisc.earthdata.nasa.gov
        |-- outputs
        |-- run_satellite_01.py
        `-- run_satellite_02.py

"""
