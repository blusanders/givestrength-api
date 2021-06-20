"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from givestrapi.models import Person, PersonType
from django.contrib.auth.models import User
import urllib.request
import json
import math

class PersonViewSet(ViewSet):
    """Give Your Strength Person"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized Person instance
        """

        user = Person.objects.get(user=request.auth.user)

        person = Person()
        person.street = request.data["street"]
        person.city = request.data["city"]
        person.state = request.data["state"]
        person.zip = request.data["zip"]
        person.bio = request.data["bio"]
        person.popup = request.data["popup"]
        person.latitude = request.data["latitude"]
        person.longitude = request.data["longitude"]

        person_type = PersonType.objects.get(pk=request.data["person_type_id"])
        person.person_type = person_type

        try:
            person.save()
            serializer = PersonSerializer(person, context={'request': request})
            return Response(serializer.data)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handle GET requests for a person

        Returns:
            Response -- JSON serialized person instance
        """
        try:
            #http://localhost:8000/person/2
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person, context={'request': request})
            return Response(serializer.data,)

        except Exception as ex:
            return HttpResponseServerError(ex, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        """Handle PUT requests for a Person

        Returns:
            Response -- Empty body with 204 status code
        """

        person = Person.objects.get(pk=pk)
        # person = Person.objects.get(user=request.auth.user)

        person.user.first_name = request.data["first_name"]
        person.user.last_name = request.data["last_name"]
        person.user.email = request.data["email"]
        person.user.username = request.data["username"]

        person.street = request.data["street"]
        person.city = request.data["city"]
        person.state = request.data["state"]
        person.zip = request.data["zip"]
        person.phone = request.data["phone"]
        person.bio = request.data["bio"]
        person.popup = request.data["popup"]

        latlong = geo_get(
            request.data["street"],
            request.data["city"],
            request.data["state"],
            request.data["zip"],
        )

        print("latlong: ", latlong)

        person.latitude = latlong[0]
        person.longitude = latlong[1]
        person.person_type_id = request.data["person_type_id"]

        person.user.save()
        person.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single person

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            person = Person.objects.get(pk=pk)
            person.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Person.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to person resource

        Returns:
            Response -- JSON serialized list of people within a given distance
        """
        #get all people, filter by distance
        current_user = Person.objects.get(user=request.auth.user)
        
        #get all people w distances. Zero distance = logged in user.
        person = Person.objects.all()

        #get all markers within distance except logged in use
        # person = Person.objects.exclude(user=request.auth.user)

        #calc distance bet lat/long and logged in user lat/long
        #http://localhost:8000/person?distance=1

        distance = self.request.query_params.get('distance', None)

        if distance is not None:

            def distance_filter(person):
                from_lat = current_user.latitude
                from_long = current_user.longitude
                to_lat = person.latitude
                to_long = person.longitude

                #distance bet each user and the logged in user
                distance_bet = get_distance(from_lat, from_long, to_lat, to_long)
                print(person.id, person.user.first_name, distance_bet)
                person.distance = distance_bet
                
                if (distance_bet<=float(distance)):
                    return True
                return False

            person = filter(distance_filter, person)

        serializer = PersonSerializer(
            person, many=True, context={'request': request})
        return Response(serializer.data)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'is_staff', 'is_active', 'email')

class PersonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonType
        fields = ['id','description']

class PersonSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    person_type = PersonTypeSerializer(many=False)

    class Meta:
        model = Person
        fields = (
            'id', 
            'user',
            "person_type",
            'street',
            'city',
            'state', 
            'zip', 
            'phone', 
            'bio',
            'popup',
            'latitude', 
            'longitude',
            "distance",
        )
        depth = 1

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

    distance=1
    within_distance = []

    for latlong in range(len(help_array)):
        distance_away = get_distance(
        from_address[0],
        from_address[1],
        help_array[latlong][0],
        help_array[latlong][1]
        )
        if distance_away<=distance:
            within_distance.append(help_array[latlong])
    print(within_distance)

def get_distance(from_lat,from_long, to_lat, to_long):

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


def geo_get(street, city, state, zip):

    q = f"{street} {city} {state} {zip}"
    q = q.replace(" ", "+")

    fetchURL = f"https://nominatim.openstreetmap.org/search?q={q}&format=geojson"
    print("fetch: ", fetchURL)
    contents = urllib.request.urlopen(fetchURL).read()

    JSON_object = json.loads(contents)
    
    # try:
    #     lat = JSON_object['features'][0]['geometry']['coordinates'][0]
    # except IndexError:
    #     gotdata = 'null'
    
    # if gotdata:
    #     lat = JSON_object['features'][0]['geometry']['coordinates'][0]
    #     long = JSON_object['features'][0]['geometry']['coordinates'][1]
    # else:   
    #     lat = ""
    #     long = ""

    if len(JSON_object['features'])>0:
        lat = JSON_object['features'][0]['geometry']['coordinates'][0]
        long = JSON_object['features'][0]['geometry']['coordinates'][1]
    else:   
        lat = ""
        long = ""

    return [lat,long] 

