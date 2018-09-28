#software control for SPID rot2prog

# We can fine the protocol here : http://ryeng.name/blog/3 

# We are going first to declare our listes and variables #

from math import *


commande = [0]*13 # command packet get 13 byte,  ASCII characters for az and el
commande[0] = 0x57                  # S (start) shall always be 0x57
commande[12] = 0x20                 # End                    be  0x20 "

reponse = [0]*12   # reponse packet get 12 byte, Byte values for az and el
reponse[0] = 0x57
reponse[11] = 0x20
reponse[5] = 0x01                   # We gonna put for the moment resolution to 1deg/pulse
reponse[10] = reponse[5]            # so we put the resolution to 1

shipaz = [0]*4   # Here we'll be save the orientation of the ship, ASCII characters for az 
                                    # note that  the ship doesn't have El orientation.

  
  # We will suppose that a file "gps.txt" existe, in which we can find every last al,lg gps  informations saved"
  # Our GPS send informations with à 50 MHz speed, we will create our file with a 1Hz speed" 
  
  def init(T,t) :
    G = []
    gps= open("gps.txt","a")
    for i in range(int(T)+1) :    # T could be a float #
      time.sleep(1)
      gps.write("al,lg /n")
      G.append("al,lg)
      if len(G) > t :            # For our need to calculate, we will only keep the t last gps informations
               del G[0]
  
            
            
    
  
      
    
  
  
