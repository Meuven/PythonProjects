#software control for SPID rot2prog

# here can be found the protocol here : http://ryeng.name/blog/3 

#Here can be found more precise example to understand the systeme 

# We are going first to declare our listes and variables #


from math import *
import numpy as np 
from np import *
import matplotlab.py as plt 
from plt import *
import ephem 
import serial
import time
import os 
from time import sleep


cmd = [0]*13                   # command packet get 13 byte,  ASCII characters for az and el
cmd[0] = 0x57                  # S (start) shall always be 0x57 = 87
cmd[12] = 0x20                 # End                    be 0x20 = 32

rep = ['0']*12                    # reponse packet get 12 byte, Byte values for az and el
rep[0] = 'W'
rep[11] = ' '


azi_max = 360
azi_min = 0
ele_max = 180 
ele_min = 0 
loop = 1
zero5 = chr(0)+chr(0)+chr(0)+chr(0)+chr(0)             # this variable will serve to give the commande to the driver 

# firstly we are going to code the several mode of the drivers: mode stop(0F), mode status(1F), mode set(2F), et mode quit  
# To have a full understanding of the code report to the protocol and to this link :
#http://alfaradio.ca/downloads/program_info/Program_format-Komunicacji-2005-08-10-p2.pdf


# As I don't really know the port and input yet, 
#we'r going to work with the liste commande and reponse as our intput as if they contained our datas.

# get the Comm Port information
#input_variable = raw_input ("Enter comm port: ")
#port = (input_variable)
#input_variable = input("Enter comm port baud rate: ")
#baud = (input_variable)




print ("Enter stop to stop rotation.")
print ("Enter status to update rotator status.")
print ("Enter quit  to quit program.")
#Get desired azimuth
   print (" ")
   input_variable = input ("Enter mode:")
   mode = str(input_variable)

loop = 1
while loop == 1 :
  if mode == "stop" :               # in this mode we just stop the rotator and have back the az and el 
    output = chr(87)+zero5+zero5+chr(15)+chr(32)
    cmd = open('data.txt', 'a')     # the format.txt is not the good one 
    cmd.write(output)
    cmd.close
    sleep(1)                        # wait for an answer 
      
#Now it's time to give the réponse to the user, before, we need to convert our datas:
    H1 = ord(rep[1])
    H2 = ord(rep[2])
    H3 = ord(rep[3])
    H4 = ord(rep[4])
    az_res = ord(rep[5])
    V1 = ord(rep[6])
    V2 = ord(rep[7])
    V3 = ord(rep[8])
    V4 = ord(rep[9])
    el_res = ord(rep[10])
  
    azs = H1*100 + H2*10 + H3 + H4/10
    els = V1*100 + V2*10 + V3 + V4/10
	 # Since the controller sends the status based on 0 degrees = 360
         # remove the 360 here
    azs = azs - 360
    els = els - 360
    print ("Rotator stopped at %3d " %(azs)+ "Degrees Azimuth and %3d " %(els) + "Degrees Elevation")
    print ("Azimuth multiplier is %3d "%(az_res)+ "  Elevation Multiplier is %3d "%(el_res)
      
      
               
      
  


                                                                                                                                                                  
