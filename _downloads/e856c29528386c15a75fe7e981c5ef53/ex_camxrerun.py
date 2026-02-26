"""
Rerun CAMx with Updated Emissions
=================================

The basic steps are:

1. Edit job script.
2. Run new job script.


Edit Job Script
'''''''''''''''

Below is a bash command that makes a requirements.txt

.. code-block:: fortran

    --- CAMx_v7.32.36.12.20160610-11.noMPI.job      2026-01-27 12:48:03.741867000 -0500
    +++ CAMx_v7.32.36.12.20160610-11.noMPI-updatedemis.job  2026-02-19 11:09:48.976320000 -0500
    @@ -15,7 +15,9 @@ set ICBC    = "../icbc"
     set INPUT   = "../inputs"
     set MET     = "../met"
     set EMIS    = "../emiss"
    +set EMISS    = "../../examples/gridemiss/outputs"
     set PTSRCE  = "../ptsrce"
    +set PTSRCES  = "../../examples/ptsrce/outputs"
     set OUTPUT  = "../outputs"
     #
     mkdir -p $OUTPUT
    @@ -106,7 +108,7 @@ cat << ieof > CAMx.in
     
     !--- Output specifications ---
     
    - Root_Output_Name         = '$OUTPUT/CAMx.$RUN.${CALDAY}',
    + Root_Output_Name         = '$OUTPUT/CAMx.$RUN.${CALDAY}.2D_EDIT',
      Average_Output_3D        = .true.,
      NetCDF_Format_Output     = .true.,
      NetCDF_Use_Compression   = .false.,
    @@ -124,8 +126,9 @@ cat << ieof > CAMx.in
      Initial_Conditions   = '$ICBC/ic.36km.${CALDAY}.nc',
      Boundary_Conditions  = '$ICBC/bc.36km.${CALDAY}.nc',
      Point_Sources(1)     = '$PTSRCE/point.camx.othpt.${CALDAY}.nc',
    - Point_Sources(2)     = '$PTSRCE/point.camx.ptnonipm.${CALDAY}.nc',
    + Point_Sources(2)     = '$PTSRCES/point.camx.ptnonipm_edit.${CALDAY}.nc',
      Point_Sources(3)     = '$PTSRCE/point.camx.pt_oilgas.${CALDAY}.nc',
    + Point_Sources(4)     = '$PTSRCES/point.camx.just1.${CALDAY}.nc',
      Master_Grid_Restart  = '$OUTPUT/CAMx.$RUN.${YESTERDAY}.inst',
      Nested_Grid_Restart  = '$OUTPUT/CAMx.$RUN.${YESTERDAY}.finst',
      PiG_Restart          = ' ',
    @@ -135,7 +138,7 @@ cat << ieof > CAMx.in
      Met2D_Grid(1)   = '$MET/camx.2d.36km.${CALDAY}.nc',
      Vdiff_Grid(1)   = '$MET/camx.kv.36km.${CALDAY}.YSU.nc',
      Emiss_Grid(1,1) = '$EMIS/camx_area.area.${CALDAY}.36km.nc',
    - Emiss_Grid(1,2) = '$EMIS/camx_area.mobile.${CALDAY}.36km.nc',
    + Emiss_Grid(1,2) = '$EMISS/camx_area_2x.mobile.${CALDAY}.36km.nc',
      Emiss_Grid(1,3) = '$EMIS/camx_area.pt.${CALDAY}.36km.nc',
      Emiss_Grid(1,4) = '$EMIS/camx_area.natural.${CALDAY}.36km.nc',
     
    @@ -144,7 +147,7 @@ cat << ieof > CAMx.in
      Met2D_Grid(2)   = '$MET/camx.2d.12km.${CALDAY}.nc',
      Vdiff_Grid(2)   = '$MET/camx.kv.12km.${CALDAY}.YSU.nc',
      Emiss_Grid(2,1) = '$EMIS/camx_area.area.${CALDAY}.12km.nc',
    - Emiss_Grid(2,2) = '$EMIS/camx_area.mobile.${CALDAY}.12km.nc',
    + Emiss_Grid(2,2) = '$EMISS/camx_area_2x_county.mobile.${CALDAY}.12km.nc',
      Emiss_Grid(2,3) = '$EMIS/camx_area.pt.${CALDAY}.12km.nc',
      Emiss_Grid(2,4) = '$EMIS/camx_area.natural.${CALDAY}.12km.nc',


Rerun CAMx
''''''''''

.. code-block:: bash

    ./CAMx_v7.32.36.12.20160610-11.noMPI-updatedemis.job

"""
