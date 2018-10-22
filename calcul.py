# now we get our sat and ship coordonate, we can calcul the az and el for the rotor .
# this code should be easy and fast to calculate the command for the rotor every seconde .

def calcul(deg, lat_lg,sat):
    

# in the first time we aregoing to calculate the distance between two points on a map 
# el = arctan( alt/dis) dis to determinate by the lat and long 

#The lyb I found to calculate the distance between 2 point of the map : latlon .
# We can fin here the different functions of the lyb :https://pypi.org/project/LatLon/#description

#note : ephem gives the lat and long coor on deg min sec . This one should be convert first in deg decimal for the calcul
#note : the converstion could be do with the cal for a lat for example (lat = d.m.s), lat_dec = d+(m/60)+(s/3600)

lat_sat = 






# note : GNSS give the lat and long coor on  deg decimal . it's ok  for the calcul .
