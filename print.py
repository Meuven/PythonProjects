#software control for SPID rot2prog

# We can fine the protocol here : http://ryeng.name/blog/3 

# We are going first to declare our listes and variables #


commande = [ 0 for k in range(13) ] # command packet get 13 byte,  ASCII characters for az and el
commande[0] = 0x57                  # S (start) shall always be 0x57
commande[12] = 0x20                 # End                    be  0x20 "

reponse = [0 for k in range(12) ]   # reponse packet get 12 byte, Byte values for az and el
reponse[0] = 0x57
reponse[11] = 0x20
reponse[5] = 0x01                   # We gonna put for the moment resolution to 1deg/pulse
reponse[10] = reponse[5]            # so we put the resolution to 1

shipaz = [ 0 for k in range(4) ]    # Here we'll be save the orientation of the ship, ASCII characters for az 
                                    # note that  the ship doesn't have El orientation.
  
