# now we get our sat and ship coordonate, we can calcul the az and el for the rotor .
# this code should be easy and fast to calculate the command for the rotor every seconde .

from math import *
import numpy as np 
import matplotlab.py as plt 
import serial 
from time import sleep
import geopy
from geopy.distance import great_circle
  
#note : ephem gives the lat and long coor on deg min sec . This one should be convert first in deg decimal for the calcul
#note : the calcul for te conversion is dec = d+(m/60)+(s/3600) with a coordonate (d°m's")
# note : GNSS give the lat and long coor on  deg decimal . it's ok  for the calcul .
    

# for the need of our calcul and more readability  we are going to split sat to calculate our new coordonates 
#here every sat conversion

def calcul(deg, lat_lg,sat):
    
    #according to the spec,  the sat alt should be at 650km, so the first print to verifie that 
    print( sat[2])
    
    
   # the elevation of the rotor is not really at the sea level. we pose m = the elev of the antenna .
    m = 0.018
    
    sat[2] = sat[2] - m
     
        # here every GNSS conversion 
        
    lat_sbt= float(lat_lg[2])
    lg_sbt = float(lat_lg[4])
    deg_sbt = float(deg[1])
    
    
    robusta = (sat[1],sat[0])
    sbt = (lat_sbt,lg_sbt)
    dist = great_circle(robusta,sbt).miles
    dist = dist *1.60934                # convert miles into km 
    
    
        # we can now calculate our elevation for the rotor .
    
    alpha = float(atan(sat[2]/dist))     # resultat should normaly be in rad 
    alpha = degrees(alpha)  
    deg_el = float("{0:.2f}".format(alpha)) 
    
    
    #for the azimuth, my idea was to create a third point with the same sbt's lat and sat's long
    #thanks to it , we geometrically work with a rectangle triangle and we can apply our cos formule.
    
    #but firstly we have to create 4 cases, because the distance is just a " norm" withou orientation,
    #and in fact it's not enough to restituate the geography of the situation .   
    
    temp = (lat_sbt, sat[0])
    new_dist = great_circle(sbt,temp).miles
    new_dist= new_dist * 1.60934
    
    beta = float(acos(new_dist/dist))
        
    if  robusta[0] >= sbt[0] and robusta[1] >= sbt[1] :
        deg_sat = beta
        
    elif robusta[0] > sbt[0] and robusta[1] < sbt[1] :
        deg_sat = pi - beta
            
    if  robusta[0] < sbt[0] and robusta[1] < sbt[1] :
        deg_sat = pi + beta
        
    elif robusta[0] < sbt[0] and robusta[1] > sbt[1] :
        deg_sat= 2*pi - beta 
   
    deg_sat = degrees(deg_sat)
    
    #Moreover we have to take in consideration ship's orientation ( data based on the true north).  
    
    deg_az = deg_sat - deg_sbt
    
    deg_az= float("{0:.2f}".format(deg_az)) 
    
    return ([deg_az,deg_el])
    
