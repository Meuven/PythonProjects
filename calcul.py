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
( reprendre net R9 page 77 )
        
        
        
        
#Open port for the NetR9 GPS 
ser = serial.Serial(port, baud, timeout)

# Note that the netR9 has an HDT command which gives us directly the orientation of the sbt based on the geo north.
    loop = 1
    while loop ==1:
        output = ?
        cmd = ser.write(output)
        sleep(0,1)              # wait for an answer
        
        if ser.avaible() ==0 :  # if not answer wait the time T to have a new coordonate of the w
            sleep(T)
        else:
            ship = ser.read(1000)
            loop = 0
            ser.close()
     

        



          

 
            
      
    
  
  
