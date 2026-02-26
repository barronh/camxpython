Get System Ready
----------------

The first step to running examples is to prepare the computer on. The examples
can be run on Linux, Mac (OS X), or Windows machines. Some of the instructions
will assume you are in a terminal (Linux or Mac), but can be adapted to Windows
Command Prompt or PowerShell.

Steps:

1. Download examples folder.
2. Setup a python version
    * Either with a system Python
    * Or mamba.
3. Get CAMx tutorial files.

Once you have done all these steps, you should will be ready to run example
scripts. The scripts use file paths to "point" to files assuming a relative
folder structure. Each python script (eg, `run_gridemiss_01_perturb.py`)
will be run using python from within its folder (eg, `examples/gridemiss/`).
So, it is important that the folder structure is as expected or you edit
the paths in the scripts.

So, if you were done preparing the system (steps 1-3), you would run an
example script like this on Linux or Mac:

.. code::

    cd ~
    cd examples/gridemiss
    python run_gridemiss_01_perturb.py


Or Windows PowerShell

.. code::

    cd ~
    cd examples/gridemiss
    py.exe run_gridemiss_01_perturb.py

As an alternative, you can run these script by pasting sections of them into an
interactive Python console. For example, on Linux/Mac:

.. code::

    cd ~/examples/gridemiss
    python
    >>> # paste commands here

Or in Windows PowerShell:

.. code::

    cd ~/examples/gridemiss
    py.exe
    >>> # paste commands here

Remember, this will not work until you complete the preparation steps:

1. Getting the examples folder done in `Get Examples Folder`
2. Preparing the python executable is described in the `Preparing Python Environment` (or in the `Using Mamba to get Python`).
3. Getting the CAMx tutorial data is described in the `Getting CAMx Files` example.
