import math
from math import *
from numpy import *
import pandas as pd
import numpy as np

# Haversine Formula:
def haversine(lon1, lat1, lon2, lat2):
    try:
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        r = 6371 # 6371 Radius of earth in kilometers.
        return c * r
    except:
        return -1

# Hospitals: long / Lat:
Fajardo = [-65.65012, 18.33211]     # These have been updated from what was given
San_Pablo = [-65.65485, 18.33673]
San_Juan = [-66.06898, 18.44424]
Bayamon =  [-66.16327, 18.39657]
Arecibo = [-66.73172, 18.46705]

# Drones V/MPC/Speed (km/h)/FT no cargo/Range no cargo/ Range max cargo
DroneB = [19800.0, 8.0, 79.0, 40.0, 52.667,47.4]

# Area Search for San Juan and Bayamon: Long / Lat
NW1 = [-66.210, 18.455]
SW1 = [-66.210, 18.267]
NE1 = [-65.960, 18.455]
SE1 = [-65.690, 18.267]
Point1 = [-66.210, 18.267]

#Loop for San Juan and Bayamon
i = Point1[0]
j = Point1[1]

Haver_out1 = pd.DataFrame(columns = ['Lats','Lons','San Juan','Bayamon','Valid Points'])
san_juan = []
bayamon = []
lats1 = []
lons1 = []
for i in np.arange(NW1[0], NE1[0],0.001):
    for j in np.arange(SE1[1], NE1[1],0.001):
        r_1 = haversine(float(San_Juan[0]), float(San_Juan[1]), i, j)
        r_2 = haversine(float(Bayamon[0]), float(Bayamon[1]), i, j)
        san_juan.append(r_1)
        bayamon.append(r_2)
        lats1.append(j)
        lons1.append(i)
Haver_out1['Lats'] = lats1
Haver_out1['Lons'] = lons1
Haver_out1['San Juan'] = san_juan
Haver_out1['Bayamon'] = bayamon

#loop to get valid points
k = 0
Vpoints =[]

for k in range(len(Haver_out1)):
    if DroneB[5]/2 - Haver_out1.iloc[k]['San Juan'] >= 0 and DroneB[5]/2 - Haver_out1.iloc[k]['Bayamon'] >=0:
        Vpoints.append([Haver_out1.iloc[k]['Lats'], Haver_out1.iloc[k]['Lons']])
    else:
        Vpoints.append(np.nan)

Haver_out1['Valid Points'] = Vpoints
Haver_out1 = Haver_out1.dropna()

# loop to get max sum of distances to get best drop locations
Distance = 0
best_index = []

for k in range(len(Haver_out1)):
    Distance_calc = Haver_out1.iloc[k]['San Juan'] + Haver_out1.iloc[k]['Bayamon']
    if Distance_calc > Distance and Distance_calc >= 38: #and Haver_out1.iloc[0]['San Juan']:
        Distance = Distance_calc
        best_index = Haver_out1.iloc[k]
        print best_index