#software control for SPID rot2prog

# We can fine the protocol here : http://ryeng.name/blog/3 

# We are going first to declare our listes and variables #

from math import *
import numpy as np 
from np import *
import matplotlab.py as plt 
from plt import *
from ephem import *


commande = [0]*13                   # command packet get 13 byte,  ASCII characters for az and el
commande[0] = 0x57                  # S (start) shall always be 0x57
commande[12] = 0x20                 # End                    be 0x20 

reponse = [0]*12                    # reponse packet get 12 byte, Byte values for az and el
reponse[0] = 0x57
reponse[11] = 0x20
reponse[5] = 0x01                   # We gonna put for the moment resolution to 1deg/pulse
reponse[10] = reponse[5]            # so we put the resolution to 1

shipaz = [0]*4   # Here we'll be save the orientation of the ship, ASCII characters for az 
                                    # note that  the ship doesn't have El orientation

  
                                    # Note that the netR9 has an HDT command which gives us directly the orientation of the sbt based on 
                                    # the geo north. The idea here is to save every last orientation to predict the orientation of the sbt
                                    # when the mission will start.
  
def init(T,10) :                     # T is the time of the mission, t is the number of coordonates we will need .
  G = []
  gps= open("gps.txt","a")
  for i in range(int(T)+1) :        # T could be a float #
    time.sleep(1)
    gps.write("d°/n")
    G.append("d°")
    if len(G) > 10 :                 # For our need to calculate, we will only keep the t last gps informations
      del G[0]
        



          

 
            
      
    
  
  
