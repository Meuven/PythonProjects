# now we get our sat and ship coordonate, we can calcul the az and el for the rotor .
# this code should be easy and fast to calculate the command for the rotor every seconde .

def calcul(deg, lat_lg,sat):
    
# we first are going to calculate the az which is easier because it only depends on the ship's orientation .
# in the first time we aregoing to calculate the distance between two points on a map 
# el = arctan( alt/dis) dis to determinate by the lat and long 
# two modules were find to calculate the distance between 2 point of the map .
# The first one is Geopy  and the seconde one est Mpu.

#note : ephem gives the lat and long coor on deg min sec . This one should be convert first in deg decimal for the calcul
# see ephem angle to convert 
# note : GNSS give the lat and long coor on  deg decimal . it's ok  for the calcul .
