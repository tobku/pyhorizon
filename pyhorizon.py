# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# read measured azimuth and elevation from file
df = pd.read_csv('horizon_measured.csv', delimiter=',')
df = df.rename(columns={"El ": "El"})
if(df.at[0,'Az']!=0):
    df_first_row = df.head(1).copy()
    df_first_row.loc[0,'Az']=0
    df = pd.concat([df_first_row, df], ignore_index=True, sort=False)

if(df.at[df.index.size-1,'Az']!=360):
    df_last_row = df.tail(1).copy()
    df_last_row.index = [0];
    df_last_row.loc[0,'Az']=360
    df = pd.concat([df, df_last_row], ignore_index=True, sort=False)

azimuth = df.Az.tolist()
elevation = df.El.tolist()

# plot measurement
plt.plot(azimuth,elevation,'x')
plt.grid()
plt.show()
plt.savefig('horizon_measured.png')

#create interpolant
y_interp = interp1d(azimuth,elevation)

#interpolate
new_az = np.linspace(0,360,180,endpoint=False).tolist()
new_elev = y_interp(new_az).tolist()

# plot interpolated horizon
plt.plot(new_az,new_elev)
plt.grid()
plt.show()
plt.savefig('horizon_interpolated.png')

# save interpolated horizon to csv
np.savetxt("horizon_interpolated.csv", 
           new_elev,
           delimiter =", ", 
           fmt ='% s')

__author__ = "toku"
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "toku"
__email__ = "tobias.kull@uni-bayreuth.de"
__status__ = "Prototype"
