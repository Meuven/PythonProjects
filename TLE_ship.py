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

        
        
        
        
#Open port for the NetR9 GPS 
ser = serial.Serial(port, baud, timeout)


#we are going to first decoded the tle. The information we're are going to extract, is the time when the 
# sat will be in the area, and it coordonates .     









# this part is the part where we  collect the ship coordonate and  calculate with the TLE the al and avec every T secondes.

duration mission = ?
while loop duration mission  > 0:
    output = $GGA
    cmd = ser.write(output)     # this first commande will write the lat, direction lat,
                                # the long and direction long
    sleep(0,1)                  # wait for an answer
    output= $HDT
    cmd = ser.write(output)     # this commande will write the orientation based on the geo north
    sleep(0.1) 
    if Serial.available > 0 :
        rep= ser.read(1000)
        rep.split("$")
        lat_lg = rep[0]
        lat_lg.split(",")
        deg = rep[1]
        deg.split(",")
        az_el = calcul( deg, lat_lg, TLE)  
        sleep(T)
        
        
# now we juste create our two list in which we have the lat, the long and the orientation of the SBT.
# With the TLE we can now calculate the orientation az and el of the rotor 
        
        
    else :
        print("error")
        sleep(T)                #wait the T time for the next commande
    duration mission = duration mission -T + 0.2
    
ser.close()
return(az_el)

  


        
        

     

        



          

 
            
      
    
  
  
