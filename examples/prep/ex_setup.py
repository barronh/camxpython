"""
Preparing Python Environment
============================

The basic steps are:

1. Create a requirements file.
2. Install a new virtual environment (py312).

    - Load the virtual environment.
    - Install libraries.
    - Unload the virtual environment.

3. Reload


Make requirements.txt
'''''''''''''''''''''

Below is a bash command that makes a requirements.txt

.. code-block:: bash

    cat << EOF > requirements.txt
    netCDF4>=1.5.8,!=1.7.0,!=1.7.1
    pseudonetcdf
    numpy>=1.19.5,<2
    scipy>=1.5.4
    pandas>=1.1.5
    xarray>=0.16.2
    pyproj>=2.6.1
    pycno
    pyrsig>=xxx
    cmaqsatproc>=xxx
    EOF

Install a new virtual environment
'''''''''''''''''''''''''''''''''

- Make a new virtual environment (py312)
- Load the virtual environment.
- Install libraries.
- Unload virtual environment (optional)

.. code-block:: bash

    python -m venv py312
    source py312/bin/activate
    python -m pip install -r requirements.txt
    deactivate

Reload Environemnt
''''''''''''''''''

Any time you want to use the python environment, load it.

.. code-block:: bash

    source py312/bin/activate

"""
