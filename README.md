# pyhorizon
Calculate 360 degree horizon file from single measurement points for PVGIS.

Use rkinnett's gyrocam (https://rkinnett.github.io/gyrocam/) to produce a *.csv file of the surrounding horizon. Use the defining extremal points (treetops, chimneys, valleys) to create your custom horizon file. The CSV-file must be saved as "horizon_measured.csv" must be formatted like this:

Az, El

0, 0

...

359, 0

Execute pyhorizon.py in the folder "containing horizon_measured.csv". pyhorizon will then produce a interpolated equidistand horizon file ("horizon_360.csv") for the PVGIS tool (https://re.jrc.ec.europa.eu/pvg_tools/en/).
