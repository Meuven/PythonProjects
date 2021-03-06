#software control for SPID rot2prog

# We can fine the protocol here : http://ryeng.name/blog/3 

# We are going first to declare our listes and variables #

from math import *
import numpy as np 
import matplotlab.py as plt 
from pyorbital import tlefile
import serial 
import time 
from datetime import datetime

              
 #we are going to first decoded the tle. The information we're are going to extract, is the time when the 
# sat will be in the area, and it coordonates .

def decode_TLE():

#here we can find more explanations about the module pyorbital here : https://pyorbital.readthedocs.io/en/latest/

    sat = tlefile.read('INMARSAT 3-F1'	,'C:\Users\Student-CIC-05\Desktop\Meuven\code\TLE.txt')
# we can use the command "Orbital", thanks to whom (with the name of the sat) we get directly on the internet the sat's TLE
    now = datetime.utcnow()
    coor_sat= sat.get_lonlatalt(now)
    return (coor_sat)         # gives a tuples with long, lat , alt 



# in this part we're going to collect the ship's coordonate and calculate with the TLE the al and az every T secondes.
# The track mode will be actived 6 min before the sat comes in the reception area.

def decode_ship():
    az_el = []
    TLE = ?
    duration mission = ?
    
    port= ?
    baud = ?
    timeout = ?
    
    ser = serial.Serial( port, time, baud) 
    
    while loop duration mission  > 0:
        k = 0                       #this is a summer that will determinate how many elements we have on our list 
        output = $GGA
        cmd = ser.write(output)     # this first commande will write the lat, direction lat,
                                    # the long and direction long
        time.sleep(0,25)                 # wait for an answer
        
        output= $HDT
        cmd = ser.write(output)     # this commande will write the orientation based on the geo north
        time.sleep(0.25) 
        
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
            time.sleep(T)
        
        
# now we juste create our two list in which we have the lat, the long and the orientation of the SBT.
# With the TLE we can now calculate the orientation az and el of the rotor 
        
        
        else :
            out = print("error")
            az_el.append(out)
            k+= 1
            return(az_el)
            time.sleep(T)                #wait the T time for the next commande
        duration mission = duration mission + 0.5 -T
    
    ser.close()
