# pyhorizon
With pyhorizon you can calculate 360 degree horizon files from measurements for the use in PVGIS.

Use rkinnett's gyrocam (https://rkinnett.github.io/gyrocam/) to produce a *.csv file of the surrounding horizon. Use the defining extremal points (treetops, chimneys, valleys) to create your custom horizon file. The CSV-file must be saved as "horizon_measured.csv" and must be formatted like this:

```
Az, El
0, 0
...
359, 0
```


Execute pyhorizon.py in the folder containing "horizon_measured.csv". pyhorizon will then produce a interpolated horizon file ("horizon_interpolated.csv") with equidistant azimuth for the PVGIS tool (https://re.jrc.ec.europa.eu/pvg_tools/en/).
