from math import *
import pyorbital
from pyorbital import tlefile
from pyorbital.orbital import Orbital
import serial 
import time 
from datetime import datetime
import os
import sat_class
import predict
import rotator_treshold_test

def rotator_set (azel,v):

    if v == False:      
        az = 0
        el = 90
            
        print(('waiting \n azimuth = %f    elevation = %f\n\n')%(az,el))

            
    else:
        az = azel[0]
        
        if azel[1] < 0:
            el  = 0
            
        else :
            el = azel[1]
        print(('tracking satellite \n azimuth = %f    elevation = %f\n\n')%(az,el))




        
def satellite_track(): 
    k=0
    saved = [0]
    p = '?'
    b = '?'
        

    sat = sat_class.Satellite()
    mission = predict.Mission()
    verif = mission.verif 
     
    if verif == False:
        mission = predict.Mission()
        now= mission.now
        print(now)
        azel = [0,0]                        # we don't need to put azel here we are in waiting mode .
        rotator_set(azel,verif)
        time.sleep(29)
            
            
            

    else :
        
        mission= predict.Mission()
        print("current time1:   ",mission.now,'\n',mission.start,'     ',mission.end)
        verif1 = mission.verif
        end = mission.end
        now2 = mission.now

        while now2 <= end :
                
                azel = rotator_treshold_test.az_correct(saved[k])
                rotator_set(azel,verif1)
                saved.append(rotator_treshold_test.az_correct(azel[0]))
                k+=1
                mission = predict.Mission()
                now2 = mission.now
                print(now2)
                time.sleep(0.8)
        print('reboot')
        # je voudrai que le programme reboot ici pour pouvoir se synchroniser avec l'heure du pc"
            




while True :
    satellite_track()




