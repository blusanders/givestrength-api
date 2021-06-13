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
    fromAddress = [36.17915, -86.75908]

    helpArray = [
        [36.17213, -86.75485],	
        [36.1844, -86.74291],
        [36.18869, -86.76962],	
        [36.196770, -86.745057]
    ]

    for latlong in range(len(helpArray)):
        print(
            latlong,
            getDistance(
            fromAddress[0],
            fromAddress[1],
            helpArray[latlong][0],
            helpArray[latlong][1]
            ))

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
    d = d*.62
    return d

getHelp()