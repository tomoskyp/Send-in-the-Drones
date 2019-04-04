#These are excerpts of the code that I use to calculate the Haversine distance between 2 Lat/Longs.
#Don't worry about the details like rail and INSEE - just think of them as 2 sets of Lat/Longs.
#Let me know if these are any questions...

#I think these are the 2 libraries I needed to import for this Haversine function:
import math
from math import radians, cos, sin, asin, sqrt

#I actually import all of these libraries, but I think the 2 I just referred to are the critical ones.
# library setup
import pyodbc
import pprint    
import pandas as pd
import numpy as np
import time
import re
import math
from math import radians, cos, sin, asin, sqrt
from openpyxl import Workbook
import unidecode
import playsound
import os
import codecs
import datetime
from time import gmtime, strftime
import time
import Levenshtein
import difflib


# HERE IS THE HAVERSINE FUNCTION.
# set the value of r below to 3956 for miles, 6371 for kilometers, and 20887680 for feet.  I use 3956 below.
# IMPORTANT: note the order that the parameters are passed to this function: lon1, lat1, lon2, lat2

def haversine(lon1, lat1, lon2, lat2):
    """
    https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    #print('lon1=',lon1)
    #print('lat1=',lat1)
    #print('lon2=',lon2)
    #print('lat2=',lat2)
    try:
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # 6371 Radius of earth in kilometers. Use 3956 for miles, 20887680 for feet
        return c * r
    except:
        return -1



# HERE IS HOW I CALL THE FUNCTION.  I have a Rail longitude and Latitude, and then I was finding how close it was to the INSEE Longitude and Latitude.
# Don't worry about INSEE and what it means.  Just send the 1st longitude and latitude,
# and then the 2nd longitude and latitude.

    haversine_best = 10000 #set this to some high number

    rail_record_id = results1[0]
    rail_latitude = float(results1[1])
    rail_longitude = float(results1[2])


        Code_INSEE = results2[0]
        geo_point_2d = results2[1]
        temp_list = geo_point_2d.split(', ')
        INSEE_latitude = float(temp_list[0])
        INSEE_longitude = float(temp_list[1])

        #haversine(lon1, lat1, lon2, lat2):
        haversine_mi = haversine(rail_longitude, rail_latitude, INSEE_longitude, INSEE_latitude)
	#use this code to find the smallest difference:
        if haversine_mi < haversine_best:  
            haversine_best = haversine_mi
            Code_INSEE_best = Code_INSEE
            INSEE_latitude_best = INSEE_latitude
            INSEE_longitude_best = INSEE_longitude

TEST THIS OUT WITH SOME DISTANCES YOU KNOW OR CAN APPROXIMATE FROM GOOGLE MAPS TO MAKE SURE YOU'RE DOING IT RIGHT.