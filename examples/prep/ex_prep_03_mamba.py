"""
Using Mamba to get Python
=========================

Sometimes machines are locked down. In that case, use your own package
manager. On these machines, we can easily use micromamba.

This is not a tutorial on micromamba, and I am going to use a fast
and dirty approach to get just what we need.


.. code-block:: bash

    mkdir -p micromamba
    pushd micromamba
    wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
    popd
    micromamba/bin/micromamba install python==3.12
    .local/share/mamba/bin/python -m venv ~/py312

Many of you will not need to do this.

"""
