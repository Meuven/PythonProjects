#software control for SPID rot2prog

# here can be found the protocol here : http://ryeng.name/blog/3 

# We are going first to declare our listes and variables #

import serial
import time
import os 
# get the Comm Port information
timeout = ?
port = ?
baud = ?

#Open Comm Port
ser = serial.Serial(port, baud, timeout = 0)

def rotator_mode ():
	#cmd = ['0']*12                    # cmd packet get 12 byte, Byte values for az and el
	#cmd[0] = 'W'			  # ASCII charac for 0x57
	#cmd[11] = ' '			  # ASCII charac for 0x20

	az_max = 360
	az_min = 0
	el_max = 180 
	el_min = 0 
	loop = 1
	zero5 = chr(0)+chr(0)+chr(0)+chr(0)+chr(0)             # this variable will serve to give the commande to the driver 

# firstly we are going to code the several mode of the drivers: mode stop(0F), mode status(1F), mode set(2F) and mode quit.  
# To have a full understanding of the code report to the protocol and to this link :
#http://alfaradio.ca/downloads/program_info/Program_format-Komunicacji-2005-08-10-p2.pdf


# As I don't really know the port and input yet, 
#we'r going to work with reponse liste as if they contained our datas.


	print ("Enter stop to stop rotation.")
	print ("Enter status to update rotator status.")
	print ("Enter quit to quit program.")
	print ("Enter set to quit program.")


#Get desired az and mode at the same time.
   	print (" ")
   	mode = input ("Enter mode: ")
   

	loop = 1
	while loop == 1 :		
		if mode == 'stop' :                  	        # this mode juste stops the rotator and gives the az and el 
			output = chr(87)+zero5+zero5+chr(15)+chr(32) 	# this cmd will stop the rotator
	    		cmd= ser.write(output)
    			time.sleep(1)                        		# wait for an answer

    			rep = ser.read(1000)
#Now it's time to give the reponse to the user, before, we need to convert our datas:
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
    			print ("Azimuth multiplier is %3d "%(az_res)+ "  Elevation Multiplier is %3d "%(el_res))
      
      
		elif mode == 'status' :
    			# Build the status command word.
    			output = chr(87)+zero5+zero5+chr(31)+chr(32)
    			cmd= ser.write(output)
    			time.sleep(1) 

    			rep = ser.read(1000)
			# Now as the stop commande,we're going to give the az and el but the rotator is still running
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
    			print ("Azimuth multiplier is %3d "%(az_res)+ "  Elevation Multiplier is %3d "%(el_res))

 		elif mode == 'set' :
# now we have the az, we are not in the 3 other modes, so we are automatically in the "set mode",
# so we ask the el to the rotator execute the commande.
			print(" ")
			input_az = input("Enter azimuth: ")
			print(" ")
   			input_el = input("Enter Elevation: ")
			az = int(input_az)%360
           		el = int(input_el)%180
		
		#see the protocol 
			az = az + 360
                	el = el + 360
                
			multi = 1 		# multi will be fixed according to the accuracy we need 
              		az = az * multi
              		el = el * multi

              		azm = str(az)
              		elm = str(el)
              		if len(azm) == 3:
                 		azm = "0" + azm
              		if len(elm) == 3:
                 		elm = "0" + elm
  
             		# Build message to be sent to controller
	      		output =  chr(87) + azm + chr(multi)+elm + chr(multi)+chr(47)+chr(32) # this cmd will stop the rotator
	      		cmd= ser.write(output)
    	      		time.sleep(1)                        # wait for an answer
	
		elif mode == 'quit':
			loop = 0 
	ser.close()
	     
