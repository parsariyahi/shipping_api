from math import radians, cos, sin, asin, sqrt
from random import randint

def distance(lat1, lat2, long1, long2):
    # Haversine formula
     
    long1 = radians(long1)
    long2 = radians(long2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    dlong = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlong / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    r = 6371

    return(c * r)

def get_driver_location(driver_id):
    # here we will call the driver location api.
    #requests.get(URL)

    latitude = randint(-100, 100)
    longitude = randint(-100, 100)

    return latitude, longitude