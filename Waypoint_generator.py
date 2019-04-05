import math
from math import *
from numpy import *
import pandas as pd
import numpy as np

R = 6371       # km Radius, do not change!!
d = 23.2735    # km Distance to find waypoint 2
d1 = 11.637    # km distance to find waypoint 2 and 3
b1 = pi/2 + pi/28 #initial bearing

#Creating waypoints and lists for looping
waypoint_1 = [0,0]
waypoint_2 = [0,0]
waypoint_3 = [0,0]
waypoint_4 = [0,0]

list_waypoint_1 =[]
list_waypoint_2 =[]
list_waypoint_3 =[]
list_waypoint_4 =[]

#ISO Drop locations:
ISO2 = [18.271 , -66.1990]
# ISO1 = [18.24055, -65.74596]
# ISO3 = [18.43874, -66.60805]

# converting ISO degrees to radians:
ISO2_lat_rad = ISO2[0] * pi / 180
ISO2_lon_rad = ISO2[1] * pi / 180
ISO2_rad = [ISO2_lat_rad, ISO2_lon_rad]



# loop to get all waypoints on flight path
i = 0
while i <= 14:    # loop to iterate 14 times
    i = i + 1

    #WAYPOINT #1
    d1 = 11.637
    waypoint_1[0] = np.arcsin(np.sin(ISO2_rad[0]) * np.cos(d1/R) + np.cos(ISO2_rad[0]) * np.sin(d1/R) * np.cos(b1))
    waypoint_1[1] = ISO2_rad[1] + np.arctan2(sin(b1) *  np.sin(d1/R) *  np.cos(ISO2_rad[0]),  np.cos(d1/R) - np.sin(ISO2_rad[0]) *  np.sin(waypoint_1[0]))
    #convert back to decimal
    waypoint_1[0] = waypoint_1[0] * 180 / pi
    waypoint_1[1] = waypoint_1[1] * 180 / pi
    # Append to list
    list_waypoint_1.append([waypoint_1[0],waypoint_1[1]])
    #Update Bearing
    b1 = b1 - (pi/28)

    # WAYPOINT #2
    waypoint_2[0] = np.arcsin(np.sin(ISO2_rad[0]) * np.cos(d/R) + np.cos(ISO2_rad[0]) * np.sin(d/R) * np.cos(b1))
    waypoint_2[1] = ISO2_rad[1] + np.arctan2(sin(b1) *  np.sin(d/R) *  np.cos(ISO2_rad[0]),  np.cos(d/R) - np.sin(ISO2_rad[0]) *  np.sin(waypoint_2[0]))
    # convert back to decimal
    waypoint_2[0] = waypoint_2[0] * 180 / pi
    waypoint_2[1] = waypoint_2[1] * 180 / pi
    # Append to list
    list_waypoint_2.append([waypoint_2[0],waypoint_2[1]])
    #Update Bearing
    b1 = b1 - (pi/28)

    #WAYPOINT #3
    waypoint_3[0] = np.arcsin(np.sin(ISO2_rad[0]) * np.cos(d1/R) + np.cos(ISO2_rad[0]) * np.sin(d1/R) * np.cos(b1))
    waypoint_3[1] = ISO2_rad[1] + np.arctan2(sin(b1) *  np.sin(d1/R) *  np.cos(ISO2_rad[0]),  np.cos(d1/R) - np.sin(ISO2_rad[0]) *  np.sin(waypoint_3[0]))
    # convert back to decimal
    waypoint_3[0] = waypoint_3[0] * 180 / pi
    waypoint_3[1] = waypoint_3[1] * 180 / pi
    #Append to list
    list_waypoint_3.append([waypoint_3[0],waypoint_3[1]])
    #Update Bearing
    b1 = b1 - (pi/28)

    #WAYPOINT #4
    waypoint_4[0] = ISO2[0]
    waypoint_4[1] = ISO2[1]
    list_waypoint_4.append([waypoint_4[0],waypoint_4[1]])

    #Update Bearing
    b1 = b1 - (pi/28)
#end loop

#Add lists to dataframe
mission_list = pd.DataFrame(columns =['waypoint 1', 'waypoint 2', 'waypoint 3', 'waypoint 4'])
mission_list['waypoint 1'] = list_waypoint_1
mission_list['waypoint 2'] = list_waypoint_2
mission_list['waypoint 3'] = list_waypoint_3
mission_list['waypoint 4'] = list_waypoint_4

print mission_list
