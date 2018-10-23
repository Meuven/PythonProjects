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
        lat_sat[k] = float(lat_sat[k])
        
    for k in range(long_sat):
        long_sat[k] = float(lon_sat[k])
        
     # if we need to format the number of dec see this example 
    #>>> x = 13.949999999999999999
    #>>> g = float("{0:.2f}".format(x))
    #>>> g
    #13.95
    if lat_sat[0] >= 0 :
        sat_dec[0] = int(lat_sat[0]) + float(lat_sat[1]/60) + float(lat_sat[2]/3600)
    else : 
        sat_dec[0] = -1*(int(abs(lat_sat[0])) + float(lat_sat[1]/60) + float(lat_sat[2]/3600))
    
    if long_sat[0] >= 0 :
        sat_dec[1] = int(long_sat[0]) + float(long_sat[1]/60) + float(long_sat[2]/3600)
    else : 
        sat_dec[1] = -1*(int(abs(long_sat[0])) + float(long_sat[1]/60) + float(long_sat[2]/3600))
        
    sat_dec[2] = sat[2]
     
        # here every GNSS conversion 
        
    lat_sbt= float(lat_lg[2])
    long_sbt = float(lat_lg[4])
    deg_sbt = float(deg[1])
    
        # now we have our new sat_dec with lat, long and alt, in deg dec we can do the calcul.
    
    robusta = latlon(sat_dec[0],sat_dec[1])
    sbt = latlon(lat_sbt,long_sbt)
    dist = robusta.distance(sbt)
    
    
        # we can now calculate our elevation and azimuth for the rotor 
        # for that we have to take in consideration the orientation of the ship ( data based on the true north)
    
    deg_elev = float(atan(sat_dec[2]/dist))
    deg_elev = float("{0:.2f}".format(deg_elev)) 
    
    # My idea was to create a third point with the same lat than the sbt and the same long than the sat
    # thanks to it , we geometrically work with a rectangle triangle and we can apply our cos formule
 
    
    
    temp = latlon(lat_sbt, sat_dec[1])
    new_dist = temp.distance(sbt)
    
    alpha = float(asin(new_dist/dist))
    alpha = float("{0:.2f}".format(deg_az)) 
    
    deg_az = alpha - deg_sbt
    
    return ([deg_az,deg_el])
    
    
    
    
    
                    
    
    
    
        
        
        
   
