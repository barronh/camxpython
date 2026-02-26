"""
Get Examples Folder
===================

The section describes how to get all the exmamples as python files.

Steps:

1. Navigate to the tutorial http://github.com/barronh/camxpython
2. Go to the documentation and Examples.
3. Find "Download all examples in Python source code: auto_examples_python.zip" and download it.
4. Make a `~/examples` and copy the `auto_examples_python.zip` file there.
* Unzip the `auto_examples_python.zip` (`unzip auto_examples_python.zip`).

This can be done directly right clicking on the zip link and choosing copy link.
Then pasting that link as shown below

..code::

    # The url below must be updated by righ clicking on the downloadurl may change
    # you must edit the line below or it will not work
    url="<LINK-GOES-HERE>"
    wget -N ${url}
    mkdir -p ~/examples
    unzip -d ~/examples auto_examples_python.zip


When you're done, run `tree -L 2 ~/examples`. You should get something like

..code::

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