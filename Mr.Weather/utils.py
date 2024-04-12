from typing import Tuple, NamedTuple
from collections import namedtuple
from geopy.geocoders import Nominatim


def get_location(address:str='Paris') ->NamedTuple:
    geolocator = Nominatim(user_agent='MyApp')
    location = geolocator.geocode(address)
    GeoCoord = namedtuple('GeoCoord', ['lat', 'lon']) 
    
    return GeoCoord(location.latitude, location.longitude)

if __name__=='__main__':
    geo_coord = get_location(address='Paris')
    print(geo_coord.lat, geo_coord.lon)