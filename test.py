import urllib.request
import json
from math import sin, cos, sqrt, atan2, radians
import math

def geoGet():

    street = "301 Neill Ave"
    city = "Nashville"
    state = "TN"
    zip = "37206"
    q = f"{street} {city} {state} {zip}"
    # q = q.replace(" ", "+")

    fetchURL = f"https://nominatim.openstreetmap.org/search?q={q}&format=geojson"
    contents = urllib.request.urlopen(fetchURL).read()

    JSON_object = json.loads(contents)
    print("LAT: ", JSON_object['features'][0]['geometry']['coordinates'][0])
    print("LONG: ", JSON_object['features'][0]['geometry']['coordinates'][1])


def getHelp() :
    from_address = [36.17915, -86.75908] #logged in user

    #all TN addresses
    #ask Will about filtering data first
    #searching all addresses not realistic
    help_array = [
        [36.17213, -86.75485], #.53
        [36.1844, -86.74291], #.96
        [36.18869, -86.76962], #.88	
        [36.196770, -86.745057] #1.44
    ]

    distance=.55
    within_distance = []

    for latlong in range(len(help_array)):
        distance_away = getDistance(
        from_address[0],
        from_address[1],
        help_array[latlong][0],
        help_array[latlong][1]
        )
        if distance_away<=distance:
            within_distance.append(help_array[latlong])
    print(within_distance)

def getDistance(from_lat,from_long, to_lat, to_long):

    #takes to and from lat/long
    #returns distance in miles bet those points

    radius = 6371  # km

    dlat = math.radians(to_lat - from_lat)
    dlon = math.radians(to_long - from_long)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(from_lat)) * math.cos(math.radians(to_lat)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    d = d*.62 #returns miles
    return d

getHelp()