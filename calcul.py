# now we get our sat and ship coordonate, we can calcul the az and el for the rotor .
# this code should be easy and fast to calculate the command for the rotor every seconde .

def calcul(deg, lat_lg,sat):
    
# we first are going to calculate the az which is easier because it only depends on the ship's orientation .
# in the first time we aregoing to calculate the distance between two points on a map 
# el = arctan( alt/dis) dis to determinate by the lat and long 
