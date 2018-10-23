# now we get our sat and ship coordonate, we can calcul the az and el for the rotor .
# this code should be easy and fast to calculate the command for the rotor every seconde .

from math import *
import numpy as np 
from np import *
import matplotlab.py as plt 
from plt import *
import ephem
import serial 
from time import sleep
import latlon

def calcul(deg, lat_lg,sat):
    



#note : ephem gives the lat and long coor on deg min sec . This one should be convert first in deg decimal for the calcul
#note : the calcul for te conversion is dec = d+(m/60)+(s/3600) with a coordonate (d°m's")
# note : GNSS give the lat and long coor on  deg decimal . it's ok  for the calcul .
    

# for the need of our calcul and more readability  we are going to split sat to calculate our new coordonates 
#here every sat conversion
    
    lat_sat= sat[0].split(':')
    long_sat = sat[1].split(':')
    sat_dec = [0,0,0]
    
    for k in range(lat_sat):            # the coordonates are considerated as str, for our calcul we first have to convert them 
        lat_sat[k] = int(lat_sat[k])
        
    for k in range(long_sat):
        long_sat[k] = int(lon_sat[k])
        
        
    if lat_sat[0] >= 0 :
        sat_dec[0] = lat_sat[0] + (lat_sat[1]/60) + (lat_sat[2]/3600)
    else : 
        sat_dec[0] = -(abs(lat_sat[0]) + (lat_sat[1]/60) + (lat_sat[2]/3600))
    
    if long_sat[0] >= 0 :
        sat_dec[1] = long_sat[0] + (long_sat[1]/60) + (long_sat[2]/3600)
    else : 
        sat_dec[1] = -(abs(long_sat[0]) + (long_sat[1]/60) + (long_sat[2]/3600))
        
    sat_dec[2] = sat[2]
     
        # here every GNSS conversion 
        
    lat_sbt= int(lat_lg[2])
    long_sbt = int(lat_lg[4])
    
        # now we have our new sat_dec with lat, long and alt, in deg dec we can do the calcul.
    
    robusta = latlon(sat_dec[0],sat_dec[1])
    sbt = latlon(lat_sbt,long_sbt)
    dist = robusta.distance(sbt)
    
    
    # we can now calculate our elevation and azimuth for the rotor 
    
    elevation = atan(
    
    
        
        
        
   
