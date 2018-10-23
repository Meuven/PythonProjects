#software control for SPID rot2prog

# We can fine the protocol here : http://ryeng.name/blog/3 

# We are going first to declare our listes and variables #

from math import *
import numpy as np 
from np import *
import matplotlab.py as plt 
from plt import *
import ephem
import serial 
from time import sleep

#class calcul:
    #time sleep = 0.1
    #def __init__(self, ip, port,baud,timeout, time_to_stop=None, frequency=None, leep_time=None):
        #self.IP = ip 
        #self.PORT = port 
        #self.BAUD = baud 
        #self.TIMEOUT = timeout 
        


        
        
 #we are going to first decoded the tle. The information we're are going to extract, is the time when the 
# sat will be in the area, and it coordonates .


#On artificial satellites, also sets:
#Geographic point beneath satellite:
#sublat — Latitude (+N)
#sublong — Longitude (+E)

#elevation — Geocentric height above sea level (m)
#range — Distance from observer to satellite (m)
#range_velocity — Range rate of change (m/s)
  

def decode_TLE(TLE):
    TLE ='''0 INMARSAT 3-F1
1 23839U 96020A   14066.96754476 -.00000012  00000-0  10000-3 0  9995
2 23839 001.6368 073.2937 0005131 268.7608 236.3372 01.00266000 65663'''    # we will use this TLE for our examples 
    sat = ephem.readtle(*[line for line in tle.split('\n')])
    lat = sat.sublat                            # answer string  in deg min sec 
    lng = sat.sublong
    alt = sat.elevation
    coor_sat = [lat,lng,alt]
    return (coor_sat)



# in this part we're going to collect the ship's coordonate and calculate with the TLE the al and az every T secondes.
# The track mode will be actived 6 min before the sat comes in the reception area.

def decode_ship():
    az_el = []
    TLE = ?
    duration mission = ?
    while loop duration mission  > 0:
        k = 0                       #this is a summer that will determinate how many elements we have on our list 
        output = $GGA
        cmd = ser.write(output)     # this first commande will write the lat, direction lat,
                                    # the long and direction long
        sleep(0,25)                 # wait for an answer
        output= $HDT
        cmd = ser.write(output)     # this commande will write the orientation based on the geo north
        sleep(0.25) 
        if Serial.available > 0 :
        rep= ser.read(1000)
            rep.split("$")
            lat_lg = rep[0]         # see doc user netR9 to understand how the message is composated 
            lat_lg.split(",")
            deg = rep[1]
            deg.split(",")
            sat = decode_TLE(TLE)
            az_el.append( calcul( deg, lat_lg,sat))  # liste of 2 elem with az_el[0] = az and az_el[1] = el of the rotor
            k+=1
            return(az_el,k)
            sleep(T)
        
        
# now we juste create our two list in which we have the lat, the long and the orientation of the SBT.
# With the TLE we can now calculate the orientation az and el of the rotor 
        
        
        else :
            out = print("error")
            az_el.append(out)
            k+= 1
            return(az_el)
            sleep(T)                #wait the T time for the next commande
        duration mission = duration mission + 0.5 -T
    
    ser.close()

  


        
        

     

        



          

 
            
      
    
  
  
